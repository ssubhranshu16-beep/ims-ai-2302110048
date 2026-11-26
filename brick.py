
import math
from cadquery import func as cf

def clutch_brick(length, width, height,
                 stud_d, stud_h, spacing,
                 rows=2, cols=4):

    body = cf.box(length, width, height)
    stud = cf.cylinder(d=stud_d, h=stud_h)

    brick = body

    for row in range(rows):
        for col in range(cols):
            x = (col - (cols - 1) / 2) * spacing
            y = (row - (rows - 1) / 2) * spacing

            brick = brick + stud.moved(x=x, y=y, z=height)

    return brick


# Create 2 x 4 clutch brick
brick = clutch_brick(31.6, 15.6, 9.6, 4.8, 1.7, 7.8)

# Expected volume: body + 8 studs
expected = (
    31.6 * 15.6 * 9.6
    + 8 * math.pi * (4.8 / 2) ** 2 * 1.7
)

assert brick.isValid()
assert abs(brick.Volume() - expected) < 0.5

print("Number of faces:", len(brick.Faces()))
print("Volume:", round(brick.Volume(), 2))

brick.exportStl("brick.stl")
