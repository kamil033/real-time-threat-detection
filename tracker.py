import numpy as np

class CentroidTracker:
    def __init__(self):
        self.nextObjectID = 0
        self.objects = {}

    def update(self, detections):
        new_objects = {}

        for det in detections:
            (x, y, w, h, emotion) = det
            new_objects[self.nextObjectID] = (x, y, w, h, emotion)
            self.nextObjectID += 1

        self.objects = new_objects
        return self.objects
