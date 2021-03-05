#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    In Euclidean plane geometry, a rectangle is a quadrilateral with four right angles.
"""
from decimal import Decimal


class Rectangle:
    """
    In Euclidean plane geometry, a rectangle is a quadrilateral with four right angles.
    It can also be defined as an equiangular quadrilateral, since equiangular means that all of its angles are equal (360°/4 = 90°).
    It can also be defined as a parallelogram containing a right angle. A rectangle with four sides of equal length is a square.
    The term oblong is occasionally used to refer to a non-square rectangle.
    """

    def __init__(
        self,
        lower_left_x: Decimal,
        lower_left_y: Decimal,
        width: Decimal,
        height: Decimal,
    ):
        assert width >= 0
        assert height >= 0
        self.x = lower_left_x
        self.y = lower_left_y
        self.width = width
        self.height = height

    def get_x(self) -> Decimal:
        """
        This function returns the x-coordinate of the lower-left of this Rectangle
        """
        return self.x

    def get_y(self) -> Decimal:
        """
        This function returns the y-coordinate of the lower-left of this Rectangle
        """
        return self.y

    def get_width(self) -> Decimal:
        """
        This function returns the width of this Rectangle
        """
        return self.width

    def get_height(self) -> Decimal:
        """
        This function returns the height of this Rectangle
        """
        return self.height