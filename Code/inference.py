# Import libraries
from ultralytics import YOLO
import os
import pandas as pd

from audio_processing import save_spectrogram_from_audio, transform_coordinates_to_seconds, transform_predictions_save_segment

# Load model (Bird Song Detector from BIRDeep)
model = YOLO("Models/Bird Song Detector/weights/best.pt")
# Clean the output folder
os.system("rm -rf runs/*")

# Perform detection on an image using the model
audio_path = "Data/Audios/AM1_20230510_083000.WAV"

audio_name = os.path.basename(audio_path).replace(".WAV", "")
# Audio has to be converted to spectrogram and saved as image
image_path = save_spectrogram_from_audio(audio_path)

model(image_path, save_txt=True, save_conf=True)

# Read txt in the output folder
predictions_txt = f"runs/detect/predict/labels/{audio_name}.txt"

# Convert to start_second, end_second, class, confidence score:
transform_predictions_save_segment(audio_path, predictions_txt)
transform_predictions_save_segment(audio_path, predictions_txt)