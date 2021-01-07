import cv2


class Clock:

    def __init__(self, images: dict):
        super(Clock, self).__init__()
        self.__cls_clock = cv2.CascadeClassifier('cascades\\relogios.xml')
        self.__obj = images
        self.__result = {}

    def __detect_clock(self, image: list) -> list:
        clocks_detected = self.__cls_clock.detectMultiScale(self.__obj[image],
                                                            scaleFactor=1.01,
                                                            minNeighbors=3)

        return clocks_detected

    def __detect_clocks(self):
        print(f"Detecting faces <".ljust(50, '='))
        for image in list(self.__obj.keys()):
            self.__result.setdefault(image, [])

            clocks_detected = self.__detect_clock(image)

            print(f'Quantidade de relógios identificados {image}: {len(clocks_detected)}')

            self.__result[image] = clocks_detected

        print("Detection finished <".ljust(50, '='))

    def get_result(self):
        self.__detect_clocks()
        return self.__result

    @staticmethod
    def draw_rectangle(detect_clocks: list, image) -> list:
        for (x, y, w, h) in detect_clocks:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        return image
