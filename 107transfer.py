#!/usr/bin/python3
import sys
import math
import os
import random

def     display_man():
    print("USAGE")
    print("    ./107transfer [num den]*")
    print("DESCRIPTION")
    print("    num    polynomial numerator defined by its coeficients")
    print("    den    polynomial denominator defined by its coeficients")

def     valid_string(string):
    i = 0
    while (i < len(string)):
        if (string[i] < '.' and string[i] > '/'
            and string[i] < '0' or string[i] > '9'):
            sys.stdout.write("Invalid argument: must be a number.\n")
            exit(84)

if (len(sys.argv) >= 2 and (len(sys.argv) - 1) % 2 == 0):
    if (sys.argv[1] == "-h"):
        display_man()
        exit(0)
    a = 1
    x = 0.0
    function = 1.0
    while (x < 1.001):
        for a in range (1, ((len(sys.argv) - 1)), 2):
            try:
                num = [int(s) for s in sys.argv[a].split('*')]
                den = [int(s) for s in sys.argv[a + 1].split('*')]
            except ValueError:
                sys.stdout.write("Invalid argument: must be a number.\n");
                exit(84)
            if ((sum(den[i] * x ** i for i in range(len(den))) == 0)):
                sys.stdout.write("Division by zero.\n");
                exit(84)
            function = function * (sum(num[i] * x ** i for i in range(len(num))) / sum(den[i] * x ** i for i in range(len(den))))
            a = a + 2
        if (round(x, 3) == int(x)):
            print('{:.3f} -> {:.5f}'.format(int(x), function))
        else:
            print('{:.3f} -> {:.5f}'.format(round(x, 3), function))
        x += 0.001
        a = 1
        function = 1.0   
elif (len(sys.argv) == 0):
		print("Usage: ./107tranfert <num> <den>")
		exit(84)
elif (len(sys.argv) % 2 != 0):
		print("Usage: ./107tranfert <num> <den>")
		exit(84)
else:
		print("Usage: ./107tranfert <num> <den>")
		exit(84)