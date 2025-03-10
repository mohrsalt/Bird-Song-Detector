"""
This script performs bird song detection on an audio file by converting the audio to a spectrogram image,
running the Bird Song Detector from BIRDeep project YOLO model to detect bird songs, and then transforming the predictions to time segments.

Workflow:
1. Load the YOLO model for bird song detection.
2. Clean the output folder to ensure no previous results interfere.
3. Convert the input audio file to a spectrogram image.
4. Perform detection on the spectrogram image using the YOLO model.
5. Read the predictions from the output folder.
6. Transform the predictions to time segments and save the results.

Variables:
- model: The YOLO model loaded with pre-trained weights for bird song detection.
- audio_path: Path to the input audio file.
- audio_name: Name of the audio file without the extension.
- image_path: Path to the saved spectrogram image.
- predictions_txt: Path to the text file containing the YOLO model predictions.
"""

# Import libraries
from ultralytics import YOLO
import os
import pandas as pd

from audio_processing import save_spectrogram_from_audio, transform_coordinates_to_seconds, transform_predictions_save_segment

# Load model (Bird Song Detector from BIRDeep)
model = YOLO("Models/Bird Song Detector/weights/best.pt")
# Clean the output folder
import shutil

# Clean the output folder
shutil.rmtree('runs', ignore_errors=True)

# Perform detection on an image using the model
audio_path = "Data/Audios/AM1_20230510_083000.WAV"

audio_name = os.path.basename(audio_path).replace(".WAV", "")
# Audio has to be converted to spectrogram and saved as image
image_path = save_spectrogram_from_audio(audio_path)

model(image_path, save_txt=True, save_conf=True)

# Read txt in the output folder
predictions_txt = f"runs/detect/predict/labels/{audio_name}.txt"

if os.path.exists(predictions_txt):
    # Convert to start_second, end_second, class, confidence score:
    transform_predictions_save_segment(audio_path, predictions_txt)
else:
    print(f"No detections for {audio_path}")