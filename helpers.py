# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:50:34 2022

@author: panm
"""
import gdspy, math, operator
import uuid


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


def tuple_substract(tuple1, tuple2):
    """
    return tuple1 - tuple2
    """
    return tuple(map(operator.sub, tuple1, tuple2))

# =============================================================================
# make_hexagonal_lattice draws the PCSEL region
# =============================================================================
def make_hexagonal_lattice(cell, a, start: int, end: int, radius: float, geometry_center: tuple):
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
            circle = gdspy.Round(tuple_add((0, 0), geometry_center), radius, tolerance=0.0001)
            cell.add(circle)
        else:
            circle = gdspy.Round(tuple_add((-a*i, 0), geometry_center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((-a*i/2, a*i*(math.sqrt(3)/2)), geometry_center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((a*i/2, a*i*math.sqrt(3)/2), geometry_center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((a*i, 0), geometry_center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((a*i/2, -a*i*math.sqrt(3)/2), geometry_center), radius, tolerance=0.0001)
            cell.add(circle)
            circle = gdspy.Round(tuple_add((-a*i/2, -a*i*math.sqrt(3)/2), geometry_center), radius, tolerance=0.0001)
            cell.add(circle)
            for jj in range(1, i):
                circle = gdspy.Round(tuple_add((-a*i+a/2*(jj), a*(jj)*(math.sqrt(3)/2)), geometry_center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((-a*i/2+a*jj, a*i*(math.sqrt(3)/2)), geometry_center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((a*i/2+a/2*jj, a*(i-jj)*math.sqrt(3)/2), geometry_center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((a*i-a/2*jj, -a*(jj)*(math.sqrt(3)/2)), geometry_center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((a*i/2-a*jj, -a*i*math.sqrt(3)/2), geometry_center), radius, tolerance=0.0001)
                cell.add(circle)
                circle = gdspy.Round(tuple_add((-a*i/2-a/2*jj, -a*(i-jj)*math.sqrt(3)/2), geometry_center), radius, tolerance=0.0001)
                cell.add(circle)


def get_prism_vertices(start, end, center):
    return [
            tuple_add((-end, 0), center),
            tuple_add((-end*math.cos(math.pi/3), -end*math.sin(math.pi/3)), center),
            tuple_add((end*math.cos(math.pi/3), -end*math.sin(math.pi/3)), center),
            tuple_add((end, 0), center),
            tuple_add((end*math.cos(math.pi/3), end*math.sin(math.pi/3)), center),
            tuple_add((-end*math.cos(math.pi/3), end*math.sin(math.pi/3)), center),
            tuple_add((-end, 0), center),
            tuple_add((-start, 0), center),
            tuple_add((-start*math.cos(math.pi/3), start*math.sin(math.pi/3)), center),
            tuple_add((start*math.cos(math.pi/3), start*math.sin(math.pi/3)), center),
            tuple_add((start, 0), center),
            tuple_add((start*math.cos(math.pi/3), -start*math.sin(math.pi/3)), center),
            tuple_add((-start*math.cos(math.pi/3), -start*math.sin(math.pi/3)), center),
            tuple_add((-start, 0), center),
        ]


def make_DBRs(cell, geometry_data: tuple, geometry_center: tuple, Ndbr: int):
    """
    

    Parameters
    ----------
    cell : TYPE
        GDS cell.
    geometry_data : tuple
        Geometry geometry_data.
    Ndbr : int
        periods of DBRs.

    Returns
    -------
    None.

    """
    (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth) = initilize_data(geometry_data)
    
    
    # D00 - D15: Radius of DBR gratings
    
    R00 = a*(Ncore + Ntrans + Nclad + 0.5)/2*math.sqrt(3)
    D00 = (R00 - tair/2)/math.sin(math.pi/3)
    D01 = (R00 + tair/2)/math.sin(math.pi/3)
    D02 = (R00 + tair/2 + tinp)/math.sin(math.pi/3)
    D03 = (R00 + tair/2 + tinp + tair)/math.sin(math.pi/3)
    D04 = (R00 + tair/2 + tinp*2 + tair)/math.sin(math.pi/3)
    D05 = (R00 + tair/2 + tinp*2 + tair*2)/math.sin(math.pi/3)
    D06 = (R00 + tair/2 + tinp*3 + tair*2)/math.sin(math.pi/3)
    D07 = (R00 + tair/2 + tinp*3 + tair*3)/math.sin(math.pi/3)
    D08 = (R00 + tair/2 + tinp*4 + tair*3)/math.sin(math.pi/3)
    D09 = (R00 + tair/2 + tinp*4 + tair*4)/math.sin(math.pi/3)
    D10 = (R00 + tair/2 + tinp*5 + tair*4)/math.sin(math.pi/3)
    D11 = (R00 + tair/2 + tinp*5 + tair*5)/math.sin(math.pi/3)
    D12 = (R00 + tair/2 + tinp*6 + tair*5)/math.sin(math.pi/3)
    D13 = (R00 + tair/2 + tinp*6 + tair*6)/math.sin(math.pi/3)
    D14 = (R00 + tair/2 + tinp*7 + tair*6)/math.sin(math.pi/3)
    D15 = (R00 + tair/2 + tinp*7 + tair*7)/math.sin(math.pi/3)
    
    Dbound = (R00 + tair/2 + tinp*10 + tair*10)/math.sin(math.pi/3)
    seo0 = -Dbound*math.cos(math.pi/3) - finwidth/2*math.cos(math.pi/6)
    deo0 = Dbound*math.sin(math.pi/3) - finwidth/2*math.sin(math.pi/6)
    teo0 = -Dbound*math.cos(math.pi/3) + finwidth/2*math.cos(math.pi/6)
    peo0 = Dbound*math.sin(math.pi/3) + finwidth/2*math.sin(math.pi/6)
    feo0 = -Dbound
    reo0 = finwidth/2

    DBRs = []
    DBRs.append(get_prism_vertices(D00, D01, geometry_center))
    DBRs.append(get_prism_vertices(D02, D03, geometry_center))
    DBRs.append(get_prism_vertices(D04, D05, geometry_center))
    DBRs.append(get_prism_vertices(D06, D07, geometry_center))
    DBRs.append(get_prism_vertices(D08, D09, geometry_center))
    DBRs.append(get_prism_vertices(D10, D11, geometry_center))
    DBRs.append(get_prism_vertices(D12, D13, geometry_center))
    DBRs.append(get_prism_vertices(D14, D15, geometry_center))
    
    fin1 = gdspy.Polygon([
        tuple_add((seo0, deo0), geometry_center),
        tuple_add((teo0, peo0), geometry_center),
        tuple_add((-seo0, -deo0), geometry_center),
        tuple_add((-teo0, -peo0), geometry_center),
        ])
    fin2 = gdspy.Polygon([
        tuple_add((-seo0, deo0), geometry_center),
        tuple_add((-teo0, peo0), geometry_center),
        tuple_add((seo0, -deo0), geometry_center),
        tuple_add((teo0, -peo0), geometry_center),
        ])
    fin3 = gdspy.Polygon([
        tuple_add((feo0, reo0), geometry_center),
        tuple_add((feo0, -reo0), geometry_center),
        tuple_add((-feo0, -reo0), geometry_center),
        tuple_add((-feo0, reo0), geometry_center),
        ])

    for nk in range(0, Ndbr, 1):
        # Subtract the fins from the DBRs
        inv = gdspy.boolean(gdspy.Polygon(DBRs[nk]), fin1, "not")
        inv = gdspy.boolean(inv, fin2, "not")
        inv = gdspy.boolean(inv, fin3, "not")
        cell.add(inv) 

      
def make_coupled_DBRs(cell, geometry_data: tuple, geometry_center: tuple, Ndbr: int, fins: []):
    """
    

    Parameters
    ----------
    cell : TYPE
        GDS cell.
    geometry_data : tuple
        Geometry geometry_data.
    Ndbr : int
        periods of DBRs.

    Returns
    -------
    None.

    """
    (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth) = initilize_data(geometry_data)
    
    
    # D00 - D15: Radius of DBR gratings
    
    R00 = a*(Ncore + Ntrans + Nclad + 0.5)/2*math.sqrt(3)
    D00 = (R00 - tair/2)/math.sin(math.pi/3)
    D01 = (R00 + tair/2)/math.sin(math.pi/3)
    D02 = (R00 + tair/2 + tinp)/math.sin(math.pi/3)
    D03 = (R00 + tair/2 + tinp + tair)/math.sin(math.pi/3)
    D04 = (R00 + tair/2 + tinp*2 + tair)/math.sin(math.pi/3)
    D05 = (R00 + tair/2 + tinp*2 + tair*2)/math.sin(math.pi/3)
    D06 = (R00 + tair/2 + tinp*3 + tair*2)/math.sin(math.pi/3)
    D07 = (R00 + tair/2 + tinp*3 + tair*3)/math.sin(math.pi/3)
    D08 = (R00 + tair/2 + tinp*4 + tair*3)/math.sin(math.pi/3)
    D09 = (R00 + tair/2 + tinp*4 + tair*4)/math.sin(math.pi/3)
    D10 = (R00 + tair/2 + tinp*5 + tair*4)/math.sin(math.pi/3)
    D11 = (R00 + tair/2 + tinp*5 + tair*5)/math.sin(math.pi/3)
    D12 = (R00 + tair/2 + tinp*6 + tair*5)/math.sin(math.pi/3)
    D13 = (R00 + tair/2 + tinp*6 + tair*6)/math.sin(math.pi/3)
    D14 = (R00 + tair/2 + tinp*7 + tair*6)/math.sin(math.pi/3)
    D15 = (R00 + tair/2 + tinp*7 + tair*7)/math.sin(math.pi/3)
    
    Dbound = (R00 + tair/2 + tinp*10 + tair*10)/math.sin(math.pi/3)
    seo0 = -Dbound*math.cos(math.pi/3) - finwidth/2*math.cos(math.pi/6)
    deo0 = Dbound*math.sin(math.pi/3) - finwidth/2*math.sin(math.pi/6)
    teo0 = -Dbound*math.cos(math.pi/3) + finwidth/2*math.cos(math.pi/6)
    peo0 = Dbound*math.sin(math.pi/3) + finwidth/2*math.sin(math.pi/6)
    feo0 = -Dbound
    reo0 = finwidth/2
    
    Dbound = 0
    seo1 = -Dbound*math.cos(math.pi/3) - finwidth/2*math.cos(math.pi/6)
    deo1 = Dbound*math.sin(math.pi/3) - finwidth/2*math.sin(math.pi/6)
    teo1 = -Dbound*math.cos(math.pi/3) + finwidth/2*math.cos(math.pi/6)
    peo1 = Dbound*math.sin(math.pi/3) + finwidth/2*math.sin(math.pi/6)
    feo1 = -Dbound
    reo1 = finwidth/2

    DBRs = []
    DBRs.append(get_prism_vertices(D00, D01, geometry_center))
    DBRs.append(get_prism_vertices(D02, D03, geometry_center))
    DBRs.append(get_prism_vertices(D04, D05, geometry_center))
    DBRs.append(get_prism_vertices(D06, D07, geometry_center))
    DBRs.append(get_prism_vertices(D08, D09, geometry_center))
    DBRs.append(get_prism_vertices(D10, D11, geometry_center))
    DBRs.append(get_prism_vertices(D12, D13, geometry_center))
    DBRs.append(get_prism_vertices(D14, D15, geometry_center))
    
    fin1 = gdspy.Polygon([
        tuple_add((seo0, deo0), geometry_center),
        tuple_add((teo0, peo0), geometry_center),
        tuple_add((-seo1, -deo1), geometry_center),
        tuple_add((-teo1, -peo1), geometry_center),
        ])
    fin2 = gdspy.Polygon([
        tuple_add((-seo0, deo0), geometry_center),
        tuple_add((-teo0, peo0), geometry_center),
        tuple_add((seo1, -deo1), geometry_center),
        tuple_add((teo1, -peo1), geometry_center),
        ])
    fin3 = gdspy.Polygon([
        tuple_add((feo0, reo0), geometry_center),
        tuple_add((feo0, -reo0), geometry_center),
        tuple_add((-feo1, -reo1), geometry_center),
        tuple_add((-feo1, reo1), geometry_center),
        ])
    fin4 = gdspy.Polygon([
        tuple_add((-seo0, -deo0), geometry_center),
        tuple_add((-teo0, -peo0), geometry_center),
        tuple_add((-teo1, -peo1), geometry_center),
        tuple_add((-seo1, -deo1), geometry_center),
        ])
    fin5 = gdspy.Polygon([
        tuple_add((seo0, -deo0), geometry_center),
        tuple_add((teo0, -peo0), geometry_center),
        tuple_add((teo1, -peo1), geometry_center),
        tuple_add((seo1, -deo1), geometry_center),
        ])
    fin6 = gdspy.Polygon([
        tuple_add((-feo0, -reo0), geometry_center),
        tuple_add((-feo0, reo0), geometry_center),
        tuple_add((-feo1, reo1), geometry_center),
        tuple_add((-feo1, -reo1), geometry_center),
        ])


    for nk in range(0, Ndbr, 1):
        # Subtract the fins from the DBRs
        inv = gdspy.Polygon(DBRs[nk])
        if fins[0]:
            inv = gdspy.boolean(inv, fin1, "not")
        if fins[1]:
            inv = gdspy.boolean(inv, fin2, "not")
        if fins[2]:
            inv = gdspy.boolean(inv, fin3, "not")
        if fins[3]:
            inv = gdspy.boolean(inv, fin4, "not")
        if fins[4]:
            inv = gdspy.boolean(inv, fin5, "not")
        if fins[5]:
            inv = gdspy.boolean(inv, fin6, "not")
        cell.add(inv) 
        
def get_coupled_pcsel_center_D4(centerA: tuple, geometry_data: tuple):
    (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth) = initilize_data(geometry_data)
    R00 = a*(Ncore + Ntrans + Nclad + 0.5)/2*math.sqrt(3)
    D03 = (R00 + tair/2 + tinp + tair)/math.sin(math.pi/3)
    D04 = (R00 + tair/2 + tinp*2 + tair)/math.sin(math.pi/3)
    Dm = (D03 + D04)/2
    # mirror_point = (Dm/2*(1 + math.cos(math.pi/3)), Dm/2*math.sin(math.pi/3))
    mirror_point = (Dm*math.cos(math.pi/6), centerA[1])
    return mirror_point, tuple_add(mirror_point, tuple_substract(mirror_point, centerA))

def initilize_data(geometry_data: tuple):
    a = geometry_data[0]
    Ncore = geometry_data[1]
    Ntrans = geometry_data[2]
    Nclad = geometry_data[3]
    tinp = geometry_data[4]
    tair = geometry_data[5]
    finwidth = geometry_data[6]
    return (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

def rotate_geometry(polygens, geometry_center, mirror_point, angle):
    polygens_rotated = []
    for item in polygens:
        slices = gdspy.slice(item.rotate(angle, geometry_center), mirror_point[0], axis=0)
        polygens_rotated.append(slices[1])
    return polygens_rotated
    

def make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection):
    
        
    cell0 = lib.new_cell(str(uuid.uuid4()))
    
    (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth) = initilize_data(geometry_data)

    Rcore = radii[0]
    Rtrans = radii[1]
    Rclad = radii[2]
    
    make_hexagonal_lattice(cell0, a, 0, Ncore, Rcore, geometry_center = geometry_center_A)
    make_hexagonal_lattice(cell0, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center_A)
    make_hexagonal_lattice(cell0, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center_A)

    geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

    # make_coupled_DBRs(cell0, geometry_data, geometry_center = geometry_center_A, Ndbr = 8, fins = [1,1,1,0,1,0])
    make_coupled_DBRs(cell0, geometry_data, geometry_center = geometry_center_A, Ndbr = 8, fins = [1,1,1,1,1,1])


    polygens = cell0.get_polygonsets()

    mirror_point, geometry_centerB = get_coupled_pcsel_center_D4(geometry_center_A, geometry_data)

    polygens_rotated = []
    for item in polygens:
        slices = gdspy.slice(item.rotate(math.pi/6, geometry_center_A), mirror_point[0], axis=0)
        polygens_rotated.append(slices[0])

    R00 = a*(Ncore + Ntrans + Nclad + 0.5)/2*math.sqrt(3)
    D00 = (R00 - tair/2)/math.sin(math.pi/3) - 1
    
    cell0.remove_polygons(lambda pts, layer, datatype: any(pts[:, 0]))
    Dw = 3*tinp + 2*tair
    Dh = 10*tinp + 10*tair
    Dt = mirror_point[0] - D00
    
    inv1 = gdspy.Polygon([(mirror_point[0] - Dw/2, mirror_point[0]*math.sin(math.pi/3) + 1 + Dh/2),
                        (mirror_point[0] + Dw/2, mirror_point[0]*math.sin(math.pi/3) + 1 + Dh/2),
                        (mirror_point[0] + Dw/2, mirror_point[0]*math.sin(math.pi/3) + 1 - Dh/2),
                        (mirror_point[0] - Dw/2, mirror_point[0]*math.sin(math.pi/3) + 1 - Dh/2)])
    inv2 = gdspy.Polygon([(mirror_point[0] - Dw/2, -mirror_point[0]*math.sin(math.pi/3) - 1 + Dh/2),
                        (mirror_point[0] + Dw/2, -mirror_point[0]*math.sin(math.pi/3) - 1 + Dh/2),
                        (mirror_point[0] + Dw/2, -mirror_point[0]*math.sin(math.pi/3) - 1 - Dh/2),
                        (mirror_point[0] - Dw/2, -mirror_point[0]*math.sin(math.pi/3) - 1 - Dh/2)])
    
    inv3 = gdspy.Polygon([(mirror_point[0] - Dt, mirror_point[1] + connection/2),
                        (mirror_point[0] + Dt, mirror_point[1] + connection/2),
                        (mirror_point[0] + Dt, mirror_point[1] - connection/2),
                        (mirror_point[0] - Dt, mirror_point[1] - connection/2)])


    polygens_trucated = []
    for item in polygens_rotated:
        temp = gdspy.boolean(item, inv1, "not")
        temp2 = gdspy.boolean(temp, inv2, "not")
        if connection:
            polygens_trucated.append(gdspy.boolean(temp2, inv3, "not"))
        else:
            polygens_trucated.append(temp2)
        
    cell.add(polygens_trucated)

    cell0 = lib.new_cell(str(uuid.uuid4()))
    make_hexagonal_lattice(cell0, a, 0, Ncore, Rcore, geometry_center = geometry_centerB)
    make_hexagonal_lattice(cell0, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_centerB)
    make_hexagonal_lattice(cell0, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_centerB)

    geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

    # make_coupled_DBRs(cell0, geometry_data, geometry_center = geometry_centerB, Ndbr = 8, fins = [0,1,0,1,1,1])
    make_coupled_DBRs(cell0, geometry_data, geometry_center = geometry_centerB, Ndbr = 8, fins = [1,1,1,1,1,1])

    polygens = cell0.get_polygonsets()

    polygens_rotated = []
    for item in polygens:
        slices = gdspy.slice(item.rotate(math.pi/6, geometry_centerB), mirror_point[0], axis=0)
        polygens_rotated.append(slices[1])

    polygens_trucated = []
    for item in polygens_rotated:
        temp = gdspy.boolean(item, inv1, "not")
        temp2 = gdspy.boolean(temp, inv2, "not")
        if connection:
            polygens_trucated.append(gdspy.boolean(temp2, inv3, "not"))
        else:
            polygens_trucated.append(temp2)
        
    cell.add(polygens_trucated)
    
    lib.remove(cell = 'DBR-PCSEL-CouplingA')
    
    lib.remove(cell = 'DBR-PCSEL-CouplingB')

    