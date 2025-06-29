import cv2
import numpy as np
from ultralytics import YOLO
from tracker import CentroidTracker

model = YOLO("models/best.pt") 

tracker = CentroidTracker()

cap = cv2.VideoCapture("15sec_input_720p.mp4")
output = cv2.VideoWriter("output/tracked_output.mp4",
                         cv2.VideoWriter_fourcc(*'mp4v'), 30, 
                         (int(cap.get(3)), int(cap.get(4))))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, stream=False)

    boxes = []
    for r in results:
        for box in r.boxes.xyxy.cpu().numpy():
            x1, y1, x2, y2 = box[:4]
            boxes.append((int(x1), int(y1), int(x2), int(y2)))

    objects = tracker.update(boxes)

    for (obj_id, centroid) in objects.items():
        cv2.circle(frame, centroid, 5, (0, 255, 0), -1)
        cv2.putText(frame, f"Player {obj_id}", (centroid[0] - 10, centroid[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    output.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
output.release()
cv2.destroyAllWindows()
