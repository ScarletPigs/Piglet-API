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
        public async Task<IActionResult> Get()
        {
            return Ok(await EventService.GetEvents());
        }

        [HttpGet("fromto")]
        public async Task<IActionResult> Get([FromQuery] DateTime fromDate, [FromQuery] DateTime toDate)
        {
            return Ok(await EventService.GetEvents(fromDate, toDate));
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> Get(int id)
        {
            return Ok(await EventService.GetEvent(id));
        }

        [HttpPost]
        public async Task<IActionResult> Post([FromBody] Event eventobj)
        {
            return Ok(await EventService.CreateEvent(eventobj));
        }

        [HttpPut]
        public async Task<IActionResult> Put([FromBody] Event eventobj)
        {
            return Ok(await EventService.UpdateEvent(eventobj));
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> Delete(int id)
        {
            return Ok(await EventService.DeleteEvent(id));
        }
    }
}
