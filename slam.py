import cv2
import numpy as np
from frameHelper import Frame

cap = cv2.VideoCapture("test_countryroad.mp4")
while True:
    ret,frame = cap.read()
    if ret is False:
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_gray = cv2.cvtColor(frame_rgb,cv2.COLOR_RGB2GRAY)

    frame_output = np.copy(frame_rgb)
    frm = Frame(frame_gray)
    kps = frm.kps
    des = frm.des

    cv2.drawKeypoints(frame,kps,frame_output,color = (0,255,0))

    cv2.imshow("Frame",frame_output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
