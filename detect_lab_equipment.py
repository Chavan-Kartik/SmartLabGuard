from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  

required_classes = ["keyboard", "mouse", "monitor"]
required_counts = {"keyboard": 5, "mouse": 5}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run object detection
    results = model(frame, stream=True)

    detected_counts = {"keyboard": 0, "mouse": 0}
    
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]
            # Draw bounding box and label
            if class_name in required_classes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, class_name, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
                
                if class_name in detected_counts:
                    detected_counts[class_name] += 1

    # Check if all objects are present(compare)
    missing_msgs = []
    for obj in required_counts:
        if detected_counts[obj] < required_counts[obj]:
            missing_msgs.append(f"{obj.capitalize()} missing: {required_counts[obj] - detected_counts[obj]}")
#status
    if missing_msgs:
        for idx, msg in enumerate(missing_msgs):
            cv2.putText(frame, msg, (10, 30 + idx*30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "All OK", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Lab Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
