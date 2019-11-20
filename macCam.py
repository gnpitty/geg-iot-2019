
import sys

def capImageOSX(file):
    import cv2
    cap = cv2.VideoCapture(0)
    while(True):
      ret, frame = cap.read()
      rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

      cv2.imshow('frame', rgb)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite(file, frame)
        break

    cap.release()
    cv2.destroyAllWindows()


if sys.platform == "darwin":
    capImageOSX('capture.jpg')

 