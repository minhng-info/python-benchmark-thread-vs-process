# -*- coding: utf-8 -*-
import python_benchmark_thread_vs_process


def test_operation():
    op = python_benchmark_thread_vs_process.Operation(
        matrix_size=5, kernel_size=3, float_from=-1.0, float_to=1.0
    )
    result = op()
    assert result is True
