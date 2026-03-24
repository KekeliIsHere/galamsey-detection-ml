import tensorflow as tf

print("Loading model...")

model = tf.keras.models.load_model("galamsey_detector_model.h5")

print("Model loaded successfully")