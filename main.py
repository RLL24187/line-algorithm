from display import *
from draw import *
import math

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

midx = int(XRES / 2)
midy = int(XRES / 2)
for x in range (XRES - 1):
    c = [0, 255, 0]
    x0 = midx + (midx) * cos(x * math.pi / (XRES - 1))
    y0 = midy + (midy) * sin(x * math.pi / (YRES - 1))
    x1 = x0 / 4
    y1 = y0 / 4
    Y = y0 - y1
    X = x0 - x1
    if (X == 0):
        c = [255, 255, 255]
    else:
        slope = Y / X
        if (slope != 0):
            n = int(YRES / slope)
            if (slope > 1):
                c = [n % 256, (255 - n) % 256, n % 256]
            else:
                c = [int(.5 * n) % 256, n % 256, int(.5 * n) % 256]
    draw_line(int(x0), int(y0), int(x1), int(y1), s, c)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
