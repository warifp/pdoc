from functools import lru_cache


##### Testing a class attribute that is a lambda (which generates quirky sources)

class LambdaAttr:
    # not really supported, but also shouldn't crash.
    attr = lambda x: 42  # noqa


##### Testing different docstring annotations
# fmt: off


def foo():
    """no indents"""


def bar():
    """no
indents"""


def baz():
    """one
    indent"""


def qux():
    """
    two
    indents
    """


class Indented:
    def foo(self):
        """no indents"""

    def bar(self):
        """no
indents"""

    def baz(self):
        """one
        indent"""

    def qux(self):
        """
        two
        indents
        """

    @lru_cache
    def foo_decorated(self):
        """no indents"""

    @lru_cache
    # comment
    def foo_commented(self):
        """no indents"""

    @lru_cache
    def bar_decorated(self):
        """no
indents"""

    @lru_cache
    def baz_decorated(self):
        """one
        indent"""

    @lru_cache
    def qux_decorated(self):
        """
        two
        indents
        """