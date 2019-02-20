import parser
import os
from collections import defaultdict

def get_test_files(test_name):
    _dir = os.path.join(os.getcwd(), 'test_graphs')

    test = {}
    for file in os.listdir(_dir):
        full_file = os.path.join(_dir, file)
        only_name = os.path.splitext(file)[0]

        info = only_name.split('_')

        if len(info) < 2:
            continue

        name = info.pop(0)

        if name == test_name:
            kind = info.pop(0)
            test[kind] = full_file

    return test

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def get_test_output(test_input):
    tempfile = '__test_file__.gml'
    parser.write_gml(test_input, tempfile)
    test_output = read_file(tempfile)
    os.unlink(tempfile)

    return test_output

def verify_identity(test):
    actual = get_test_output(parser.get_raw_gml(test['in']))
    expected = read_file(test['in'])

    assert actual == expected

def verify_transform(test):
    actual = get_test_output(parser.get_gml(test['in']))
    expected = read_file(test['out'])

    assert actual == expected

def test_ex_1():
    test = get_test_files('1')
    verify_identity(test)
    verify_transform(test)

def test_ex_2():
    test = get_test_files('2')
    verify_identity(test)
    verify_transform(test)

def test_ex_3():
    test = get_test_files('3')
    verify_identity(test)
