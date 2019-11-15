# UWSGI Sandbox

Putting all simple examples for using uwsgi in here. Good reference for more complex projects.

## Commands

* Run Flask no uwsgi

```bash
python app.py
```

* Run uwsgi referencing virtualenv

```bash
PYTHONPATH=${PATH TO this dir} uwsgi -H ${PATH To virtualenv} --ini uwsgi.ini
```

## Docker

Inspiration from this docker image comes from this [medium post](https://medium.com/@smirnov.am/running-flask-in-production-with-docker-1932c88f14d0)

Build image using this command:

```
docker build -t datadidit/uwsgi .
```

Run Image:

```
docker run -it datadidit/uwsgi
```

To verify websockets are working go to [http://localhost:8080](http://localhost:8080) you will
see network connections to the socketio endpoint were successful.

## Troubleshooting

* IOError: unable to complete websocket handshake while running in uwsgi?

This is happening because `uwsgi` was not installed with [ssl](https://stackoverflow.com/a/38842664) support. To ensure it's installed with ssl support
run this command:

```bash
CFLAGS="-I/usr/local/opt/openssl/include" LDFLAGS="-L/usr/local/opt/openssl/lib" UWSGI_PROFILE_OVERRIDE=ssl=true pip install uwsgi -Iv --no-cache-dir
```
