"""
Functional test for Python checker.
"""

import os, ast

import pytest
from testsupport import *

from snakefood.checker import *
from snakefood.find import ImportVisitor


def visit_source(source, cls):
    astree = ast.parse(source)
    visitor = cls()
    visitor.visit(astree)
    return visitor.finalize()


# @pytest.mark.parametrize(
#     'source,expected',
#     (
#         ('import mymod', ['mymod']),
#         ('import mod1, mod2, mod3', ['mod1', 'mod2','mod3']),
#         ('import mod1 as mymod', ['mymod']),
#         ('import mod1 as mymod, mod2 as mymod2', ['mymod', 'mymod2']),
#         ('from mod1 import mymod', ['mymod']),
#         ('from mod1 import mymod, mymod2', ['mymod', 'mymod2']),
#         ('from mod1 import mymod as bli1', ['bli1']),
#         ('from mod1 import mymod as bli1, mymod2 as bli2', ['bli1', 'bli2']),
#         ('import os.path', ['os.path']),
#     )
# )
# def test_checker_functional_imports(source, expected):
#     found = visit_source(source, ImportVisitor)
#     actual = [x[2] for x in found if x[2] is not None]
#     assert actual == expected, (actual, expected)


@pytest.mark.parametrize(
    'source,expected',
    (
      ('a = 1; print(b.c); d.e = 3', ['b', 'b.c', 'd']),
      ('fn = os.path.join("a", "b")', ['os', 'os.path', 'os.path.join']),
    )
)
def test_checker_functional_names(source, expected):
    dotted, simple = visit_source(source, NamesVisitor)
    actual = [x[0] for x in dotted]
    assert actual == expected, (actual, expected)


# def test_checker_expected():
#     checkdir = os.path.join(data, 'checker')
#     pytocheck = [os.path.join(checkdir, fn) for fn in os.listdir(checkdir) if fn.endswith('.py')]
#     for fn in pytocheck:
#         print('Testing checker on: %s' % fn)
#         compare_expect(None, fn.replace('.py', '.expect'), 'sfood-checker', fn, filterdir=(data, 'ROOT'))

