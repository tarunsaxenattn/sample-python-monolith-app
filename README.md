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

## Run App locally for monolith app for internal healthcheck

```
docker run -itd -e healthcheckhost=127.0.0.1 --name sample-python-monolith-app -p 80:80 sample-python-monolith-app
```

## Run App in microservices mode for external healthcheck

```
docker run -itd -e healthcheckhost=<APIHOST> --name sample-python-monolith-app -p 80:80 sample-python-monolith-app
```

> The environment variable is mandatory to pass for healthcheck to work. Intentionally this is not made default variable


## APIs

### GET / => UI service
```
curl localhost/ui
UI
```

### GET /payment => Payment service
```
curl localhost/payment
Payment page
```

### GET /login => Login service
```
curl localhost/login
Login page
```

### GET /healthcheck => healthcheck service
```
curl localhost/healthcheck   (For 127.0.0.1)

{"hostname": "66bac320fd75", "status": "success", "timestamp": 1678819024.6349406, "results": [{"checker": "login_available", "output": "Login up @@ ", "passed": true, "timestamp": 1678819024.631133, "expires": 1678819051.631133}, {"checker": "payment_available", "output": "Payment up @@ ", "passed": true, "timestamp": 1678819024.6346788, "expires": 1678819051.6346788}]}
```


## Run with Publically available image

Full monolith app
```
docker run -itd -e healthcheckhost=127.0.0.1 --name sample-python-monolith-app -p 80:80 tarunttnd/sample-python-monolith-app
```


Only UI app (to simulate failure and let UI healthcheck hit APIHOST URL running on different host)
```
docker run -itd -e healthcheckhost=<APIHOST> --name sample-python-monolith-app -p 80:80 tarunttnd/sample-python-monolith-app:ui
```



## Destroy
```
docker rm -f sample-python-monolith-app
```
