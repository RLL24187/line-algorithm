from display import *
from draw import *
import math
import random

s = new_screen()
c = [ 0, 255, 0 ]

# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, int(YRES / 2), s, c)
# draw_line(XRES-1, YRES-1, 0, int(YRES / 2), s, c)
#
# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, YRES/2, s, c);
#
# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);
#
# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);
#
# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, int(YRES/2), XRES-1, int(YRES/2), s, c);
# draw_line(int(XRES/2), 0, int(XRES/2), YRES-1, s, c);

def drawstar(x0, y0, s, c, r):
    draw_line(x0 - r, y0, x0 + r, y0, s, c) #horizontal
    draw_line(x0 - r, y0 - r, x0 + r, y0 + r, s, c) #slope 1
    draw_line(x0, y0 - r, x0, y0 + r, s, c) #vertical
    draw_line(x0 + r, y0 - r, x0 - r, y0 + r, s, c) #slope -1

midx = int(XRES / 2)
midy = int(XRES / 2)
for x in range (XRES - 1):
    c[RED] = int(c[RED] + 1) % 256
    c[GREEN] = int(c[GREEN] + 2) % 256
    c[BLUE] = int(c[BLUE] + 3) % 256
    x0 = midx + (midx) * math.cos(x * math.pi / (XRES - 1))
    y0 = midy + (midy) * math.sin(x * math.pi / (YRES - 1))
    x1 = (midx + x0) / 4
    y1 = (midy + y0) / 4
    Y = y0 - y1
    X = x0 - x1
    draw_line(int(x0), int(y0), int(x1), int(y1), s, c)

for x in range (XRES - 1):
    c[RED] = int(c[RED] + 1) % 256
    c[GREEN] = int(c[GREEN] + 2) % 256
    c[BLUE] = int(c[BLUE] + 3) % 256
    x0 = midx + (midx) * math.cos(x * math.pi / (XRES - 1))
    y0 = midy + (midy) * math.sin(x * math.pi / (YRES - 1))
    x1 = (midx + x0) / 4
    y1 = (midy + y0) / 4
    Y = y0 - y1
    X = x0 - x1
    draw_line(XRES - 1 - int(x0), int(y1), XRES - 1 - int(x1), int(y0), s, c)

for x in range (XRES - 1):
    if (x > 10 and x < XRES - 11):
        n = random.randint(0, 10)
        if (n > 6):
            x = random.randint(10, XRES - 11)
            y = random.randint(10, YRES - 11)
            c = [ (x + y) % 256, x % 256, y % 256]
            drawstar(x, y, s, c, int(n / 2))
display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
