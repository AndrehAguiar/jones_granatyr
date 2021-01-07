import cv2
from model.Face import Face


class Cam:
    def __init__(self):
        super(Cam, self).__init__()
        self.__video = cv2.VideoCapture(0)

    def __face_cam(self):
        n = 0
        while True:
            conn, frame = self.__video.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = Face({n: gray_frame})
            detected_faces = face.get_face(n)
            Face.draw_rectangle(detected_faces, frame)

            cv2.imshow("Vídeo", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        self.__video.release()
        cv2.destroyAllWindows()

    def get_cam(self):
        self.__face_cam()
