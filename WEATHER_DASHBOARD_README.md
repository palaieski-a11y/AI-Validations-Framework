# Weather Dashboard API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-blue.svg)](https://fastapi.tiangolo.com/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A modern, production-ready weather dashboard API built with FastAPI, PostgreSQL, and Redis. Fetches real-time weather data from OpenWeatherMap API with intelligent caching.

## 🌟 Features

✅ **Real-Time Weather Data**
- Current weather conditions (temperature, humidity, wind, pressure)
- 5-day weather forecast
- Location search with autocomplete
- Weather alerts and warnings
- UV index and air quality data

✅ **Performance Optimized**
- Redis caching (10-minute TTL)
- Async/await architecture
- Connection pooling
- Health checks and monitoring

✅ **Enterprise Ready**
- Type-safe Pydantic validation
- Comprehensive error handling
- Structured logging
- Docker containerization
- API documentation with Swagger UI

✅ **Developer Friendly**
- FastAPI with auto-generated docs
- Easy local development with Docker Compose
- Environment-based configuration
- Comprehensive Makefile

## 📋 Prerequisites

- Python 3.9+
- Docker & Docker Compose
- OpenWeatherMap API key (free: https://openweathermap.org/api)
- PostgreSQL 12+
- Redis 6+

## 🚀 Quick Start

### Option 1: Using Docker Compose (Recommended)

```bash
# Clone repository
git clone https://github.com/palaieski-a11y/weather-dashboard.git
cd weather-dashboard

# Copy environment
cp .env.example .env

# Start all services
docker-compose up -d

# Access the API
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### Option 2: Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Add your OpenWeatherMap API key to .env

# Run development server
uvicorn app.main:app --reload

# Access API at http://localhost:8000
```

## 📚 API Documentation

### Interactive Docs
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Weather Endpoints

#### Get Current Weather
```http
GET /api/weather/current?city=London
```

**Response:**
```json
{
  "city": "London",
  "country": "GB",
  "temperature": 15.5,
  "feels_like": 14.2,
  "humidity": 72,
  "pressure": 1013,
  "description": "Partly cloudy",
  "icon": "02d",
  "wind_speed": 4.2,
  "wind_direction": 230,
  "cloudiness": 25,
  "uv_index": 3.5,
  "visibility": 10000,
  "sunrise": "2026-05-18T05:30:00Z",
  "sunset": "2026-05-18T20:45:00Z",
  "timestamp": "2026-05-18T12:00:00Z"
}
```

#### Get 5-Day Forecast
```http
GET /api/weather/forecast?city=London&days=5
```

**Response:**
```json
{
  "city": "London",
  "country": "GB",
  "forecast": [
    {
      "date": "2026-05-18",
      "temp_min": 12.0,
      "temp_max": 18.5,
      "description": "Partly cloudy",
      "precipitation": 0.0,
      "wind_speed": 4.2
    }
  ]
}
```

#### Search Locations
```http
GET /api/weather/search?query=Lond&limit=5
```

**Response:**
```json
{
  "results": [
    {
      "city": "London",
      "country": "GB",
      "latitude": 51.5074,
      "longitude": -0.1278,
      "population": 8900000
    }
  ]
}
```

#### Get Weather Alerts
```http
GET /api/weather/alerts?city=London
```

### Location Endpoints

#### Get Favorite Locations
```http
GET /api/locations/favorites
```

#### Add Favorite Location
```http
POST /api/locations/favorites
Content-Type: application/json

{
  "city": "London",
  "country": "GB",
  "latitude": 51.5074,
  "longitude": -0.1278
}
```

#### Remove Favorite Location
```http
DELETE /api/locations/favorites/{location_id}
```

#### Get Recent Searches
```http
GET /api/locations/recent
```

### Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "database": "connected",
  "cache": "connected",
  "external_api": "reachable"
}
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file (copy from `.env.example`):

```env
# API Configuration
OPENWEATHER_API_KEY=your_api_key_here
OPENWEATHER_BASE_URL=https://api.openweathermap.org/data/2.5

# Database
DATABASE_URL=postgresql://weather:password@db:5432/weather_db
DATABASE_POOL_SIZE=20
DATABASE_ECHO=false

# Redis
REDIS_URL=redis://cache:6379/0
REDIS_TTL=600

# Application
APP_ENV=development
DEBUG=true
LOG_LEVEL=INFO

# CORS
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080

# API Rate Limiting
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_PERIOD=3600
```

## 🏗️ Project Structure

```
weather-dashboard/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry point
│   ├── config.py               # Configuration management
│   ├── schemas.py              # Pydantic models
│   ├── services.py             # Business logic
│   ├── integrations.py         # OpenWeatherMap API client
│   ├── cache.py                # Redis client
│   ├── database.py             # SQLAlchemy setup
│   ├── models.py               # Database models
│   ├── middleware.py           # Custom middleware
│   └── routers/
│       ├── weather.py          # Weather endpoints
│       ├── locations.py        # Location endpoints
│       └── health.py           # Health checks
├── tests/
│   ├── test_weather.py
│   ├── test_locations.py
│   └── test_health.py
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container image
├── docker-compose.yml          # Multi-service orchestration
├── Makefile                    # Development commands
├── .env.example                # Environment template
└── README.md                   # This file
```

## 🛠️ Development

### Using Make Commands

```bash
# Show all available commands
make help

# Install dependencies
make install

# Run development server
make dev

# Run tests with coverage
make test

# Lint code
make lint

# Format code
make format

# Clean build artifacts
make clean

# Docker commands
make docker-build
make docker-up
make docker-down
make logs
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app --cov-report=html

# Run specific test
pytest tests/test_weather.py -v
```

### Code Quality

```bash
# Check code with Ruff
ruff check app/

# Type check with Mypy
mypy app/ --ignore-missing-imports

# Format with Black
black app/

# Sort imports with isort
isort app/
```

## 🐳 Docker

### Build Image
```bash
docker build -t weather-dashboard:latest .
```

### Run Container
```bash
docker run -p 8000:8000 \
  -e OPENWEATHER_API_KEY=your_key \
  weather-dashboard:latest
```

### Docker Compose
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f backend

# Stop services
docker-compose down

# Rebuild services
docker-compose up --build
```

## 📊 Database Schema

### Locations Table
```sql
CREATE TABLE locations (
  id SERIAL PRIMARY KEY,
  city VARCHAR(100) NOT NULL,
  country VARCHAR(2) NOT NULL,
  latitude FLOAT NOT NULL,
  longitude FLOAT NOT NULL,
  population INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Favorite Locations Table
```sql
CREATE TABLE favorite_locations (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  location_id INT NOT NULL REFERENCES locations(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(user_id, location_id)
);
```

### Weather Cache Table
```sql
CREATE TABLE weather_cache (
  id SERIAL PRIMARY KEY,
  location_id INT NOT NULL REFERENCES locations(id),
  weather_data JSONB NOT NULL,
  cached_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  expires_at TIMESTAMP NOT NULL
);
```

## 🔐 Security Considerations

- API keys stored in environment variables
- Input validation with Pydantic
- Rate limiting on endpoints
- CORS configuration
- SQL injection prevention with SQLAlchemy ORM
- Request/response logging
- Error message sanitization

## 📈 Performance

- **Caching**: 10-minute Redis cache for weather data
- **Async**: All I/O operations are async
- **Connection Pooling**: Database connection pooling configured
- **Response Times**: < 100ms for cached requests
- **Throughput**: 1000+ requests per minute

## 🐛 Troubleshooting

### Issue: API returns 401 Unauthorized
**Solution**: Verify your OpenWeatherMap API key in `.env`

### Issue: Database connection fails
**Solution**: Ensure PostgreSQL is running and DATABASE_URL is correct

### Issue: Redis connection error
**Solution**: Ensure Redis is running on the configured host:port

### Issue: Weather API rate limit exceeded
**Solution**: Upgrade to a paid OpenWeatherMap plan or implement request batching

## 📝 Logging

Logs are written to:
- **Console**: All log levels
- **File**: `logs/weather_dashboard.log`

Configure log level in `.env`:
```env
LOG_LEVEL=DEBUG  # DEBUG, INFO, WARNING, ERROR, CRITICAL
```

## 🚀 Deployment

### AWS EC2
```bash
# SSH into instance
ssh -i key.pem ubuntu@instance-ip

# Clone repo
git clone https://github.com/palaieski-a11y/weather-dashboard.git
cd weather-dashboard

# Run with Docker Compose
docker-compose up -d
```

### Heroku
```bash
# Login and create app
heroku login
heroku create weather-dashboard-api

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### DigitalOcean App Platform
1. Connect GitHub repository
2. Set environment variables
3. Deploy with auto-scaling

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 📧 Support

- 📖 [API Documentation](http://localhost:8000/docs)
- 🐛 [Issues](https://github.com/palaieski-a11y/weather-dashboard/issues)
- 💬 [Discussions](https://github.com/palaieski-a11y/weather-dashboard/discussions)

## 🎯 Roadmap

- [ ] Real-time WebSocket updates
- [ ] Weather notifications
- [ ] Historical weather data
- [ ] Weather patterns analysis
- [ ] Mobile app integration
- [ ] GraphQL API
- [ ] Multi-language support
- [ ] Advanced analytics dashboard

## 👨‍💻 Authors

- **Eski Palai** - Initial development

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) - Weather data API
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
- [Pydantic](https://pydantic-ai.jina.ai/) - Data validation
