using Microsoft.AspNetCore.Mvc;
using Piglet_API.Repositories;
using Piglet_Domain_Models.Models;

namespace Piglet_API.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class EventsController : Controller
    {

        private IEventRepository EventService { get; set; }

        public EventsController(IEventRepository eventService)
        {
            EventService = eventService;
        }

        [HttpGet]
        public IActionResult Get()
        {
            return Ok(EventService.GetEvents());
        }

        [HttpGet]
        public IActionResult Get([FromQuery] DateTime fromDate, [FromQuery] DateTime toDate)
        {
            return Ok(EventService.GetEvents(fromDate, toDate));
        }

        [HttpGet("{id}")]
        public IActionResult Get(int id)
        {
            return Ok(EventService.GetEvent(id));
        }

        [HttpPost]
        public IActionResult Post([FromBody] Event eventobj)
        {
            return Ok(EventService.CreateEvent(eventobj));
        }

        [HttpPut]
        public IActionResult Put([FromBody] Event eventobj)
        {
            return Ok(EventService.UpdateEvent(eventobj));
        }

        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            return Ok(EventService.DeleteEvent(id));
        }
    }
}
