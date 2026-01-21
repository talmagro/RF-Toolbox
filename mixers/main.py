import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 10e6          # Sampling Frequency (10 MHz)
T = 1e-3           # Signal Duration (1 ms)
t = np.arange(0, T, 1/fs)

f_if = 100e3       # IF = 100 kHz
f_lo = 1e6         # LO = 1 MHz

# Signals
if_signal = np.cos(2 * np.pi * f_if * t)
lo_signal = np.cos(2 * np.pi * f_lo * t)

# Mixer (Multiplication)
mixed_signal = if_signal * lo_signalh

# FFT helper
def compute_fft(signal, fs):
    N = len(signal)
    spectrum = np.fft.fft(signal)
    spectrum = np.fft.fftshift(spectrum)
    freqs = np.fft.fftshift(np.fft.fftfreq(N, 1/fs))
    return freqs, np.abs(spectrum) / N


# FFTs
f_if_fft, IF_fft = compute_fft(if_signal, fs)
f_lo_fft, LO_fft = compute_fft(lo_signal, fs)
f_mix_fft, MIX_fft = compute_fft(mixed_signal, fs)

# Frequency Domain Plot
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(f_if_fft/1e6, IF_fft)
plt.title("IF signal spectrum")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(f_lo_fft/1e6, LO_fft)
plt.title("LO signal spectrum")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(f_mix_fft/1e6, MIX_fft)
plt.title("Mixer output spectrum")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()

# Time Domain Plots
plt.figure(figsize=(12, 8))

plt.subplot(3,1,1)
plt.plot(t*1e6, if_signal)
plt.title("IF signal (time domain)")
plt.xlabel("Time [µs]")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3,1,2)
plt.plot(t*1e6, lo_signal)
plt.title("LO signal (time domain)")
plt.xlabel("Time [µs]")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3,1,3)
plt.plot(t*1e6, mixed_signal)
plt.title("Mixer output (time domain)")
plt.xlabel("Time [µs]")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
