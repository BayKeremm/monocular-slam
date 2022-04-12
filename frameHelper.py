import cv2
import numpy as np

class Frame(object):
    def __init__(self,frame):
        self.data = frame
        self.extractORBs(frame)

    def extractORBs(self,frame):
        orb = cv2.ORB_create()
        #detection
        #TODO: Understand the function below
        feats = cv2.goodFeaturesToTrack(frame,3000,qualityLevel=0.01,minDistance = 1)
        #extraction
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in feats]

        kps,des = orb.compute(frame,kps)
        self.kps = kps
        self.des = des
        #getters
        @property
        def data(self):
            return self.data
        @property
        def kps(self):
            return self.kps
        @property
        def des(self):
            return self.des
#TODO: Add frame manager
class FrameManager(object):
    def __init__(self):
        self._frames = []
    def addFrame(self,frame):
        self.frames.append(frame)
    @property
    def frames(self):
        return self._frames
    
    def matchFrames(self,f1,f2):
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        matches = bf.knnMatch(f1.des,f2.des,k=2)

        #ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                p1=f1.kps[m.queryIdx].pt
                p2=f2.kps[m.trainIdx].pt
                good.append([p1, p2])
        good = np.asarray(good,dtype=int)
        return good

