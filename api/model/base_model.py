import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.keras.applications.imagenet_utils import decode_predictions

class Model:
    def __init__(self) -> None:
        self._model = None
        self._load_model()

    def _load_model(self) -> None:
        self._model = tf.keras.applications.MobileNetV2(weights="imagenet")
        print("model loaded")

    def _scale_image(self, image: Image.Image):
        image = np.asarray(image.resize((224, 224)))[..., :3]
        image = np.expand_dims(image, 0)
        image = image / 127.5 - 1.0
        return image

    def process(self, image: Image.Image)->np.ndarray:
        return self._scale_image(image)

    def predict(self, image: np.ndarray):
        result = decode_predictions(self._model.predict(image), 2)[0]
        # print(result)
        response = []
        for i, res in enumerate(result):
            resp = {}
            resp["class"] = res[1]
            resp["confidence"] = f"{res[2]*100:0.2f} %"

            response.append(resp)
        
        return response