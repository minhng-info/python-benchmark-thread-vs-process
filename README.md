<img src='https://img.shields.io/pypi/l/python_benchmark_thread_vs_process.svg'> <img src='https://img.shields.io/pypi/pyversions/python_benchmark_thread_vs_process.svg'> <img src='https://img.shields.io/pypi/v/python_benchmark_thread_vs_process.svg'> <img src='https://img.shields.io/pypi/dm/python_benchmark_thread_vs_process.svg'> <img src='https://img.shields.io/badge/code%20style-black-000000.svg'>

# python-benchmark-thread-vs-process
A benchmark on speed evaluation between multi-thread and multi-process in Python

# Installation

```
$ pip install python_benchmark_thread_vs_process
```

# Usage

Run benchmarking with the following command:

```
$ python_benchmark_thread_vs_process
```

# Benchmarking Results

| Num CPUs               | CPU Freq (MHz)         | Multi-Thread Time (s)  | Multi-Process Time (s) | Num Test Operation     |
|------------------------|------------------------|------------------------|------------------------|------------------------|
| 1                      | 2500                   | 1.2260                 | 1.2269                 | 10                     |

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
