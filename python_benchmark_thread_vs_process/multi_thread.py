# -*- coding: utf-8 -*-
import threading
from .operation import run_operation


class MultiThread(object):
    def __init__(self, num_thread=4, num_op=100):
        self.num_thread = num_thread
        self.num_op = num_op
        assert self.num_thread > 0
        assert self.num_op > 0
        pass

    def __call__(self):
        thread_list = []
        for _ in range(self.num_thread):
            t = threading.Thread(target=run_operation, args=(self.num_op,))
            t.start()
            thread_list.append(t)

        for _ in range(len(thread_list)):
            t = thread_list[_]
            t.join()

        pass
