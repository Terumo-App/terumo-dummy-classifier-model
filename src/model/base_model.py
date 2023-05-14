import tensorflow as tf
from PIL import Image
import numpy as np
import torch
from src.model import Net
from src.process.transformation import get_transform

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

class Model:
    def __init__(self) -> None:
        self._model = None
        self._transform = get_transform()
        self._load_model()

    def _load_model(self) -> None:
        self._model = Net(net_version="b0", num_classes=2).to(DEVICE)
        print("model loaded")


    def process(self, image: Image.Image)->np.ndarray:
        image_processed = self._transform(image)
        image_processed = image_processed.unsqueeze(0)
        return image_processed

    def predict(self, image: np.ndarray):
        self._model.eval()

        with torch.no_grad():
            
            output = self._model(image.to(DEVICE))
            scores = torch.sigmoid(output)
            predictions = (scores>0.5).float()
            _, pred = torch.min(predictions, 1)

        return pred.item()