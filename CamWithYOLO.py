import cv2
import time

config_path = "yolov4.cfg"
weights_path = "yolov4.weights"
names_path = "coco.names"

def detect():
    class_name = []
    with open('coco.names', 'r') as f:
        class_name = [cname.strip() for cname in f.readlines()]

    cap = cv2.VideoCapture(0)

    net = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

    model = cv2.dnn.DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1/255)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        start = time.time()
        classes, scores, boxes = model.detect(frame, 0.1, 0.2)
        end = time.time()

        for (classid, score, box) in zip(classes, scores, boxes):
            label = f"{class_name[int(classid)]} : {score:.2f}"
            cv2.rectangle(frame, box, color=(0, 255, 0), thickness=2)
            cv2.putText(frame, label, (box[0], box[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255), 2)

        fps_label = f"FPS: {round(1/(end-start), 2)}"

        cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
        cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Video', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
