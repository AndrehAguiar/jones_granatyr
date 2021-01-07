import cv2


class Cat:

    def __init__(self, images: dict):
        super(Cat, self).__init__()
        self.__cls_cat = cv2.CascadeClassifier('cascades\\haarcascade_frontalcatface.xml')
        self.__obj = images
        self.__result = {}

    def __detect_cat(self, image: list) -> list:
        cats_detected = self.__cls_cat.detectMultiScale(self.__obj[image],
                                                        scaleFactor=1.15,
                                                        minNeighbors=4)

        return cats_detected

    def __detect_cats(self):
        print(f"Detecting faces <".ljust(50, '='))
        for image in list(self.__obj.keys()):
            self.__result.setdefault(image, [])

            cats_detected = self.__detect_cat(image)

            print(f'Quantidade de gatos identificados {image}: {len(cats_detected)}')

            self.__result[image] = cats_detected

        print("Detection finished <".ljust(50, '='))

    def get_result(self):
        self.__detect_cats()
        return self.__result

    @staticmethod
    def draw_rectangle(detect_cats: list, image) -> list:
        for (x, y, w, h) in detect_cats:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        return image
