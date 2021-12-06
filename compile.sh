cc test.c -fPIC -shared -o testlib.so
cc gaussian_blur.c -O3 -fPIC -shared -o gausslib.so
