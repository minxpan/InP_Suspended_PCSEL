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
cell = lib.new_cell('DBR-PCSEL-CONFIG-I')

# Create the geometry (a single rectangle) and add it to the cell.
# rect = gdspy.Rectangle((0, 0), (2, 1))
# cell.add(rect)

# =============================================================================
# structure 1: PCSEL with 5 periods of DBR, finwidth 1 micron
# =============================================================================

deviceSize = 50
geometry_center = (0, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, geometry_center = geometry_center, Ndbr = 5)

# =============================================================================
# structure 2: PCSEL without DBR, finwidth 1 micron
# =============================================================================

geometry_center = (0, 0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)


# =============================================================================
# structure 3: PCSEL with 1 period of DBR, finwidth 1 micron
# =============================================================================

geometry_center = (0, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 1, geometry_center = geometry_center)


# =============================================================================
# structure 4: PCSEL with 2 periods of DBR, finwidth 1 micron
# =============================================================================

geometry_center = (deviceSize*1, deviceSize*3)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 2, geometry_center = geometry_center)

# =============================================================================
# structure 5: PCSEL with 3 periods of DBR, finwidth 1 micron
# =============================================================================

geometry_center = (deviceSize*1, deviceSize*1)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 3, geometry_center = geometry_center)

# =============================================================================
# structure 6: PCSEL with 4 periods of DBR, finwidth 1 micron
# =============================================================================

geometry_center = (deviceSize*2, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 4, geometry_center = geometry_center)

# =============================================================================
# structure 7: PCSEL with 5 periods of DBR, finwidth 1 micron
# =============================================================================

geometry_center = (deviceSize*2, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 8: PCSEL with 6 periods of DBR, finwidth 1 micron
# =============================================================================

geometry_center = (deviceSize*2, 0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 6, geometry_center = geometry_center)

# =============================================================================
# structure 9: PCSEL with 7 periods of DBR, finwidth 1 micron, Ncore = 10
# =============================================================================

geometry_center = (deviceSize*3, deviceSize*1)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 7, geometry_center = geometry_center)

# =============================================================================
# structure 10: PCSEL with 7 periods of DBR, finwidth 1 micron, Ncore = 15
# =============================================================================

Ncore = 15
geometry_center = (deviceSize*3, deviceSize*3)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 7, geometry_center = geometry_center)

# =============================================================================
# structure 11: PCSEL with 8 periods of DBR , finwidth 3 micron, Ncore = 15
# =============================================================================

geometry_center = (deviceSize*4, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, 3)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)

# =============================================================================
# structure 12: PCSEL with 8 periods of DBR, finwidth 1 micron, Ncore = 15
# =============================================================================

geometry_center = (deviceSize*4, 0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, 1)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)

# =============================================================================
# structure 13: PCSEL with 8 periods of DBR, finwidth 2 micron, Ncore = 15
# =============================================================================

geometry_center = (deviceSize*4, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, 2)

make_DBRs(cell, geometry_data, Ndbr = 8, geometry_center = geometry_center)


# Save the library in a file called 'first.gds'.
lib.write_gds('DBRs_PCSEL_Config.I.gds')

# Optionally, save an image of the cell as SVG.
cell.write_svg('DBRs_PCSEL_Config.I.svg')

# Display all cells using the internal viewer.
gdspy.LayoutViewer()


