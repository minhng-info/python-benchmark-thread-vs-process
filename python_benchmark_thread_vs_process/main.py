# -*- coding: utf-8 -*-
import sys
import psutil
import time
import multiprocessing
from .multi_thread import MultiThread
from .multi_process import MultiProcess


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
    csv_result = [
        "====================",
        "| BENCHMARK RESULT |",
        "====================",
        ",".join(
            [
                "Num CPUs",
                "CPU Freq (MHz)",
                "Multi-Thread Time (s)",
                "Multi-Process Time (s)",
                "Num Test Operation",
            ]
        ),
    ]
    line = []

    args = sys.argv[1:]
    num_op = 100
    if len(args) >= 1:
        if is_number(s=args[0]):
            num_op = int(args[0])
        else:
            print(
                """USAGE: $ python_benchmark_thread_vs_process <NUM_OPERATIONS> (default: NUM_OPERATIONS=100)
Eg. $ python_benchmark_thread_vs_process 10"""
            )
            return

    if nops is not None:
        num_op = nops

    ncpus = multiprocessing.cpu_count()
    line.append(str(ncpus))

    current_cpu_feq = round(psutil.cpu_freq().current)
    line.append("%.0f" % current_cpu_feq)

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
    line.append("%.4f" % tdelta)

    time.sleep(1)  # sleep 1 second

    # multi-process benchmarking
    tstart = time.time()
    mprocess = MultiProcess(num_process=ncpus, num_op=num_op)
    mprocess()
    tend = time.time()
    tdelta = tend - tstart  # seconds
    line.append("%.4f" % tdelta)

    line.append(str(num_op))
    csv_result.append(",".join(line))
    csv_result.append("--------------------")

    print("\n".join(csv_result))
    pass


if __name__ == "__main__":
    run()
