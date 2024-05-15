import librosa
import soundfile as sf
from scipy import signal

def load_file(file):
    y, sr = librosa.load(file)
    return y, sr

def shift_pitch(y, sr=1, n_steps=None):
    shifted_file = librosa.effects.pitch_shift(y, sr, n_steps)
    sf.write("pitch_shifted.wav", shifted_file, sr)

def trim(y, sr, top_db):
    a = int(top_db)
    yt, index = librosa.effects.trim(y, top_db=a)
    sf.write("short.wav", yt, sr)

def f_high(y, sr):
    b,a = signal.butter(10, 2000/(sr/2), btype='highpass')
    yf = signal.lfilter(b,a,y)
    sf.write('filtered_high.wav', yf, sr)

def f_low(y, sr):
    b,a = signal.butter(10, 0.9, btype='lowpass')
    yf = signal.lfilter(b,a,y)
    sf.write('filtered_low.wav', yf, sr)