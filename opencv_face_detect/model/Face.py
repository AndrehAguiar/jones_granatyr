import cv2


class Face:

    def __init__(self, images: dict):
        super(Face, self).__init__()
        self.__cls_face = cv2.CascadeClassifier('cascades\\haarcascade_frontalface_default.xml')
        self.__obj = images
        self.__result = {}

    def __detect_face(self, image: list) -> list:

        faces_detected = self.__cls_face.detectMultiScale(self.__obj[image],
                                                          scaleFactor=1.01581,
                                                          minNeighbors=47,
                                                          minSize=(30, 30))
        return faces_detected

    def __detect_faces(self):
        print(f"Detecting faces <".ljust(50, '='))
        for image in list(self.__obj.keys()):
            self.__result.setdefault(image, [])

            faces_detected = self.__detect_face(image)

            print(f'Quantidade de faces identificadas {image}: {len(faces_detected)}')

            self.__result[image] = faces_detected

        print("Detection finished <".ljust(50, '='))

    def get_result(self):
        self.__detect_faces()
        return self.__result

    def get_face(self, image):
        return self.__detect_face(image)

    @staticmethod
    def draw_rectangle(detect_faces: list, image) -> list:
        for (x, y, w, h) in detect_faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        return image
