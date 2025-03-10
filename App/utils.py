import os
import pandas as pd

class Globals:
    audio_files = pd.DataFrame()  # Placeholder for loaded audio files
    detections = pd.DataFrame()  # Placeholder for detections
    classifications = pd.DataFrame()  # Placeholder for classifications
    root_audio_dir = None  # Root directory for loaded audio
    spectrogram_dir = os.path.join(os.getcwd(), "Generated_Spectrograms")  # Directory for spectrograms
    models_dir = os.path.join(os.getcwd(), "Models")  # Directory for models

    @staticmethod
    def get_default_bird_song_model():
        """Return the default YOLOv8 bird song detector model path."""
        return os.path.join(Globals.models_dir, "Bird Song Detector", "weights", "best.pt")
    
    @staticmethod
    def get_default_birdnet_model():
        """Return the default BirdNET model and classes."""
        model_path = os.path.join(Globals.models_dir, "BirdNET FineTuned BIRDeep", "model.tflite")
        classes_path = os.path.join(Globals.models_dir, "BirdNET FineTuned BIRDeep", "classes.txt")
        return model_path, classes_path

def segment_audio(folder_path):
    """Segment audio files into 1-minute chunks, with padding for shorter clips."""
    from pydub import AudioSegment
    segmented_files = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".wav"):
                file_path = os.path.join(root, file)
                audio = AudioSegment.from_file(file_path)

                # Ensure 1-minute segments
                duration = len(audio)
                segment_duration = 60 * 1000  # 1 minute in milliseconds
                for i in range(0, duration, segment_duration):
                    segment = audio[i:i + segment_duration]

                    # If segment is less than 1 minute, pad with silence
                    if len(segment) < segment_duration:
                        segment = segment + AudioSegment.silent(duration=segment_duration - len(segment))

                    # Save the segment
                    segment_name = f"{os.path.splitext(file)[0]}_{i // 1000}s_{(i + len(segment)) // 1000}s.wav"
                    segment_path = os.path.join(root, "Segmented", segment_name)
                    os.makedirs(os.path.dirname(segment_path), exist_ok=True)
                    segment.export(segment_path, format="wav")
                    segmented_files.append({"File": segment_name, "Path": segment_path})

    return pd.DataFrame(segmented_files)
