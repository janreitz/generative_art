def rgb255to1(palette):
    normalized = []
    for color in palette:
        normalized += [tuple(val / 255 for val in color)]
    return normalized

mondrian_rgb_255 = [
    (255,240,1),
    (255,1,1),
    (1,1,253),
    (255,255,255)
]

greys_rgb_1 = [(i/10, i/10, i/10) for i in range(10)]