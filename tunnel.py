import cairo
import math
import random

if __name__ == "__main__":
    # configuration
    WIDTH, HEIGHT = 1000, 1000
    n = 100

    # Setting up Cairo
    surface = cairo.SVGSurface("tunnel.svg", WIDTH, HEIGHT)
    ctx = cairo.Context (surface)
    
    # background
    ctx.set_source_rgb(0,0,0)
    ctx.paint()

    # Line brush setup
    ctx.set_line_width(8)

    for i in range(1,n):
        scaling = 0.95
        translation = (WIDTH - WIDTH * scaling)/2
        ctx.translate(translation, translation)
        translation_to_center = WIDTH/2 - translation 
        ctx.translate(translation_to_center, translation_to_center)
        ctx.rotate(math.pi/180 * 5)
        ctx.translate(-translation_to_center, -translation_to_center)
        ctx.scale(scaling, scaling)
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.set_source_rgb(0, 0, 0)
        ctx.stroke()
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        ctx.set_source_rgb(1-0.95**i, 1-0.95**i, 1-0.95**i)
        ctx.fill()
    
    surface.finish()
