import cv2

from model.Face import Face


class Eye:

    def __init__(self, images: dict):
        super(Eye, self).__init__()
        self.__cls_eye = cv2.CascadeClassifier('cascades\\haarcascade_eye.xml')
        self.__obj = images
        self.__result = {}

    def __detect_eye(self, region):
        eyes_detected = self.__cls_eye.detectMultiScale(region,
                                                        scaleFactor=2.95,
                                                        minNeighbors=5)

        return eyes_detected

    def __detect_eyes(self, images: dict):
        face = Face(self.__obj)
        print(f"Detecting eyes in face <".ljust(50, '='))

        for image in self.__obj.keys():

            faces_deteceted = face.get_face(image)
            face_region = []
            detected = []

            for (x, y, w, h) in faces_deteceted:
                image_face = cv2.rectangle(images[image], (x, y), (x + w, y + h), (0, 255, 0), 2)
                region = image_face[y:y + h, x:x + w]
                region_gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
                eyes_detected = self.__detect_eye(region_gray)
                face_region.append(region)
                detected.append(eyes_detected)

            self.__result[image] = {'region': face_region, "eyes_detected": detected}

            print(f'Quantidade de olhos identificadas {image}: {len(detected)}')

        print("Detection finished <".ljust(50, '='))

    def get_result(self, images: dict) -> dict:
        self.__detect_eyes(images)
        return self.__result

    def get_eye(self, region):
        self.__detect_eye(region)

    @staticmethod
    def draw_rectangle(region: list, detect_eyes: list, image: list) -> list:
        for (x, y, w, h) in detect_eyes:
            cv2.rectangle(region, (x, y), (x + w, y + h), (0, 0, 255), 2)

        return image
