# =============================================================================
# Draw a single PCSEL device with uniform PC lattice configurations. 
# =============================================================================

# Geometry parameters
a = 0.646  # lattice constant
Rcore = 0.24*a # air hole size: radius/periodicity
Rtrans = 0.22*a
Rclad = 0.20*a
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
Ndbr = 5 # DBR periods
tinp = 0.16 # DBR dielectric width
tair = 0.25 # DBR air trentch width
finwidth = 1.0 # fin width (DBR opening width)


import gdspy
from helpers import make_hexagonal_lattice, make_DBRs

# The GDSII file is called a library, which contains multiple cells.
lib = gdspy.GdsLibrary()

# Geometry must be placed in cells.
cell = lib.new_cell('DBR-PCSEL-Scaling')

# Create the geometry (a single rectangle) and add it to the cell.
# rect = gdspy.Rectangle((0, 0), (2, 1))
# cell.add(rect)

# =============================================================================
# structure 1: 4 PC PCSEL with 8 periods of DBR, finwidth 0.5 micron
# =============================================================================

Ncore = 4
a = 0.63
finwidth = 0.5
deviceSize = 50
geometry_center = (0, 0)

make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, geometry_center = geometry_center, Ndbr = 8)

# =============================================================================
# structure 2: 4 PC PCSEL with 5 periods of DBR, finwidth 0.5 micron
# =============================================================================
geometry_center = (0, deviceSize)

make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, geometry_center = geometry_center, Ndbr = 5)

# =============================================================================
# structure 3: 4 PC PCSEL with 3 periods of DBR, finwidth 0.5 micron
# =============================================================================

geometry_center = (0, deviceSize*2)

make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, geometry_center = geometry_center, Ndbr = 3)

# =============================================================================
# structure 4: 4 PC PCSEL with 1 period of DBR, finwidth 0.5 micron
# =============================================================================

geometry_center = (0, deviceSize*3)

make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, geometry_center = geometry_center, Ndbr = 1)

# =============================================================================
# structure 5: PCSEL without DBRs
# =============================================================================

geometry_center = (0, deviceSize*4)

make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)



# =============================================================================
# =============================================================================
# =============================================================================
# # # structure 6: 5 PC PCSEL with 5 period of DBR, finwidth 0.5 micron
# =============================================================================
# =============================================================================
# =============================================================================

Ncore = 5
a = 0.636
finwidth = 0.5

geometry_center = (deviceSize*1, deviceSize*0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 7: 5 PC PCSEL with 8 period of DBR, finwidth 0.5 micron
# =============================================================================

geometry_center = (deviceSize*1, deviceSize*1)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)

# =============================================================================
# structure 8: 5 PC PCSEL without DBR
# =============================================================================

geometry_center = (deviceSize*1, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# =============================================================================
# =============================================================================
# # # structure 9: 6 PC PCSEL with 8 period of DBR, finwidth 0.5 micron
# =============================================================================
# =============================================================================
# =============================================================================
Ncore = 6
a = 0.636
finwidth = 0.5
geometry_center = (deviceSize*1, deviceSize*3)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)

# =============================================================================
# structure 10: 6 PC PCSEL with 5 period of DBR, finwidth 0.5 micron
# =============================================================================

geometry_center = (deviceSize*1, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 11: 6 PC PCSEL without DBR
# =============================================================================

geometry_center = (deviceSize*2, deviceSize*0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# =============================================================================
# =============================================================================
# # # structure 12: 7 PC PCSEL with 8 period of DBR, finwidth 1.5 micron
# =============================================================================
# =============================================================================
# =============================================================================

Ncore = 7
a = 0.646
finwidth = 1.5

geometry_center = (deviceSize*2, deviceSize*1)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)

# =============================================================================
# structure 13: 7 PC PCSEL with 5 period of DBR, finwidth 1.5 micron
# =============================================================================

geometry_center = (deviceSize*2, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 14: 7 PC PCSEL without DBR
# =============================================================================

geometry_center = (deviceSize*2, deviceSize*3)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 15: 8 PC PCSEL without DBR
# =============================================================================

Ncore = 8
a = 0.646
finwidth = 1.5

geometry_center = (deviceSize*2, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 16: 8 PC PCSEL with 5 period of DBR, finwidth 1.5 micron
# =============================================================================

geometry_center = (deviceSize*3, deviceSize*0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 17: 8 PC PCSEL with 8 period of DBR, finwidth 1.5 micron
# =============================================================================

geometry_center = (deviceSize*3, deviceSize*1)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)

# =============================================================================
# structure 18: 9 PC PCSEL with 8 period of DBR, finwidth 1.5 micron
# =============================================================================

Ncore = 9
a = 0.646
finwidth = 1.5

geometry_center = (deviceSize*3, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)


# =============================================================================
# structure 19: 9 PC PCSEL without DBR
# =============================================================================

geometry_center = (deviceSize*3, deviceSize*3)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 20: 10 PC PCSEL without DBR
# =============================================================================

Ncore = 10
a = 0.646
finwidth = 1.5

geometry_center = (deviceSize*3, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 21: 10 PC PCSEL with 8 period of DBR, finwidth 1.5 micron
# =============================================================================

geometry_center = (deviceSize*4, deviceSize*0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)

# =============================================================================
# =============================================================================
# =============================================================================
# # # structure 22: 12 PC PCSEL without DBR
# =============================================================================
# =============================================================================
# =============================================================================

Ncore = 12
a = 0.646
finwidth = 1.5

geometry_center = (deviceSize*4, deviceSize*1)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 23: 12 PC PCSEL with 8 period of DBR, finwidth 1.5 micron
# =============================================================================

geometry_center = (deviceSize*4, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)

# =============================================================================
# =============================================================================
# =============================================================================
# # # structure 24: 15 PC PCSEL without DBR
# =============================================================================
# =============================================================================
# =============================================================================

Ncore = 15
a = 0.646
finwidth = 1.5

geometry_center = (deviceSize*4, deviceSize*3)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 25: 15 PC PCSEL with 8 period of DBR, finwidth 1.5 micron
# =============================================================================

geometry_center = (deviceSize*4, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)


# Save the library in a file called 'first.gds'.
lib.write_gds('DBRs_PCSEL_Scaling.gds')

# Optionally, save an image of the cell as SVG.
cell.write_svg('DBRs_PCSEL_Scaling.svg')

# Display all cells using the internal viewer.
gdspy.LayoutViewer()


