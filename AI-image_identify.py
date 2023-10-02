# 导入必要的库
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 下载并加载预训练的模型（例如，MobileNetV2）
model = keras.applications.MobileNetV2(weights="imagenet")

# 定义一个函数来识别物品
def recognize_item(image_path):
    # 加载图像并进行预处理
    img = keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = keras.applications.mobilenet_v2.preprocess_input(img_array)

    # 使用模型进行预测
    predictions = model.predict(img_array)
    decoded_predictions = keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]

    # 返回识别结果
    item_name, confidence = decoded_predictions[0]
    return item_name, confidence

# 测试识别功能
image_path = "path_to_your_image.jpg"  # 替换为你的图像路径
item_name, confidence = recognize_item(image_path)
print(f"识别结果：{item_name}，置信度：{confidence:.2f}")
