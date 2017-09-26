using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using System.Web.Http;
using System.Web.Http.Description;
using WebApp4.Models;

namespace WebApp4.Controllers
{
    public class ValuesController : ApiController
    {
        // GET api/values
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/values/5
        public string Get(int id)
        {
            return "value";
        }

        // POST api/values

        // POST api/values
        [HttpPost]
        [ResponseType(typeof(ProductItem))]
        public async Task<IHttpActionResult> Post([FromBody] ProductItem item)
        {
            ProductItem newItem = item;
            newItem.Price = newItem.Price * (decimal).80;


            return CreatedAtRoute("DefaultApi", new { controller = "messages", id = 3 }, newItem);
        }

        /*
        public void Post([FromBody]ProductItem value)
        {
            ProductItem newVal = value;
            return CreatedAtRoute("DefaultApi", new { controller = "messages", id = 3 }, "This is a test response");
        }
        */
        // PUT api/values/5
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/values/5
        public void Delete(int id)
        {
        }
    }
}
