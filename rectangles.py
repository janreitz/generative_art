import cairo
import math
import random

def generate_rect_grid(width, height, num_rows, num_cols):
    rects = []
    for i in range(num_rows):
        for j in range(num_cols):
            rects.append((i * width, j * height, width, height))
    return rects

def split_rect_vertical(x, y, width, height):
    rects = []
    rects.append((x, y, width/2, height))
    rects.append((x + width/2, y, width/2, height))
    return rects

def split_rect_horizontal(x, y, width, height):
    rects = []
    rects.append((x, y, width, height/2))
    rects.append((x, y + height/2, width, height/2))
    return rects         

def random_recursive_splits(num_splits, rects):
    local_rects = rects
    for _ in range(num_splits):
        split_rects = []
        for x, y, width, height in local_rects:
            rand = random.randint(0,2)
            if rand == 0:
                split_rects += split_rect_horizontal(x, y, width, height)
            elif rand == 1:
                split_rects += split_rect_vertical(x, y, width, height)
            elif rand == 2:
                split_rects += [(x, y, width, height)]
        local_rects = split_rects
    return local_rects

if __name__ == "__main__":
    # configuration
    WIDTH, HEIGHT = 1000, 1000

    # Setting up Cairo
    surface = cairo.SVGSurface("rectangles.svg", WIDTH, HEIGHT)
    ctx = cairo.Context (surface)
    
    # background
    ctx.set_source_rgb(0.133,0.314,0.584)
    ctx.paint()

    # Line brush setup
    ctx.set_line_width(4)

    mondrian = [
        (255/255,240/255,1/255),
        (255/255,1/255,1/255),
        (1/255,1/255,253/255),
    ]

    greys = [(i/10, i/10, i/10) for i in range(10)]

    rects = generate_rect_grid(WIDTH/10, HEIGHT/10, 10, 10)
    rects = random_recursive_splits(3, rects)

    for x, y, width, height in rects:
        ctx.rectangle(x, y, width, height)
        ctx.set_source_rgb(0, 0, 0)
        ctx.stroke()
        ctx.rectangle(x, y, width, height)
        color = random.choice(mondrian)
        ctx.set_source_rgb(*color)
        ctx.fill()
    
    surface.finish()
