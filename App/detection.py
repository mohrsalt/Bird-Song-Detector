import os
import pandas as pd
from utils import Globals

def detect_bird_songs():
    """Run YOLO detection on the spectrograms."""
    from ultralytics import YOLO  # Ensure ultralytics is installed

    # Load default or custom YOLO model
    model_path = Globals.get_default_bird_song_model()
    model = YOLO(model_path)

    detections = []
    for spectrogram in os.listdir(Globals.spectrogram_dir):
        if spectrogram.endswith(".png"):
            image_path = os.path.join(Globals.spectrogram_dir, spectrogram)
            results = model(image_path)  # Run YOLO model

            for result in results.xywhn[0].tolist():
                xc, yc, w, h, conf = result
                detections.append({
                    "Path": image_path,
                    "Filename": spectrogram,
                    "Class": 0,  # Fixed as "Bird"
                    "x_center": xc, "y_center": yc,
                    "width": w, "height": h,
                    "Confidence": conf
                })

    detections_df = pd.DataFrame(detections)
    Globals.detections = detections_df
    return detections_df.to_dict(orient="records")

def detection_interface():
    with gr.Column():
        gr.Markdown("## Bird Song Detection")
        detect_button = gr.Button("Detect Bird Songs")
        detections_table = gr.DataFrame(headers=["Path", "Filename", "Class", "x_center", "y_center", "width", "height", "Confidence"])
        
        detect_button.click(fn=detect_bird_songs, outputs=detections_table)
