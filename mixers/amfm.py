import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Parameters
# ============================================================

fs = 200_000            # Sampling frequency (Hz)
t = np.arange(0, 0.02, 1/fs)   # Time vector (20 ms)

fm = 500                # Message frequency (Hz)
fc = 20_000             # Carrier frequency (Hz)

# ============================================================
# Message (baseband) signal
# ============================================================

message = np.cos(2 * np.pi * fm * t)

# ============================================================
# AM Modulation
# ============================================================

am_index = 0.7          # Modulation index (0 < m <= 1 for no distortion)
am_signal = (1 + am_index * message) * np.cos(2 * np.pi * fc * t)

# ============================================================
# FM Modulation
# ============================================================

freq_dev = 3_000        # Frequency deviation (Hz)

# Integral of message for FM phase
integral_message = np.cumsum(message) / fs

fm_signal = np.cos(
    2 * np.pi * fc * t +
    2 * np.pi * freq_dev * integral_message
)

# ============================================================
# Time Domain Plots
# ============================================================

plt.figure()

plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title("Message Signal – Time Domain")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, am_signal)
plt.title("AM Signal – Time Domain")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, fm_signal)
plt.title("FM Signal – Time Domain")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# ============================================================
# Frequency Domain (FFT)
# ============================================================

def plot_fft(signal, fs, title):
    N = len(signal)
    fft_vals = np.fft.fft(signal)
    fft_vals = fft_vals / N                   # Normalize
    freqs = np.fft.fftfreq(N, 1/fs)

    plt.figure()
    plt.plot(freqs[:N//2], np.abs(fft_vals[:N//2]))
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.show()

plot_fft(am_signal, fs, "AM Signal - Frequency Domain")
plot_fft(fm_signal, fs, "FM Signal - Frequency Domain")
