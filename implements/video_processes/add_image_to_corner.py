import cv2

# Read the video from file
cap = cv2.VideoCapture('input.mp4')

# Get the video frames per second (fps)
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the video frame dimensions
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Read the image to be added to the video
img = cv2.imread("logo.png", -1)

# Resize the image to fit in the video frame
img = cv2.resize(img, (frame_height // 5, frame_height // 5),
                 interpolation = cv2.INTER_AREA)

# Get the dimensions of the image
img_height, img_width, _ = img.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        # Add the image to the video frame
        frame[0:img_height, frame_width - img_width:frame_width] = img

        # Write the frame to the output video file
        out.write(frame)
        print("Thêm hình vào video hoàn tất")

        # Display the resulting frame
        # cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("không đọc được dữ liệu video")
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
