import cv2

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    dilated = cv2.dilate(thresh, None, iterations=3)

    contours, _ = cv2.findContours(
        dilated,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    motion = False

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue

        motion = True

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            frame1,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    if motion:
        cv2.putText(
            frame1,
            "Motion Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )
    else:
        cv2.putText(
            frame1,
            "No Motion",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    cv2.imshow("Real-Time Motion Detection", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        break

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()