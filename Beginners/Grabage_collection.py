#!/usr/bin/python3
import gc
for number in range(0, 20, 2):
    print (number, "Here")
    del number
    gc.collect()