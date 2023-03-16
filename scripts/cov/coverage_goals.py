from coverage import Coverage

from scripts.cov.test_sum import test_sum


source = '/Users/chillaranand/projects/avilpage.com/scripts/cov/sum.py'

coverage = Coverage()
# coverage = Coverage(source=source, data_file=None)

coverage.start()

test_sum()

coverage.stop()
coverage.report()
