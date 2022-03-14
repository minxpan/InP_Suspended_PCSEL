# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:50:34 2022

@author: panm
"""
import gdspy, math


def tuple_add(tuple1, tuple2):
    """
    Return the summation of two tuples

    Parameters
    ----------
    tuple1 : TYPE
        DESCRIPTION.
    tuple2 : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return tuple(map(sum, zip(tuple1, tuple2)))

# =============================================================================
# make_hexagonal_lattice draws the PCSEL region
# =============================================================================
def make_hexagonal_lattice(cell, a, start: int, end: int, radius: float, center: tuple):
    """
    Draw the air holes for PCSEL regions. 

    Parameters
    ----------
    cell : TYPE
        GDS cell.
    a : TYPE
        PC lattice constant.
    start : int
        starting position of the PCSEL region.
    end : int
        ending position.
    radius : float
        radius of the circular air hole.
    center : tuple
        Center of the PCSEL PC region.

    Returns
    -------
    None.

    """
    for i in range(start, end):
        if i == 0:
            circle = gdspy.Round(tuple_add((0, 0), center), radius, tolerance=0.0001)
            cell.add(circle)
        else:
            circle = gdspy.Round(tuple_add((-a*i, 0), center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((-a*i/2, a*i*(math.sqrt(3)/2)), center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((a*i/2, a*i*math.sqrt(3)/2), center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((a*i, 0), center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((a*i/2, -a*i*math.sqrt(3)/2), center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((-a*i/2, -a*i*math.sqrt(3)/2), center), radius, tolerance=0.0001)
            cell.add(circle)
            for jj in range(1, i):
                circle = gdspy.Round(tuple_add((-a*i+a/2*(jj), a*(jj)*(math.sqrt(3)/2)), center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((-a*i/2+a*jj, a*i*(math.sqrt(3)/2)), center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((a*i/2+a/2*jj, a*(i-jj)*math.sqrt(3)/2), center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((a*i-a/2*jj, -a*(jj)*(math.sqrt(3)/2)), center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((a*i/2-a*jj, -a*i*math.sqrt(3)/2), center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((-a*i/2-a/2*jj, -a*(i-jj)*math.sqrt(3)/2), center), radius, tolerance=0.0001)
                cell.add(circle)


def make_DBRs(cell, start: int, tinp: float, tair: float, Ndbr: int):
    
    hex = gdspy.Rectangle((0, 0), (2, 1))
    cell.add(hex)
    
    
    