from __future__ import absolute_import

import logging

from wordcount.wordcount import run


if __name__ == '__main__':
  '''
  To run issue a command:
  python wordcount_main.py --input gs://dataflow-samples/shakespeare/kinglear.txt \
                         --output gs://cloud-data-flow-test/results/output \
                         --runner DataflowRunner \
                         --project <project_name> \
                         --setup_file <fullpath to file>/setup.py \
                         --temp_location gs://cloud-data-flow-test/tmp_sandbox/output
  '''
  logging.getLogger().setLevel(logging.INFO)
  run()