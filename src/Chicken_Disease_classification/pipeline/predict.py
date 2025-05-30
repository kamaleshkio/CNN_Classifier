import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredicationPipline:
    def __init__(self, filename):
        pass
        self.filename = filename

    def predict(self):
        # Load the model
        model = load_model(os.path.join("artifacts", "training", "model.keras"))

        # Load and preprocess the image

        imagename = self.filename

        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        # Get the class labels from the model

        if result[0] == 1:
            prediction = "Healthy"
            return[{"image": prediction}]
        
        else:
            prediction = "cocidiosis"
            return[{"image": prediction}]