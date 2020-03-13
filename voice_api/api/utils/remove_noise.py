'''import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa
import IPython.display as ipd
import librosa.display
import noisereduce as nr

def fftnoise(f):
    f = np.array(f, dtype="complex")
    Np = (len(f) - 1) // 2
    phases = np.random.rand(Np) * 2 * np.pi
    phases = np.cos(phases) + 1j * np.sin(phases)
    f[1 : Np + 1] *= phases
    f[-1 : -1 - Np : -1] = np.conj(f[1 : Np + 1])
    return np.fft.ifft(f).real

def band_limited_noise(min_freq, max_freq, samples=1024, samplerate=1):
    freqs = np.abs(np.fft.fftfreq(samples, 1 / samplerate))
    f = np.zeros(samples)
    f[np.logical_and(freqs >= min_freq, freqs <= max_freq)] = 1
    return fftnoise(f)

print ('start')
#read audio

rate, data = wavfile.read('output1.mp3')
data = data / 32768

print(data)
print(rate)


#audio visualization 
%matplotlib inline
plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)

#Remoove noise 
# select section of data that is noise
noise_len = 2 # seconds
noise = band_limited_noise(min_freq=4000, max_freq = 12000, samples=len(data), samplerate=rate)*10
noise_clip = noise[:rate*noise_len]


# perform noise reduction
reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=noise_clip, verbose=True)

print ('reduce ')
print (reduced_noise)

#diaplay audio

print ('after remove ')
temp = ipd.Audio(reduced_noise, rate=24000)
librosa.output.write_wav('audio.mp3', reduced_noise, 24000)
'''

#!pip install noisereduce 
import IPython
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa
import IPython.display as ipd
import librosa.display
import noisereduce as nr
# convert audio to flac format
from pydub import AudioSegment

def fftnoise(f):
    f = np.array(f, dtype="complex")
    Np = (len(f) - 1) // 2
    phases = np.random.rand(Np) * 2 * np.pi
    phases = np.cos(phases) + 1j * np.sin(phases)
    f[1 : Np + 1] *= phases
    f[-1 : -1 - Np : -1] = np.conj(f[1 : Np + 1])
    return np.fft.ifft(f).real

def band_limited_noise(min_freq, max_freq, samples=1024, samplerate=1):
    freqs = np.abs(np.fft.fftfreq(samples, 1 / samplerate))
    f = np.zeros(samples)
    f[np.logical_and(freqs >= min_freq, freqs <= max_freq)] = 1
    return fftnoise(f)

def remove_noise_function(file_name):
    #read audio
    data, sr = librosa.load(f'{ file_name }.wav')

    #Remoove noise 
    # select section of data that is noise
    noise_len = 2 # seconds
    noise = band_limited_noise(min_freq=4000, max_freq = 12000, samples=len(data), samplerate=sr)*10
    noise_clip = noise[:sr*noise_len]
    # perform noise reduction

    reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=noise_clip, verbose=True)
    
    #diaplay audio

    print ('after remove ')

    t=ipd.Audio(reduced_noise, rate=sr)
    librosa.output.write_wav(f'{ file_name }.wav', reduced_noise, sr)
    # changing format from wav to flac 
    wav_audio = AudioSegment.from_file(f"{ file_name }.wav", format="wav")
    wav_audio.export(f"{ file_name }.flac", format="flac")
