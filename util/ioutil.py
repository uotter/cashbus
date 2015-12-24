# -*-coding:UTF-8-*-
import time
import random

__author__ = 'M'

f_test_x = open("..//data//test_x.csv")
f_train_x = open("..//data//train_x.csv")
f_train_y = open("..//data//train_y.csv")
f_feature = open("..//data//features_type.csv")


def read_train_test():
    start = time.time()
    f_train_x_lines = f_train_x.readlines()
    f_train_y_lines = f_train_y.readlines()
    end = time.time()
    print 'read train file fininshed with: ' + str(end - start)
    start = time.time()
    f_test_x_lines = f_test_x.readlines()
    end = time.time()
    print 'read test file fininshed with: ' + str(end - start)
    return f_train_x_lines,f_train_y_lines, f_test_x_lines


