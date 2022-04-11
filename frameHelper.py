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
        feats = cv2.goodFeaturesToTrack(frame,1000,qualityLevel=0.01,minDistance = 1)
        #extraction
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in feats]

        kps,des = orb.compute(frame,kps)
        self.kps = kps
        self.des = des
        #getters
        @property
        def data(self):
            return sef.data
        @property
        def kps(self):
            return sef.kps
        @property
        def des(self):
            return sef.des

#TODO: Add frame manager
