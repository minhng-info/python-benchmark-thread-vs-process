<img src='https://img.shields.io/pypi/l/python_benchmark_thread_vs_process.svg'> <img src='https://img.shields.io/pypi/pyversions/python_benchmark_thread_vs_process.svg'> <img src='https://img.shields.io/pypi/v/python_benchmark_thread_vs_process.svg'> <img src='https://img.shields.io/pypi/dm/python_benchmark_thread_vs_process.svg'> <img src='https://img.shields.io/badge/code%20style-black-000000.svg'>

# python-benchmark-thread-vs-process
A benchmark on speed evaluation between multi-thread and multi-process in Python

* PyPI: [https://pypi.org/project/python-benchmark-thread-vs-process/](https://pypi.org/project/python-benchmark-thread-vs-process/)
* Github: [https://github.com/minhng-info/python-benchmark-thread-vs-process](https://github.com/minhng-info/python-benchmark-thread-vs-process)

# Installation

```
$ sudo pip3 install python_benchmark_thread_vs_process
```

Note: this package only supports Python 3.

Install package and run test in one command:

```
$ sudo pip3 install python_benchmark_thread_vs_process && python_benchmark_thread_vs_process
```

# Usage

Run benchmarking with the following command:

```
$ python_benchmark_thread_vs_process
```

Note: It takes up to 15 minutes to finish the test. Please be patient!

# Benchmarking Results

Try to keep your CPUs usage free as much as possible before benchmarking.

For latest benchmarking result, please checkout @ [https://github.com/minhng-info/python-benchmark-thread-vs-process](https://github.com/minhng-info/python-benchmark-thread-vs-process)

| Num CPUs | CPU Model | Current CPU Freq (MHz) | Multi-Thread Time (s) | Multi-Process Time (s) | Total Test Operation | Contributor |
|---|---|---|---|---|---|---|
| 1        | Intel(R) Xeon(R) CPU E5-2680 v3 @ 2.50GHz | 2500                   | 11.7581               | 12.0673                | 100                  | @minhng92 |
| 4        | Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz | 2474                   | 55.3840               | 8.8589                 | 400                  | @minhng92 |
| 4        | Intel(R) Core(TM) i7-6500U CPU @ 2.50GHz | 2683                   | 20.9098               | 10.9195                | 400                  | @minhng92 |
| 16       | Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHz | 2597                   | 98.6584               | 7.1033                 | 1600                 | @minhng92 |
| 24       | Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz | 1331                   | 372.3926              | 18.5923                | 2400                 | @minhng92 |
| 32       | Intel(R) Xeon(R) Silver 4108 CPU @ 1.80GHz | 809                    | 478.8115              | 15.0538                | 3200                 | @minhng92 |
| 72       | Intel(R) Xeon(R) Gold 5220S CPU @ 2.70GHz | 1016                   | 550.4936              | 11.6759                | 7200                 | @minhng92 |

# Contributing

## Benchmarking

To contribute to our benchmark table, please follow these steps:

* Step 1: Install package: `pip install python-benchmark-thread-vs-process`
* Step 2: Run benchmarking on your machine / server with the command: `python_benchmark_thread_vs_process`
* Step 3: If your system information has not been included in the benchmarking results, please create a new issue ticket (with `enhancement` label) and submit your benchmarking result. Your submission is welcome!
* Step 4: We'll review and update the benchmarking results.

## Code development

* Step 1. Fork on **master** branch.
* Step 2. Install **pre-commit** on the local dev environment.

```
pip install pre-commit
pre-commit install

```

* Step 3. Write unit-test (if any).
* Step 4. Write code to pass the tests.
* Step 5. Make sure that the new code passes all the pre-commmit conditions.

```
sh pre_commit.sh

```

* Step 6. Create pull request.
