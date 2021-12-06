import ctypes
import numpy as np

n=27
A = np.arange(n, dtype='float32')
B = np.arange(n, dtype='float32')
C = np.zeros(n, dtype='float32')

A = A.reshape(3,3,3)
B = B.reshape(3,3,3)
C = C.reshape(3,3,3)

print(A)

testlib = ctypes.CDLL('/home/aki/ADHDSimulator/testlib.so')
testlib.compute_mean.restype = ctypes.c_void_p

mean = testlib.compute_mean(ctypes.c_void_p(A.ctypes.data),ctypes.c_void_p(B.ctypes.data),ctypes.c_void_p(C.ctypes.data), ctypes.c_int(A.size))
# mean = np.frombuffer(testlib.compute_mean(A.ctypes.data, A.size)).copy()
print(C)
