"""
------------------------------------------
@File       : __init__.py
@CreatedOn  : 2023/12/27
------------------------------------------
"""
from os.path import dirname, join as path_join

from utils.log import Logger


def gen_log_dir() -> str:
    """生成log文件夹路径相对路径"""
    project_dir = dirname(dirname(__file__))

    return path_join(project_dir, "log")


log = Logger(log_dir=gen_log_dir(), filename='batch_decompression_tool').log
