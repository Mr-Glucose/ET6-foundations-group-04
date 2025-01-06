#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the FizzBuzz module.

This file contains unit tests for the fizzbuzz function.

Created on 06/01/2025
Author: Hector Colmenares
"""

import unittest

from solutions.challenge_12.fizzbuzz_program import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """Unit tests for the fizzbuzz function."""

    def test_fizzbuzz_case_first(self):
        """Test first value for numbers 1 to 5."""
        self.assertEqual(fizzbuzz(5)[0], "1")

    def test_fizzbuzz_case_second(self):
        """Test second value for numbers 1 to 5."""
        self.assertEqual(fizzbuzz(5)[1], "2")

    def test_fizzbuzz_case_third(self):
        """Test third value for numbers 1 to 5."""
        self.assertEqual(fizzbuzz(5)[2], "Fizz")

    def test_fizzbuzz_case_fourth(self):
        """Test fourth value for numbers 1 to 5."""
        self.assertEqual(fizzbuzz(5)[3], "4")

    def test_fizzbuzz_case_fifth(self):
        """Test fifth value for numbers 1 to 5."""
        self.assertEqual(fizzbuzz(5)[4], "Buzz")

    def test_fizz_only_third(self):
        """Test third value for a range containing only 'Fizz'."""
        self.assertEqual(fizzbuzz(3)[2], "Fizz")

    def test_buzz_only_last(self):
        """Test FizzBuzz for a range ending with 'Buzz'."""
        self.assertEqual(fizzbuzz(10)[-1], "Buzz")

    def test_fizzbuzz_case_last(self):
        """Test FizzBuzz for a number divisible by both 3 and 5."""
        self.assertEqual(fizzbuzz(15)[-1], "FizzBuzz")

    def test_invalid_input_zero(self):
        """Test FizzBuzz raises ValueError for input 0."""
        with self.assertRaises(ValueError):
            fizzbuzz(0)

    def test_invalid_input_negative(self):
        """Test FizzBuzz raises ValueError for negative input."""
        with self.assertRaises(ValueError):
            fizzbuzz(-5)

    def test_invalid_input_non_integer(self):
        """Test FizzBuzz raises ValueError for non-integer input."""
        with self.assertRaises(ValueError):
            fizzbuzz("a")

    def test_boundary_case(self):
        """Test FizzBuzz with the smallest valid input (n=1)."""
        self.assertEqual(fizzbuzz(1), ["1"])
