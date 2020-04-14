# -*- coding: utf-8 -*-
from python_benchmark_thread_vs_process import MultiProcess


def test_thread():
    mprocess = MultiProcess(num_process=4, num_op=1)
    try:
        mprocess()
    except Exception as e:
        print(e)
        assert False
    assert True
