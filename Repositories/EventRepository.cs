using Microsoft.EntityFrameworkCore;
using Piglet_API.Data;
using Piglet_Domain_Models.Models;

namespace Piglet_API.Repositories
{
    public interface IEventRepository
    {
        public Task<IEnumerable<Event>> GetEvents();
        public Task<IEnumerable<Event>> GetEvents(DateTime fromDate, DateTime toDate);
        public Task<Event> GetEvent(int id);
        public Task<Event> CreateEvent(Event eventobj);
        public Task<Event> UpdateEvent(Event eventobj);
        public Task<Event> DeleteEvent(int id);
    }

    public class EventRepository : IEventRepository
    {
        private PigletDBContext DBContext { get; set; }

        public EventRepository(PigletDBContext context)
        {
            DBContext = context;
        }

        public async Task<IEnumerable<Event>> GetEvents()
        {
            return await DBContext.Events.AsNoTracking().ToListAsync();
        }

        public async Task<IEnumerable<Event>> GetEvents(DateTime fromDate, DateTime toDate)
        {
            return await DBContext.Events.AsNoTracking().Where(e => e.StartTime >= fromDate && e.EndTime <= toDate).ToListAsync();
        }

        public async Task<Event?> GetEvent(int id)
        {
            return await DBContext.Events.AsNoTracking().FirstOrDefaultAsync(e => e.Id == id);
        }

        public async Task<Event> CreateEvent(Event eventobj)
        {
            await DBContext.Events.AddAsync(eventobj);
            await DBContext.SaveChangesAsync();
            return eventobj;
        }

        public async Task<Event> UpdateEvent(Event eventobj)
        {
            DBContext.Events.Update(eventobj);
            await DBContext.SaveChangesAsync();
            return eventobj;
        }

        public async Task<Event> DeleteEvent(int id)
        {
            var eventobj = await DBContext.Events.FirstOrDefaultAsync(e => e.Id == id);
            DBContext.Events.Remove(eventobj);
            await DBContext.SaveChangesAsync();
            return eventobj;
        }
    }
}
