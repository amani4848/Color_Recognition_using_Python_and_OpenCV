
import cv2
import numpy as np 

cap = cv2.VideoCapture('red_flower.mp4')

if not cap.isOpened():
    print("Error: Video not loaded")
    exit()

clicked = False
r = g = b = xpos = ypos = 0

def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked, frame
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = frame[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('Video')
cv2.setMouseCallback('Video', draw_function)

paused = False

while True:
    if not paused:
        ret, frame = cap.read()
        if not ret:
            print("Video ended")
            break

    if clicked:
        cv2.rectangle(frame, (20, 20), (600, 60), (b, g, r), -1)
        text = f'R={r} G={g} B={b}'
        cv2.putText(frame, text, (50, 50), 2, 0.8, (255,255,255), 2)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(30) & 0xFF
    if key == 27: 
        break
    elif key == ord('p'):  
        paused = not paused
        clicked = False

cap.release()
cv2.destroyAllWindows()
