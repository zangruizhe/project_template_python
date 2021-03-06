#!/usr/local/bin/python2.7
# -*- coding: UTF-8 -*-

# create logger
#----------------------------------------------------------------------
import logging

log = logging.getLogger('python_logger')
log.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 2015-08-28 17:01:57,662 - simple_example - ERROR - error message

# formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s:%(lineno)-4d: %(message)s')
formatter = logging.Formatter('%(asctime)s %(levelname)-2s [%(filename)s: %(lineno)d] %(message)s')


fh = logging.FileHandler('python_project_template.log', 'w')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(fh)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(ch)
#----------------------------------------------------------------------

log.info("test log")
log.error("test error")

