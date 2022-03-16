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
cell = lib.new_cell('DBR-PCSEL-Calibration')


# Create the geometry (a single rectangle) and add it to the cell.
# rect = gdspy.Rectangle((0, 0), (2, 1))
# cell.add(rect)

# =============================================================================
# structure 1: coupled PCSEL with 10 periods of PC (radius) nwith = 0, lattice constant a = 0.63
# =============================================================================

a = 0.630
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0

deviceSize = 50

geometry_center = (deviceSize*0, deviceSize*0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 2: coupled PCSEL with 10 periods of PC (radius) nwith = 0, lattice constant a = 0.635
# =============================================================================

a = 0.635
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0

deviceSize = 50

geometry_center = (deviceSize*0, deviceSize*1)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 3: coupled PCSEL with 10 periods of PC (radius) nwith = 0, lattice constant a = 0.64
# =============================================================================

a = 0.640
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0

deviceSize = 50

geometry_center = (deviceSize*0, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 4: coupled PCSEL with 10 periods of PC (radius) nwith = 0, lattice constant a = 0.645
# =============================================================================

a = 0.645
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0

deviceSize = 50

geometry_center = (deviceSize*0, deviceSize*3)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

# =============================================================================
# structure 5: coupled PCSEL with 10 periods of PC (radius) nwith = 0, lattice constant a = 0.65
# =============================================================================

a = 0.65
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0

deviceSize = 50

geometry_center = (deviceSize*0, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)


# =============================================================================
# structure 6: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# tinp = 0.18, tair = 0.23 DBR air trentch width
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 1

tinp = 0.18 # DBR dielectric width
tair = 0.23 # DBR air trentch width


geometry_center = (deviceSize*1, deviceSize*0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 7: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# tinp = 0.17, tair = 0.24 DBR air trentch width
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 1

tinp = 0.17 # DBR dielectric width
tair = 0.24 # DBR air trentch width


geometry_center = (deviceSize*1, deviceSize*1)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 8: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# tinp = 0.16, tair = 0.25 DBR air trentch width
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 1

tinp = 0.16 # DBR dielectric width
tair = 0.25 # DBR air trentch width


geometry_center = (deviceSize*1, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 9: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# tinp = 0.15, tair = 0.26 DBR air trentch width
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 1

tinp = 0.15 # DBR dielectric width
tair = 0.26 # DBR air trentch width


geometry_center = (deviceSize*1, deviceSize*3)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 10: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# tinp = 0.14, tair = 0.27 DBR air trentch width
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 1

tinp = 0.14 # DBR dielectric width
tair = 0.27 # DBR air trentch width


geometry_center = (deviceSize*1, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 11: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 0.5

tinp = 0.16 # DBR dielectric width
tair = 0.25 # DBR air trentch width


geometry_center = (deviceSize*2, deviceSize*0)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 12: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 1

tinp = 0.16 # DBR dielectric width
tair = 0.25 # DBR air trentch width


geometry_center = (deviceSize*2, deviceSize*1)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 13: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 1.5

tinp = 0.16 # DBR dielectric width
tair = 0.25 # DBR air trentch width


geometry_center = (deviceSize*2, deviceSize*2)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 14: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 2

tinp = 0.16 # DBR dielectric width
tair = 0.25 # DBR air trentch width


geometry_center = (deviceSize*2, deviceSize*3)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# =============================================================================
# structure 15: 10 PC (radius) PCSEL with 5 bperiod of DBR, finwidth 1 micron;
# Simulation optimized values: DBR dielectric width: tinp = 0.16, DBR air trentch width: tair = 0.25
# =============================================================================

a = 0.646
Ncore = 10 # PCSEL periods in radius
Ntrans = 0
Nclad = 0
finwidth = 2.5

tinp = 0.16 # DBR dielectric width
tair = 0.25 # DBR air trentch width


geometry_center = (deviceSize*2, deviceSize*4)
make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, geometry_center = geometry_center)
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, geometry_center = geometry_center)

geometry_data = (a, Ncore, Ntrans, Nclad, tinp, tair, finwidth)

make_DBRs(cell, geometry_data, Ndbr = 5, geometry_center = geometry_center)

# Save the library in a file called 'first.gds'.
lib.write_gds('DBRs_PCSEL_Calibration.gds')

# Optionally, save an image of the cell as SVG.
cell.write_svg('DBRs_PCSEL_Calibration.svg')

# Display all cells using the internal viewer.
gdspy.LayoutViewer()


