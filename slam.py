import cv2
import numpy as np
from frameHelper import Frame,FrameManager
cap = cv2.VideoCapture("test_countryroad.mp4")
frmManager = FrameManager();
while True:
    ret,frame = cap.read()
    if ret is False:
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_gray = cv2.cvtColor(frame_rgb,cv2.COLOR_RGB2GRAY)
    frame_output = np.copy(frame_rgb)


    frm = Frame(frame_gray)
    frmManager.addFrame(frm)
    if len(frmManager.frames)==1:
        continue

    matches = frmManager.matchFrames(frmManager.frames[-1],frmManager.frames[-2])

    for p1,p2 in matches:
        cv2.line(frame_output, tuple(p1), tuple(p2), (0, 255, 0))
        cv2.circle(frame_output, tuple(p2), 3, (0, 255, 0))

    cv2.imshow("Frame",frame_output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
