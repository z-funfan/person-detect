# -*- encoding:utf-8 -*-
import logging
import os.path
import time

logger_inited = False


def init_logger():
    # create logger
    logger_name = "main"
    mlogger = logging.getLogger(logger_name)
    mlogger.setLevel(logging.DEBUG)

    # console handler
    console = logging.StreamHandler()

    # create file handler
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd())
    log_name = log_path + rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.INFO)

    # create formatter
    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    # add handler and formatter to logger
    fh.setFormatter(formatter)
    mlogger.addHandler(console)  # -*- encoding:utf-8 -*-
    mlogger.addHandler(fh)  # -*- encoding:utf-8 -*-


def logger(name = "main"):
    global logger_inited
    if not logger_inited:
        init_logger()
    return logging.getLogger(name)
