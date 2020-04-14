# -*- coding: utf-8 -*-
import python_benchmark_thread_vs_process


def test_main_run():
    try:
        python_benchmark_thread_vs_process.run(nops=1)
    except Exception as e:
        print(e)
        assert False
    assert True
