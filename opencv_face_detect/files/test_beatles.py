import cv2

cls = cv2.CascadeClassifier('cascades\haarcascade_frontalface_default.xml')

image = cv2.imread('images\\beatles.jpg')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detectFaces = cls.detectMultiScale(imageGray)
print(f'Quantidade de faces identificadas: {len(detectFaces)}')
print([f'Posição da face {i+1} [x, y, w, h]: {face}' for i, face in enumerate(detectFaces)])

for (x, y, w, h) in detectFaces:
    print(x, y, w, h)
    # x = face_width start
    # y = face_hegth start
    # w = face_with end
    # y = face_heigth end
    # .rectangle(image, (w face_start, h face_start), (x + w = w face_end, y + h = h face_end), (r, g, b), (edge width))
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)
    
cv2.imshow('Detected Faces', image)
cv2.waitKey()
