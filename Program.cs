
using Microsoft.EntityFrameworkCore;
using Microsoft.OpenApi.Models;
using Piglet_API.Data;
using Piglet_API.Repositories;
using System.Reflection;

namespace Piglet_API
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);


            builder.Services.AddControllers();

            // Register services
            builder.Services.AddScoped<IEventRepository, EventRepository>();

            // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
            builder.Services.AddEndpointsApiExplorer();
            builder.Services.AddSwaggerGen(options =>
            {
                options.SwaggerDoc("v1", new OpenApiInfo { Title = "Piglet API", Version = "v1" });
                options.IncludeXmlComments(Path.Combine(AppContext.BaseDirectory, $"{Assembly.GetExecutingAssembly().GetName().Name}.xml"));
            });

            builder.Services.AddDbContext<PigletDBContext>(options =>
            {
                options.UseNpgsql(Environment.GetEnvironmentVariable("PigletDBContext") ?? "");
            });

            var app = builder.Build();

            // Run database migrations
            using (var scope = app.Services.CreateScope())
            {
                var services = scope.ServiceProvider;
                var context = services.GetRequiredService<PigletDBContext>();
                context.Database.Migrate();
            }

            // Configure the HTTP request pipeline.
            if (app.Environment.IsDevelopment())
            {
                app.UseSwagger();
                app.UseSwaggerUI();
            }

            app.UseAuthorization();


            app.MapControllers();

            app.Run();
        }
    }
}
