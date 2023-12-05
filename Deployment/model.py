import streamlit as st
import requests
from PIL import Image
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('model1.h5') 
class_names = ['cats', 'dogs']

def preprocess_image(image):
    img = image.resize((224, 224))
    img_array = np.asarray(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_class(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    predicted_class_index = np.argmax(predictions)
    predicted_class = class_names[predicted_class_index]
    return predicted_class

def run():
    st.title('Image Prediction from URL')
    st.write('It can predict image Cat and Dog')
    image_url = st.text_input("Enter Image URL:")
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                image = Image.open(response.raw)
                st.image(image, caption='Image from URL', use_column_width=True)
                if st.button('Predict'):
                    predicted_class = predict_class(image)
                    st.write(f'Predicted class: {predicted_class}')
            else:
                st.write("Unable to fetch image from URL.")
        except Exception as e:
            st.write(f"Error occurred: {e}")

if __name__ == '__main__':
    run()