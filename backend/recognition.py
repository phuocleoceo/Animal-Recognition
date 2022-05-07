from keras.models import load_model
import numpy as np
import base64
import cv2

# Load lại model
label_list = ["Mèo", "Chó", "Bướm", "Gà", "Voi",
              "Nhện", "Bò", "Ngựa", "Sóc", "Cừu"]
model = load_model("animal.h5")


def predict(image: str):
    image = read_image(image)
    pred = model.predict([image])[0]
    # Nhãn dự đoán
    animal = label_list[np.argmax(pred)]
    # Độ tin cậy, làm tròn 2 chữ số
    confidence = round(np.max(pred)*100, 2)
    return animal, confidence


def read_image(file: str):
    img_size = 64
    # base64 to cv2 array
    encoded_data = file.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Resize và reshape kích thước ảnh
    image = cv2.resize(image, (img_size, img_size))
    image = image.reshape((img_size, img_size, 3))
    image = np.expand_dims(image, axis=0)
    image = np.array(image, dtype=np.float64)
    # Chuẩn hóa [0,255] về [0,1]
    image /= 255.0
    return image
