import os
import pandas as pd
from birdnet_analyzer import analyze_audio  # Ensure BirdNET library is installed
from utils import Globals

def classify_segments():
    """Run BirdNET classification on audio segments."""
    model_path, classes_path = Globals.get_default_birdnet_model()
    segments = Globals.detections
    results = []

    for _, segment in segments.iterrows():
        audio_path = segment["Path"]
        analysis = analyze_audio(audio_path, model_path, classes_path)

        for species, score in analysis.items():
            results.append({
                "Path": audio_path,
                "Segment": os.path.basename(audio_path),
                "Classification": species,
                "Confidence": score
            })

    results_df = pd.DataFrame(results)
    Globals.classifications = results_df
    return results_df.to_dict(orient="records")

def classification_interface():
    with gr.Column():
        gr.Markdown("## BirdNET Classifier")
        classify_button = gr.Button("Classify Segments")
        results_table = gr.DataFrame(headers=["Path", "Segment", "Classification", "Confidence"])
        
        classify_button.click(fn=classify_segments, outputs=results_table)
