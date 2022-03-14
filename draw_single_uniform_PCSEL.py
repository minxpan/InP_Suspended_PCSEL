# =============================================================================
# Draw a single PCSEL device with uniform PC lattice configurations. 
# =============================================================================

# Geometry parameters
a=0.685
Rcore = 0.24*a
Rtrans = 0.22*a
Rclad = 0.20*a
Ncore = 5
Ntrans = 4
Nclad = 3
Ndbr = 5




import gdspy
from helpers import make_hexagonal_lattice

# The GDSII file is called a library, which contains multiple cells.
lib = gdspy.GdsLibrary()

# Geometry must be placed in cells.
cell = lib.new_cell('DBR-PC')

# Create the geometry (a single rectangle) and add it to the cell.
# rect = gdspy.Rectangle((0, 0), (2, 1))
# cell.add(rect)


make_hexagonal_lattice(cell, a, 0, Ncore, Rcore, (0, 0))
make_hexagonal_lattice(cell, a, Ncore, Ncore+Ntrans, Rtrans, (0, 0))
make_hexagonal_lattice(cell, a, Ncore+Ntrans, Ncore+Ntrans+Nclad, Rclad, (0, 0))









# Save the library in a file called 'first.gds'.
lib.write_gds('DBR_PCSEL.gds')

# Optionally, save an image of the cell as SVG.
cell.write_svg('DBR_PCSEL.svg')

# Display all cells using the internal viewer.
gdspy.LayoutViewer()


