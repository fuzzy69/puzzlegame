# -*- coding: UTF-8 -*-
# !/usr/bin/env python

from math import sqrt

from unittest import TestCase, main

from source.vector2d import Vector2D


class TestVector2D(TestCase):
    def setUp(self):
        self._vector = Vector2D(10, 10)
    
    def test_add(self):
        v1 = Vector2D(5, 5)
        v2 = Vector2D(15, 15)
        self.assertEqual(self._vector + v1, v2, "invalid add operator")

    def test_sub(self):
        v1 = Vector2D(3, 8)
        v2 = Vector2D(7, 2)
        self.assertEqual(self._vector - v1, v2, "invalid subtraction operator")

    def test_mul(self):
        v1 = Vector2D(15, 15)
        self.assertEqual(self._vector * 1.5, v1, "invalid multiply operator")

    def test_equal(self):
        v1 = Vector2D(10, 10)
        self.assertEqual(self._vector, v1, "invalid equal operator")

    def test_not_equal(self):
        v1 = Vector2D(5, 5)
        self.assertNotEqual(self._vector, v1, "invalid not equal operator")
        
    def test_length(self):
        self.assertEqual(self._vector.length(), sqrt(10 * 10 + 10 * 10), "invalid vector length")
    
    def test_normalize(self):
        self._vector.normalize()
        x = self._vector.x
        y = self._vector.y
        x2 = 10 / sqrt(10 * 10 + 10 * 10)
        y2 = 10 / sqrt(10 * 10 + 10 * 10)
        self.assertEqual((x, y), (x2, y2), "invalid vector normalize")


if __name__ == "__main__":
    main()
