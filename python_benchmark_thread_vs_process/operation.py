# -*- coding: utf-8 -*-
import random


def run_operation(
    num_op, matrix_size=128, kernel_size=3, float_from=-1.0, float_to=1.0
):
    for _ in range(num_op):
        op = Operation(matrix_size, kernel_size, float_from, float_to)
        op()
    pass


class Operation(object):
    def __init__(self, matrix_size=128, kernel_size=3, float_from=-1.0, float_to=1.0):
        self.matrix_size = matrix_size
        self.kernel_size = kernel_size
        self.float_from = float_from
        self.float_to = float_to

        assert self.matrix_size >= 3
        assert self.kernel_size >= 3
        assert self.matrix_size >= self.kernel_size
        pass

    def _init_matrix(self, size):
        matrix = []
        for r in range(size):
            one_row = []
            for c in range(size):
                one_row.append(random.uniform(self.float_from, self.float_to))
            matrix.append(one_row)
        return matrix

    def __call__(self):
        self.matrix = self._init_matrix(size=self.matrix_size)
        self.kernel = self._init_matrix(size=self.kernel_size)

        nloop = self.matrix_size - self.kernel_size + 1
        self.result = self._init_matrix(size=nloop)
        for my in range(nloop):
            for mx in range(nloop):
                for ky in range(self.kernel_size):
                    for kx in range(self.kernel_size):
                        kernel_val = self.kernel[ky][kx]
                        matrix_val = self.matrix[my + ky][mx + kx]
                        self.result[my][mx] = matrix_val * kernel_val
        return True
