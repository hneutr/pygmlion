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

def check_identity(test_in_file):
    actual = get_test_output(parser.get_raw_gml(test_in_file))
    expected = read_file(test_in_file)

    assert actual == expected

def check_transform(test):
    actual = get_test_output(parser.get_gml(test['in']))
    expected = read_file(test['out'])

    assert actual == expected

def run_test(test_name):
    test = get_test_files(test_name)

    check_identity(test['in'])

    if test.get('out'):
        check_transform(test)

def test_ex_1():
    run_test('1')

def test_ex_2():
    run_test('2')

def test_ex_3():
    run_test('3')
