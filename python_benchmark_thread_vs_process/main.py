# -*- coding: utf-8 -*-
import sys
import psutil
import time
import multiprocessing
from .multi_thread import MultiThread
from .multi_process import MultiProcess

from . import TableIt


def is_number(s):
    """
    Check whether string is number
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def run(nops=None):
    out_table = []

    args = sys.argv[1:]

    ncpus = multiprocessing.cpu_count()
    num_op = ncpus * 10

    if len(args) >= 1:
        if is_number(s=args[0]):
            num_op = int(args[0])
        else:
            print(
                """USAGE: $ python_benchmark_thread_vs_process <NUM_OPERATIONS> (default: NUM_OPERATIONS=NCPUS*10=%d)
Eg. $ python_benchmark_thread_vs_process 10"""
                % num_op
            )
            return

    if nops is not None:
        num_op = nops

    out_table.append(
        [
            "Num CPUs",
            "CPU Freq (MHz)",
            "Multi-Thread Time (s)",
            "Multi-Process Time (s)",
            "Num Test Operation",
        ]
    )

    out_table.append([str(ncpus)])

    current_cpu_feq = round(psutil.cpu_freq().current)
    out_table[1].append("%.0f" % current_cpu_feq)

    print(
        "Benchmarking (%d CPUs @ %s) ... please wait..."
        % (int(ncpus), "%.0fMHz" % current_cpu_feq)
    )

    # multi-thread benchmarking
    tstart = time.time()
    mthread = MultiThread(num_thread=ncpus, num_op=num_op)
    mthread()
    tend = time.time()
    tdelta = tend - tstart  # seconds
    out_table[1].append("%.4f" % tdelta)

    time.sleep(1)  # sleep 1 second

    # multi-process benchmarking
    tstart = time.time()
    mprocess = MultiProcess(num_process=ncpus, num_op=num_op)
    mprocess()
    tend = time.time()
    tdelta = tend - tstart  # seconds
    out_table[1].append("%.4f" % tdelta)

    out_table[1].append(str(num_op))

    benchmark_result_banner = [
        "====================",
        "| BENCHMARK RESULT |",
        "====================",
    ]
    print("\n".join(benchmark_result_banner))
    TableIt.printTable(out_table, useFieldNames=True, color=(26, 156, 171))
    pass


if __name__ == "__main__":
    run()
