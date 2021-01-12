from model.Detection import Detection
import cv2

#detect = Detection()

"""
marked_imgs = detect.get_faces()
for image in list(marked_imgs.keys()):
    print(f"Result faces: {image} <".ljust(50, '#'))
    cv2.imshow(image, marked_imgs[image])
    cv2.waitKey()
"""
"""
marked_imgs = detect.get_eyes()
for image in list(marked_imgs.keys()):
    print(f"Result eyes in faces: {image} <".ljust(50, '#'))
    cv2.imshow(image, marked_imgs[image])
    cv2.waitKey()
"""

# detect.get_cam_face()

detect = Detection(path='outros')
"""
marked_imgs = detect.get_cats()
for image in list(marked_imgs.keys()):
    print(f"Result cats: {image} <".ljust(50, '#'))
    cv2.imshow(image, marked_imgs[image])
    cv2.waitKey()
"""
"""
marked_imgs = detect.get_clocks()
for image in list(marked_imgs.keys()):
    print(f"Result cats: {image} <".ljust(50, '#'))
    cv2.imshow(image, marked_imgs[image])
    cv2.waitKey()
"""
"""
marked_imgs = detect.get_cars()
for image in list(marked_imgs.keys()):
    print(f"Result cats: {image} <".ljust(50, '#'))
    cv2.imshow(image, marked_imgs[image])
    cv2.waitKey()
"""
# https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

marked_imgs = detect.get_bananas()
for image in list(marked_imgs.keys()):
    print(f"Result cats: {image} <".ljust(50, '#'))
    cv2.imshow(image, marked_imgs[image])
    cv2.waitKey()
