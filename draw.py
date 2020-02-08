from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    A = int(y0) - int(y1)
    B = int(x0) - int(x1)
    x = int(x0)
    y = int(y0)
    slope = float(A / B)
    # octant 1 and 5
    if (slope < 1 and slope > 0 ):
        oct1(A, B, x0, y0, x1, y1, screen, color)

def oct1(A, B, x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    d = 2 * A + B
    while (x <= x1):
        plot (screen, color, x, y)
        if (d > 0):
            y = y + 1
            d = d + 2 * B
        x = x + 1
        d = d + 2 * A
