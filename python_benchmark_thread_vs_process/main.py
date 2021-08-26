# -*- coding: utf-8 -*-
import sys
import psutil
import time
import multiprocessing
from .multi_thread import MultiThread
from .multi_process import MultiProcess

# https://github.com/Robpol86/terminaltables
from terminaltables import AsciiTable
from . import cpuinfo


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
    num_op = 100

    if len(args) >= 1:
        if is_number(s=args[0]):
            num_op = int(args[0])
        else:
            print(
                """USAGE: $ python_benchmark_thread_vs_process <NUM_OPERATIONS_PER_CHILD> (default: NUM_OPERATIONS_PER_CHILD=%d)
Eg. $ python_benchmark_thread_vs_process 10"""
                % num_op
            )
            return

    if nops is not None:
        num_op = nops

    out_table.append(
        [
            "Num CPUs",
            "CPU Model",
            "Current CPU Freq (MHz)",
            "Multi-Thread Time (s)",
            "Multi-Process Time (s)",
            "Total Test Operation",
        ]
    )

    out_table.append([str(ncpus)])

    cpu_info = psutil.cpu_freq()
    current_cpu_freq = round(cpu_info.current)
    try:
        out_table[1].append(cpuinfo.cpu.info[0]["model name"])
    except Exception:
        out_table[1].append("N/A")
    out_table[1].append("%.0f" % current_cpu_freq)

    print(
        "Benchmarking (%d CPUs @ %s) ... please wait..."
        % (int(ncpus), "%.0fMHz" % current_cpu_freq)
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

    out_table[1].append(str(ncpus * num_op))

    benchmark_result_banner = [
        "====================",
        "| BENCHMARK RESULT |",
        "====================",
    ]
    print("\n".join(benchmark_result_banner))
    print(AsciiTable(out_table).table)
    pass


if __name__ == "__main__":
    run()
