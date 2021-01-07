import cv2


class Banana:

    def __init__(self, images: dict):
        super(Banana, self).__init__()
        self.__cls_banana = cv2.CascadeClassifier('cascades\\banana_classifier.xml')
        self.__obj = images
        self.__result = {}

    def __detect_banana(self, image: list) -> list:
        cars_detected = self.__cls_banana.detectMultiScale(self.__obj[image],
                                                           scaleFactor=1.1,
                                                           minNeighbors=3)

        return cars_detected

    def __detect_bananas(self):
        print(f"Detecting faces <".ljust(50, '='))
        for image in list(self.__obj.keys()):
            self.__result.setdefault(image, [])

            bananas_detected = self.__detect_banana(image)

            print(f'Quantidade de relógios identificados {image}: {len(bananas_detected)}')

            self.__result[image] = bananas_detected

        print("Detection finished <".ljust(50, '='))

    def get_result(self):
        self.__detect_bananas()
        return self.__result

    @staticmethod
    def draw_rectangle(detect_bananas: list, image) -> list:
        for (x, y, w, h) in detect_bananas:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        return image
