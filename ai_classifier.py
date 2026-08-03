import os
import numpy as np
from PIL import Image, ImageOps
import tf_keras as keras

# Load the trained AI model and label files
MODEL_PATH = "keras_model.h5"
LABELS_PATH = "labels.txt"

# Ensure required model files are present
if not os.path.exists(MODEL_PATH) or not os.path.exists(LABELS_PATH):
    print(f"[ERROR] Required files '{MODEL_PATH}' or '{LABELS_PATH}' not found in the project folder!")
    exit()

# Load model and class labels
model = keras.models.load_model(MODEL_PATH, compile=False)

with open(LABELS_PATH, "r", encoding="utf-8") as file:
    # Remove index numbers and extra spaces, keeping only the class names
    class_names = [line.strip().split(" ", 1)[-1] for line in file.readlines()]
def classify_product(image_path):
    try:
        # Check if the image file exists
        if not os.path.exists(image_path):
            print(f"[ERROR] The file '{image_path}' was not found!")
            return
        # Prepare array for model input (shape: 1, 224, 224, 3)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Open and resize the image to match model input requirements
        image = Image.open(image_path).convert("RGB")
        image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

        # Normalize the image pixel values
        image_array = np.array(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1.0
        data[0] = normalized_image_array

        # Make prediction using the model
        prediction = model.predict(data, verbose=0)
        class_index = np.argmax(prediction)

        # Extract predicted class name and confidence level
        raw_label = class_names[class_index]
        clean_label = raw_label.split(' ', 1)[-1] if raw_label[0].isdigit() else raw_label
        confidence = prediction[0][class_index] * 100

        # Display formatted output
        print("\n" + "=" * 45)
        print("     AI PRODUCT RECOGNITION RESULT      ")
        print("=" * 45)
        print(f" Detected Product : {clean_label.capitalize()}")
        print(f" Confidence Level : {confidence:.2f}%")
        print(" Status           : Successfully Analyzed!")
        print("=" * 45 + "\n")

    except Exception as error:
        print(f"[ERROR] Failed to classify image: {error}")

# ==========================================================
# Run the classifier on any image file (e.g., test.jfif, cheese.jpg)
# ==========================================================
classify_product("test4.avif")  # Replace with your image file name