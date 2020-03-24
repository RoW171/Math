#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-24"
__version__ = "0.0.0"

__all__ = ('DegreeSequence',)


class DegreeSequence(tuple):
    def __new__(cls, *sequence) -> 'DegreeSequence':
        return tuple.__new__(DegreeSequence, sequence)

    @property
    def vertecies(self) -> int:
        return len(self)

    @property
    def edges(self) -> int:
        return sum(self) // 2  # divide by 2 since we count twice

    @property
    def is_realizable(self) -> bool:
        """based on Havel-Hakimi, see below"""
        return self.havel_hakimi(*self)

    def havel_hakimi(self, *sequence) -> bool:
        # TODO write docstring here
        """"""
        sequence = sorted(sequence)
        if sequence[0] < 0: return False
        for i in range(sequence.pop()): sequence[-1 - i] -= 1
        for item in sequence:
            if item != 0: return self.havel_hakimi(*sequence)
        return True

    @property
    def is_tree(self) -> bool:
        """|E| = |V| - 1"""
        return self.vertecies - 1 == self.edges

    @property
    def has_hamilton(self) -> bool:
        """
        1.: |E| >= 3
        2.: {v ∈ V : deg(v) >= (|E| / 2)}
        """
        return self.vertecies >= 3 and all(v >= self.edges for v in self)

    @property
    def has_euler(self) -> bool:
        """number of vertecies with odd degree is even"""
        return len(tuple(i for i in self if i % 2 != 0)) % 2 == 0

    @property
    def is_planar(self) -> bool:
        # TODO write docstring here
        """"""
        if self.vertecies < 3: return True
        return self.edges <= 3 * self.vertecies - 6


# Tests:


from unittest import TestCase, main


class DGTest(TestCase):
    def test_realizable(self): pass

    def test_tree(self): pass

    def test_hamilton(self): pass

    def test_euler(self): pass

    def test_planar(self): pass


if __name__ == '__main__': main()
