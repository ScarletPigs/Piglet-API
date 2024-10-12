using Microsoft.AspNetCore.Mvc;

namespace Piglet_API.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class EventsController : Controller
    {

        [HttpGet]
        public IActionResult Get()
        {
            return View();
        }

        [HttpGet("{id}")]
        public IActionResult Get(int id)
        {
            return View();
        }

        [HttpGet]
        public IActionResult Get([FromQuery] DateTime fromDate, [FromQuery] DateTime toDate)
        {
            return View();
        }
    }
}
