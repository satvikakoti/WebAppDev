import cv2
import numpy as np


class VideoCam(object):

    def get_frame(self):
        cap = cv2.VideoCapture(0)  # capturing video from webcam by creating a video capture object
        # cap = cv2.VideoCapture("F:\\Personal Documents\\Y2019-family-pics-video\\Mussorie\\VID20191226172802.mp4")

        while True:  # infinite loop
            ret, frame = cap.read()  # ret is true/false based on whether there was something to be read

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('frame', frame)
            cv2.imshow('gray', gray)

            k = cv2.waitKey(1) & 0xFF  # 0xFF is 11111111 in binary. Doing & makes sure we only get 8 bits

            jpeg = cv2.imencode('.jpg', gray)
            if k == 27:  # 27 is the value for esc
                break  # break out of the infinite loop

        cv2.destroyAllWindows()
        cap.release()
        return jpeg.tostring()


# VideoCam.get_frame(self)