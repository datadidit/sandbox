# Word Count Apache Beam example

* Packaging from scratch to make sure I understand how to package.

## Running Package

1. [Ensure you've setup your environment to work with Google Cloud Runner](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-pythons)
2. cd into wordcount package `cd <workspace>/sandbox/python/apache_bean/wordcount`
2. `pip install -r requirements.txt`
3. Run the below command:
```bash
python wordcount_main.py --input gs://dataflow-samples/shakespeare/kinglear.txt \
                         --output gs://cloud-data-flow-test/results/output \
                         --runner DataflowRunner \
                         --project <project_name> \
                         --setup_file <fullpath to file>/setup.py \
                         --temp_location gs://cloud-data-flow-test/tmp_sandbox/output
```

## [How to query MySQL from Python pipeline](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/)

Had trouble querying MySQL from my pipeline and found a ton of examples for JDBC but not for Python. In order to do it
with Python you need to use:

* pymysql (For the directrunner and likely others you can use `mysql-python`/`mysqlclient` but I had trouble getting MySQLDb
to run in [DataFlowRunner](https://stackoverflow.com/questions/56202734/python-mysql-in-cloud-dataflowrunner/56206596#56206596))
* SQLAlchemy your url would start with `mysql+pymysql`
```
REQUIRED_PACKAGES = [
    "pymysql",
    "sqlalchemy",
    "redis",
    "matplotlib"
]
```
* Depending on your MySQL instance you may need to setup an SQLProxy in order to communicate from
the machines the DataFlowRunner starts up.



## Trouble Shooting

* I needed to set my PYTHONPATH to:

```bash
export PYTHONPATH=/Users/mkwyche/workspace/python/sandbox/python/apache_beam/wordcount
```

For it to work.