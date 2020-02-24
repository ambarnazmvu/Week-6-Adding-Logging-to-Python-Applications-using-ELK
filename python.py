import logging
import logstash
import sys
import time

#host = 'localhost'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.DEBUG)
test_logger.addHandler(logstash.TCPLogstashHandler('34.204.89.19', 5010, version=1))
# 34.204.89.19
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

test_logger.error('somthing.')


#test_logger.info('python-logstash: test logstash info message.')
#test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
# extra = {
#     'test_string': 'python version: ' + repr(sys.version_info),
#     'test_boolean': True,
#     'test_dict': {'a': 1, 'b': 'c'},
#     'test_float': 2.21545,
#     'test_integer': 126,
#     'test_list': [1, 2, '3'],
# }
# test_logger.info('python-logstash: test extra fields', extra=extra)