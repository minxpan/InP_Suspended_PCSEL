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
# structure 1: coupled PCSEL with 5 periods of PC (radius)
# =============================================================================

deviceSize = 50

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*0)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0)

# =============================================================================
# structure 2: coupled PCSEL with 5 periods of PC (radius)
# =============================================================================


geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*1)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 0.5)

# =============================================================================
# structure 3: coupled PCSEL with 5 periods of PC (radius)
# =============================================================================


geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*2)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1)

# =============================================================================
# structure 4: coupled PCSEL with 5 periods of PC (radius)
# =============================================================================


geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*3)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 1.5)

# =============================================================================
# structure 5: coupled PCSEL with 5 periods of PC (radius)
# =============================================================================


geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)
radii = (Rcore, Rtrans, Rclad)

geometry_center_A = (deviceSize*0, deviceSize*4)

make_trucated_DBRs(lib, cell, geometry_data, radii, geometry_center_A, connection = 2)


# Save the library in a file called 'first.gds'.
lib.write_gds('DBRs_PCSEL_Coupling.gds')

# Optionally, save an image of the cell as SVG.
cell.write_svg('DBRs_PCSEL_Coupling.svg')

# Display all cells using the internal viewer.
gdspy.LayoutViewer()


