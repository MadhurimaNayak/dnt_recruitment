import cv2

input_file = 'input_video.mp4'
output_file = 'output_video.mp4'

cap = cv2.VideoCapture(input_file)

fps = cap.get(cv2.CAP_PROP_FPS)
frame_skip = int(fps * 0.75)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    if cap.get(cv2.CAP_PROP_POS_FRAMES) % frame_skip != 0:
        continue
    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()
