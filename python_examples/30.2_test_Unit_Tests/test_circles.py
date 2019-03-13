#!/usr/bin/env python3.5

"""test_circles.py.

TEST Thirtieth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""

import logging
import unittest
from circles import circle_area
from math import pi


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_2.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("#test_circles.py RUN / START")


class TestCircleArea(unittest.TestCase):
    """docstring for TestCircleArea."""

    def test_area(self):
        """Test areas when radius > 0."""
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * (2.1 ** 2))

    def test_values(self):
        """Test areas when radius = values."""
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        """Test areas when radius = invalid type."""
        self.assertRaises(TypeError, circle_area, 3 + 5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, False)
        self.assertRaises(TypeError, circle_area, "radius")
        self.assertRaises(TypeError, circle_area, (1, 2))
        self.assertRaises(TypeError, circle_area, [1, 2])
        self.assertRaises(TypeError, circle_area, {1: 2, 2: 1})
        self.assertRaises(TypeError, circle_area, None)
