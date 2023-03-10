# Sample python monolith application

## Tech Stack
- Flask
- Python 3.7.16

## Build Instructions

```
git clone git@github.com:tarunsaxenattn/sample-python-monolith-app.git
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
