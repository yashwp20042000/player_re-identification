import numpy as np

class CentroidTracker:
    def __init__(self, max_disappeared=50):
        self.next_id = 0
        self.objects = {} 
        self.disappeared = {}  
        self.max_disappeared = max_disappeared

    def register(self, centroid):
        self.objects[self.next_id] = centroid
        self.disappeared[self.next_id] = 0
        self.next_id += 1

    def deregister(self, object_id):
        del self.objects[object_id]
        del self.disappeared[object_id]

    def update(self, rects):
        if len(rects) == 0:
            for obj_id in list(self.disappeared.keys()):
                self.disappeared[obj_id] += 1
                if self.disappeared[obj_id] > self.max_disappeared:
                    self.deregister(obj_id)
            return self.objects

        centroids = np.array(
            [(int((x1 + x2) / 2), int((y1 + y2) / 2)) for (x1, y1, x2, y2) in rects]
        )

        if len(self.objects) == 0:
            for centroid in centroids:
                self.register(centroid)
        else:
            object_ids = list(self.objects.keys())
            existing_centroids = np.array(list(self.objects.values()))

            # Compute distances
            distances = np.linalg.norm(existing_centroids[:, np.newaxis] - centroids, axis=2)

            rows = distances.min(axis=1).argsort()
            cols = distances.argmin(axis=1)[rows]

            used_rows = set()
            used_cols = set()

            for row, col in zip(rows, cols):
                if row in used_rows or col in used_cols:
                    continue
                self.objects[object_ids[row]] = centroids[col]
                self.disappeared[object_ids[row]] = 0
                used_rows.add(row)
                used_cols.add(col)

            unused_cols = set(range(len(centroids))) - used_cols
            for col in unused_cols:
                self.register(centroids[col])

            unused_rows = set(range(len(existing_centroids))) - used_rows
            for row in unused_rows:
                obj_id = object_ids[row]
                self.disappeared[obj_id] += 1
                if self.disappeared[obj_id] > self.max_disappeared:
                    self.deregister(obj_id)

        return self.objects
