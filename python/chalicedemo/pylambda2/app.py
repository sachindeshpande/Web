from chalice import Chalice, Response
from chalice import NotFoundError
import json
import boto3
from botocore.exceptions import ClientError

from chalice import NotFoundError

app = Chalice(app_name='helloworld')
app.debug = True

CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR',
}


#S3 = boto3.client('s3', region_name='us-east-1')
BUCKET = 'sactmo-testbuck'
s3Resource = boto3.resource('s3')
s3Client = boto3.client('s3', region_name='us-east-2')

@app.route('/authenticated', methods=['GET'], api_key_required=True)
def authenticated():
    return {"secure": True}


@app.route('/objects/{key}', methods=['GET', 'PUT'])
def s3objects(key):
    request = app.current_request
    if request.method == 'PUT':
        s3Resource.Bucket(BUCKET).put_object(Key=key,
                      Body=json.dumps(request.json_body))
    elif request.method == 'GET':
        try:
            print('key = ' + key)
            response = s3Client.get_object(Bucket=BUCKET, Key=key)
            result = response['Body'].read()
            print(result)
            return json.loads(result)
        except ClientError as e:
            raise NotFoundError(key)


@app.route('/')
def index():
    return Response(body='hello world!',
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})

@app.route('/cities/{city}')
def state_of_city(city):
    try:
        return {'state': CITIES_TO_STATE[city]}
    except KeyError:
        raise BadRequestError("Unknown city '%s', valid choices are: %s" % (
            city, ', '.join(CITIES_TO_STATE.keys())))

@app.route('/resource/{value}', methods=['PUT'])
def put_test(value):
    return {"value": value}

@app.route('/myview', methods=['POST', 'PUT'])
def myview():
    pass

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
