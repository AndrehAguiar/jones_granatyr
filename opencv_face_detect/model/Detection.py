import cv2
import os

from model.Clock import Clock
from model.Cat import Cat
from model.Car import Car
from model.Face import Face
from model.Eye import Eye
from model.Cam import Cam


class Detection:

    def __init__(self, path: str = 'images'):
        super(Detection, self).__init__()

        self.__path = path + '\\'
        self.__dct_images = {}
        self.__dct_im_gray = {}
        self.__face = None
        self.__eye = None
        self.__cam = None
        self.__cat = None
        self.__clock = None
        self.__car = None
        self.__load_data()

    def __load_data(self):
        """
        Percorre a pasta path e lê cada arquivo jpg
        :return:
        """
        for i, filename in enumerate(os.listdir(self.__path)):
            if filename.endswith('.jpg'):
                self.__dct_images[filename] = cv2.imread(f'{self.__path + filename}')
                self.__dct_im_gray[filename] = cv2.cvtColor(self.__dct_images[filename], cv2.COLOR_BGR2GRAY)

    def get_faces(self) -> dict:
        faces = {}
        self.__face = Face(self.__dct_im_gray)
        result = self.__face.get_result()

        for image in list(result.keys()):
            faces.setdefault(image, [])
            faces[image] = self.__face.draw_rectangle(result[image], self.__dct_images[image])

        return faces

    def get_eyes(self) -> dict:
        eyes = {}
        self.__eye = Eye(self.__dct_im_gray)
        result = self.__eye.get_result(self.__dct_images)
        for image in list(result.keys()):
            for region in result[image]["region"]:
                for eye in result[image]["eyes_detected"]:
                    eyes[image] = self.__eye.draw_rectangle(region, eye, self.__dct_images[image])

        return eyes

    def get_cam_face(self):
        self.__cam = Cam()
        self.__cam.get_cam()

    def get_cats(self):
        cats = {}
        self.__cat = Cat(self.__dct_im_gray)
        result = self.__cat.get_result()

        for image in list(result.keys()):
            cats.setdefault(image, [])
            cats[image] = self.__cat.draw_rectangle(result[image], self.__dct_images[image])

        return cats

    def get_clocks(self):
        clocks = {}
        self.__clock = Clock(self.__dct_im_gray)
        result = self.__clock.get_result()

        for image in list(result.keys()):
            clocks.setdefault(image, [])
            clocks[image] = self.__clock.draw_rectangle(result[image], self.__dct_images[image])

        return clocks

    def get_cars(self):
        cars = {}
        self.__car = Car(self.__dct_im_gray)
        result = self.__car.get_result()

        for image in list(result.keys()):
            cars.setdefault(image, [])
            cars[image] = self.__car.draw_rectangle(result[image], self.__dct_images[image])

        return cars
