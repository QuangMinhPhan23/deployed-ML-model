# Personality Prediction API

A machine learning model API for predicting personality type (Extrovert/Introvert).

## Docker Instructions

### Building the Container
```
docker build -t deployed_ml .
```

### Running the Container
```
docker run -p 8888:8888 deployed_ml
```

### Accessing the API
When running with Docker, access the API at:
```
http://localhost:8888
```

⚠️ **IMPORTANT:** 
- Do NOT try to use http://0.0.0.0:8888 in your browser
- The 0.0.0.0 address shown in Docker logs is only for internal container configuration
- Always use localhost:8888 instead

## API Endpoints

- `/` - Welcome page
- `/docs` - Interactive Swagger documentation
- `/predict` - Make personality predictions (POST)
- `/health` - Health check endpoint

## Example Usage

Using curl:
```
curl -X POST "http://localhost:8888/predict" -H "Content-Type: application/json" -d "{\"features\":[1,0,1,0,1,0,1]}"
```

Or visit http://localhost:8888/docs for interactive API testing.
