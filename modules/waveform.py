from pydub import AudioSegment
import librosa
import matplotlib.pyplot as plt

def plot_waveform(audio_path):

    # Original audio ni WAV ki convert chestunnam
    audio = AudioSegment.from_file(audio_path)

    # WAV file path create chestunnam
    wav_path = audio_path.rsplit(".", 1)[0] + ".wav"

    # Converted audio ni save chestunnam
    audio.export(wav_path, format="wav")

    # WAV file ni librosa tho load chestunnam
    y, sr = librosa.load(wav_path, sr=None)

    # Waveform plot
    fig, ax = plt.subplots()
    ax.plot(y)

    ax.set_title("Audio Waveform")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")

    return fig
