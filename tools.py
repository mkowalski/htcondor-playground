#!/usr/bin/python3

__author__ = "Mateusz Kowalski"
__email__ = "mateusz.kowalski@cern.ch"
__status__ = "Development"

import multiprocessing
from subprocess import call
from time import gmtime, strftime, sleep


def time_me(func):
    def timed(*args, **kwargs):
        print("\n"+strftime("%Y-%m-%d %H:%M:%S", gmtime()), ">> start <<", func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()), ">> end <<", func.__name__, args, kwargs, '\n')

        return result
    return timed


def report_result(func):
    def proxy(*args, **kwargs):
        r = func(*args, **kwargs)
        print(r)
        return r
    return proxy


def handle_error(func):
    def handle_problems(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
    return handle_problems


@handle_error
@report_result
@time_me
def read_from_file(path):
    file = open(path, 'r')
    return file


@handle_error
@time_me
def write_to_file(path):
    file = open(path, 'w')
    file.write("Hello\nIt's me again\n")


@handle_error
@time_me
def run_application(app, args):
    call([app, args])


@handle_error
@time_me
def do_nothing(time):
    sleep(time)


@handle_error
@time_me
def do_heavy_computation(time):
    def foo(x):
        while True:
            x * x

    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    p.start()
    sleep(time)
    p.terminate()
    p.join()
