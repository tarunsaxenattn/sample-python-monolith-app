# Sample python monolith application

## Tech Stack
- Flask
- Python 3.7.16

## Build Instructions

```
git clone git@github.com:tarunsaxenattn/sample-python-monolith-app.git
cd sample-python-monolith-app
docker build . -t sample-python-monolith-app -f docker/Dockerfile
```

## Run App locally

```
docker run -itd --name sample-python-monolith-app -p 5000:5000 sample-python-monolith-app
```

## Destroy
```
docker rm -f sample-python-monolith-app
```

## APIs

### GET /ui => UI service
```
curl localhost:5000/ui
UI Service is healthy
```

### GET /payment => Payment service
```
curl localhost:5000/payment
Payment Service is healthy
```

### GET /login => Login service
```
curl localhost:5000/login
Login Service is healthy
```

### GET /health => healthcheck service
```
curl localhost:5000/health
app is healthy
```
