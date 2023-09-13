# Data Pipeline for Cocktails

## How to run

If using docker:

```shell
docker build -t pipeline_app .
docker run -v "$(pwd)/data:/app/data" -it pipeline_app
```

Else:

```shell
python ./etl/run.py
```

## ToDo
1. Pass in configuration as command line argument instead of contained within code. Update code to work with yaml instead.
2. Update configuration paths relevant for deployment environment
3. Unit and integration tests
4. Replace sqllite with postgres prod database

