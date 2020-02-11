from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x1 < x0): # x1 should always be >= x0
        x1, x0 = x0, x1
        y1, y0 = y0, y1 # have to reverse y's too

    A = int(y0) - int(y1) #change in Y
    B = int(x1) - int(x0) #negative change in X

    if (B == 0): # check vertical line first to prevent 0 division
        for y in range (y0, y1 + 1):
            plot(screen, color, x, y)
    else:
        slope = float(A / -B)
        print(slope)
        if (slope == 0): # horizontal line
            for x in range (x0, x1 + 1):
                plot(screen, color, x, y)

        # octant 1 and 5
        # print(slope)
        x = int(x0)
        y = int(y0)
        A2 = 2 * A
        B2 = 2 * B
        if (slope <= 1 and slope > 0 ):
            print("octant 1 or 5")
            d = A2 + B
            while (x <= x1):
                plot (screen, color, x, y)
                if (d > 0):
                    y = y + 1
                    d = d + B2
                x = x + 1
                d = d + A2
