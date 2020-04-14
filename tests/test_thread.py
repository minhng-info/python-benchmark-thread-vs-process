# -*- coding: utf-8 -*-
from python_benchmark_thread_vs_process import MultiThread


def test_thread():
    mthread = MultiThread(num_thread=4, num_op=1)
    try:
        mthread()
    except Exception as e:
        print(e)
        assert False
    assert True
