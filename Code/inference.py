# Import libraries
from ultralytics import YOLO
import os
import pandas as pd

from audio_processing import save_spectrogram_from_audio

# Load model (Bird Song Detector from BIRDeep)
model = YOLO("Models/Bird Song Detector/weights/best.pt")

# Option 1: Perform detection on an image using the model
audio_path = "Data/Audios/AM1_20230510_073000.WAV"
# Audio has to be converted to spectrogram and saved as image
image_path = save_spectrogram_from_audio(audio_path)

# Option 2: Perform detection on an image using the model
results = model(image_path)

print(results)

print("------------------")

# View results
for r in results:
    print(r)  # print the Probs object containing the detected class probabilities

# # Get predictions on best model
# results = model.predict(
#     source=TEST_TXT, #"Dataset/multispecies.jpeg", # (str, optional) source directory for images or videos
#     save=True, 
#     conf=0.15,
#     # iou=0.2,
#     save_txt = True,  # (bool) save results as .txt file
#     save_conf = True,  # (bool) save results with confidence scores
#     save_crop = False,  # (bool) save cropped images with results

#     show = False,  # (bool) show results if possible
#     show_labels = True,  # (bool) show object labels in plots
#     show_conf = True,  # (bool) show object confidence scores in plots

#     visualize = False,  # (bool) visualize model features
    
    
#     #vid_stride = 1,  # (int) video frame-rate stride
#     #line_width = ,   # (int, optional) line width of the bounding boxes, auto if missing
#     #augment = False,  # (bool) apply image augmentation to prediction sources
#     # agnostic_nms = False,  # (bool) Enables class-agnostic Non-Maximum Suppression (NMS), which merges overlapping boxes of different classes. Useful in multi-class detection scenarios where class overlap is common.
#     #classes = , # (int | list[int], optional) filter results by class, i.e. classes=0, or classes=[0,2,3]
#     #retina_masks = False,  # (bool) use high-resolution segmentation masks
#     #boxes = True  # (bool) Show boxes in segmentation predictions
# )

# # View results
# for r in results:
#     print(r.B)  # print the Probs object containing the detected class probabilities'''