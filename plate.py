
from cadquery import func as cf

def plate_with_hole(length, width, thickness,
                    hole_d, hole_offset):
    plate = cf.box(length, width, thickness)

    hole = cf.cylinder(
        d=hole_d,
        h=thickness
    ).moved(x=hole_offset)

    part = plate - hole

    rim = part.faces(">Z").edges("%CIRCLE")

    return part.fillet(2.0, [rim])


# Create a parametric plate
part = plate_with_hole(80, 50, 10, 20, 20)

# Design validation
assert part.isValid()
assert part.Volume() > 0

print(len(part.Faces()), "faces")
