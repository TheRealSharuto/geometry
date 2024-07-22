""" 
test that the calculate_area function does the right thing for some well-understood input
"""
from geometry.circle import calculate_area
from math import pi

def test_calculate_area():
    assert calculate_area(1) == pi