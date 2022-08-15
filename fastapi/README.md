# setup

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

# start local server

```
$ uvicorn main:app --reload
```

# run load test for local server

```
$ locust
```

# deploy to cloud run

```
$ gcloud run deploy
```

# run load test for cloud run service

```
$ locust -f locustfile_for_cloud_run.py 
```

