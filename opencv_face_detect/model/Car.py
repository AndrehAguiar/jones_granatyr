import cv2


class Car:

    def __init__(self, images: dict):
        super(Car, self).__init__()
        self.__cls_car = cv2.CascadeClassifier('cascades\\cars.xml')
        self.__obj = images
        self.__result = {}

    def __detect_car(self, image: list) -> list:
        cars_detected = self.__cls_car.detectMultiScale(self.__obj[image],
                                                        scaleFactor=1.05,
                                                        minNeighbors=5)

        return cars_detected

    def __detect_cars(self):
        print(f"Detecting faces <".ljust(50, '='))
        for image in list(self.__obj.keys()):
            self.__result.setdefault(image, [])

            cars_detected = self.__detect_car(image)

            print(f'Quantidade de relógios identificados {image}: {len(cars_detected)}')

            self.__result[image] = cars_detected

        print("Detection finished <".ljust(50, '='))

    def get_result(self):
        self.__detect_cars()
        return self.__result

    @staticmethod
    def draw_rectangle(detect_cars: list, image) -> list:
        for (x, y, w, h) in detect_cars:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        return image
