# =============================================================================
# Draw two PCSELs coupled together. 
# =============================================================================

# Geometry parameters
a = 0.636  # lattice constant
Rcore = 0.24*a # air hole size: radius/periodicity
Rtrans = 0.22*a
Rclad = 0.20*a
Ncore = 5 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
Ndbr = 5 # DBR periods
tinp = 0.16 # DBR dielectric width
tair = 0.25 # DBR air trentch width
finwidth = 0.5 # fin width (DBR opening width)


import gdspy, math
from helpers import make_hexagonal_lattice, make_DBRs, get_coupled_pcsel_center_D4, make_coupled_DBRs, make_trucated_DBRs

# The GDSII file is called a library, which contains multiple cells.
lib = gdspy.GdsLibrary()

# Geometry must be placed in cells.
cell = lib.new_cell('DBR-PCSEL-Coupling')


# Create the geometry (a single rectangle) and add it to the cell.
# rect = gdspy.Rectangle((0, 0), (2, 1))
# cell.add(rect)

# =============================================================================
# structure 1: coupled PCSEL with 5 periods of PC (radius) nwith = 0
# =============================================================================

deviceSize = 50

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*0)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0, decoupled=False)

# =============================================================================
# structure 2: coupled PCSEL with 5 periods of PC (radius) nwith = 0.5
# =============================================================================


geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*1)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0.5, decoupled=False)

# =============================================================================
# structure 3: coupled PCSEL with 5 periods of PC (radius) nwith = 1
# =============================================================================


geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*2)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1, decoupled=False)

# =============================================================================
# structure 4: coupled PCSEL with 5 periods of PC (radius) nwith = 1.5
# =============================================================================


geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*3)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1.5, decoupled=False)

# =============================================================================
# structure 5: coupled PCSEL with 5 periods of PC (radius) nwith = 2
# =============================================================================


geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*4)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 2, decoupled=False)


# =============================================================================
# structure 6: coupled PCSEL with 7 periods of PC (radius) finwith = 1
# =============================================================================

a = 0.646  # lattice constant
Ncore = 7
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*1, deviceSize*0)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0, decoupled=False)

# =============================================================================
# structure 7: coupled PCSEL with 7 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 7
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*1, deviceSize*1)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0.5, decoupled=False)

# =============================================================================
# structure 8: coupled PCSEL with 7 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 7
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*1, deviceSize*2)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1, decoupled=False)

# =============================================================================
# structure 9: coupled PCSEL with 7 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 7
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*1, deviceSize*3)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1.5, decoupled=False)

# =============================================================================
# structure 10: coupled PCSEL with 7 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 7
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*1, deviceSize*4)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 2, decoupled=False)



# =============================================================================
# structure 11: coupled PCSEL with 10 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 10
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*2, deviceSize*0)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0, decoupled=False)

# =============================================================================
# structure 12: coupled PCSEL with 10 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 10
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*2, deviceSize*1)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0.5, decoupled=False)

# =============================================================================
# structure 13: coupled PCSEL with 10 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 10
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*2, deviceSize*2)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1, decoupled=False)

# =============================================================================
# structure 14: coupled PCSEL with 10 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 10
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*2, deviceSize*3)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1.5, decoupled=False)

# =============================================================================
# structure 15: coupled PCSEL with 10 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 10
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*2, deviceSize*4)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 2, decoupled=False)

# =============================================================================
# structure 16: coupled PCSEL with 15 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 15
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*3, deviceSize*0)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0, decoupled=False)

# =============================================================================
# structure 17: coupled PCSEL with 15 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 15
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*3, deviceSize*1)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0.5, decoupled=False)

# =============================================================================
# structure 18: coupled PCSEL with 15 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 15
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*3, deviceSize*2)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1, decoupled=False)

# =============================================================================
# structure 19: coupled PCSEL with 15 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 15
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*3, deviceSize*3)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1.5, decoupled=False)

# =============================================================================
# structure 20: coupled PCSEL with 15 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 15
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*3, deviceSize*4)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 2, decoupled=False)

# =============================================================================
# structure 21: decoupled PCSEL with 5 periods of PC (radius) finwith = 0.5
# =============================================================================

Ncore = 5
finwidth = 0.5
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*4, deviceSize*0)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0, decoupled=True)

# =============================================================================
# structure 22: decoupled PCSEL with 7 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 7
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*4, deviceSize*1)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0, decoupled=True)

# =============================================================================
# structure 23: decoupled PCSEL with 10 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 10
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*4, deviceSize*2)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0, decoupled=True)


# =============================================================================
# structure 24: decoupled PCSEL with 15 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 15
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*4, deviceSize*3)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0, decoupled=True)


# =============================================================================
# structure 25: decoupled PCSEL with 20 periods of PC (radius) finwith = 1
# =============================================================================

Ncore = 20
finwidth = 1
geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*4, deviceSize*4)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0, decoupled=True)


# Save the library in a file called 'first.gds'.
lib.write_gds('DBRs_PCSEL_Coupling.gds')

# Optionally, save an image of the cell as SVG.
cell.write_svg('DBRs_PCSEL_Coupling.svg')

# Display all cells using the internal viewer.
gdspy.LayoutViewer()


