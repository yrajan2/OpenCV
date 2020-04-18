import numpy as np
import cv2

# Global variables
canvas = np.ones([500, 500, 3], 'uint8') * 255
radius = 3
color = (0, 0, 255)
pressed = False


# click callback
def click(event, x, y, flags, param):
    global canvas, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas, (x, y), radius, color, -1)
    elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
        cv2.circle(canvas, (x, y), radius, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False


# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:

    cv2.imshow("canvas", canvas)

    # key capture every 1ms
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        b, g, r = color
        color = (((b + 1) % 255), g, r)
    elif ch & 0xFF == ord('g'):
        b, g, r = color
        color = (b, ((g + 1) % 255), r)
    elif ch & 0xFF == ord('r'):
        b, g, r = color
        color = (b, g, (r + 1) % 255)

cv2.destroyAllWindows()