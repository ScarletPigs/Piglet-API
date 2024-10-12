using Microsoft.EntityFrameworkCore;

namespace Piglet_API.Data
{
    public class PigletDBContext : DbContext
    {
        public PigletDBContext(DbContextOptions<PigletDBContext> options) : base(options)
        {
        }
    }
}
