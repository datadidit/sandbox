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

## Trouble Shooting

* I needed to set my PYTHONPATH to:

```bash
export PYTHONPATH=/Users/mkwyche/workspace/python/sandbox/python/apache_beam/wordcount
```

For it to work.