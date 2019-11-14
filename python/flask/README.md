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