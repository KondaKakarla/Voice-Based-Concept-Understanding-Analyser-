import librosa
import matplotlib.pyplot as plt


def plot_waveform(audio_path):

    # Load audio
    y, sr = librosa.load(audio_path, sr=None)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 3))

    # Plot waveform
    ax.plot(y, color="blue")

    ax.set_title("Audio Waveform")
    ax.set_xlabel("Samples")
    ax.set_ylabel("Amplitude")

    plt.tight_layout()

    return fig