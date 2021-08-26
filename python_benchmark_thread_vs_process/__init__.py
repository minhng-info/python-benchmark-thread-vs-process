# -*- coding: utf-8 -*-
from .main import run
from .operation import Operation
from .multi_thread import MultiThread
from .multi_process import MultiProcess

__version__ = "0.1.5"
__all__ = [
    "run",
    "Operation",
    "MultiThread",
    "MultiProcess",
]
