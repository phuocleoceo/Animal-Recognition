from keras.models import load_model
import numpy as np
import cv2

# Load lại model
label_list = ["Mèo", "Chó", "Bướm", "Gà", "Voi",
              "Nhện", "Bò", "Ngựa", "Sóc", "Cừu"]
model = load_model("animal.h5")


def predict(image: bytes):
    image = read_image(image)
    pred = model.predict([image])[0]
    animal = label_list[np.argmax(pred)]
    return animal


def read_image(file: bytes):
    img_size = 64
    # Convert bytes sang OpenCV nparray
    image = np.asarray(bytearray(file), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # Resize và reshape kích thước ảnh
    image = cv2.resize(image, (img_size, img_size))
    image = image.reshape((img_size, img_size, 3))
    image = np.expand_dims(image, axis=0)
    image = np.array(image, dtype=np.float64)
    # Chuẩn hóa [0,255] về [0,1]
    image /= 255.0
    return image
