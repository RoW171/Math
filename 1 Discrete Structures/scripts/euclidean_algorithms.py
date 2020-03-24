#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-24"
__version__ = "0.0.0"

__all__ = ('euclidean_algorithm', 'extended_euclidean_algorithm',)

from typing import Tuple


def handle_args(a: int, b: int) -> Tuple[int, int]:
    """Really unnecessary, but keeps stuff slightly DRYer"""
    a, b, = (a, b,) if a <= b else (b, a,)
    if a < 0: raise ArithmeticError('"a" must be greater than 0!')
    return a, b,


def euclidean_algorithm(a: int, b: int) -> int:
    """
    Determine the greatest common denominator(gcd)
    by recursivly calling itself with b mod a.
    Notes:
        1. gcd(a, b) == gcd(b, a) == gcd(-a, b)
           == gcd(a, -b) == gcd(-a, -b)
              --> 0 <= a <= b
        2. gcd(a, b) == b if a == 0
        3. gdc(a, b) == gdc(b mod a, a) if 0 < a <= b
    :param a: a ∈ ℕ₀
    :param b: b ∈ {x ∈ ℕ₀ | x > a}
    :return: the greatest common denominator of a and b
    """
    a, b, = handle_args(a, b)
    if a == 0: return b
    return euclidean_algorithm(b % a, a)


def extended_euclidean_algorithm(a: int, b: int) -> Tuple[int, int]:
    """
    Determine alpha and beta that alpha * a + beta *  == gcd(a, b)
    by first performing a normal ea and keeping track of the divisions
    as well. Then 'refill the table' with beta - division * alpha, alpha.
    The explanation in the docs will be a bit clearer, especially when it
    comes to doing this by hand.
    :param a: a ∈ ℕ₀
    :param b: b ∈ {x ∈ ℕ₀ | x > a}
    :return: alpha, beta, where alpha * a + beta * b == gcd(a, b)
    """
    a, b, = handle_args(a, b)
    if a == 0: return 0, 1,
    division, rest = divmod(b, a)
    if rest == 0: return 1, 0,
    alpha, beta, = extended_euclidean_algorithm(rest, a)
    return beta - division * rest, alpha,


if __name__ == '__main__': pass
