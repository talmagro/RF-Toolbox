import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Parameters
# ============================================================

fs = 200_000          # Sampling frequency (Hz)
Tb = 1e-3             # Bit duration (1 ms)
fc = 20_000           # Carrier frequency (Hz)

bits = np.array([1, 0, 1, 1, 0, 0, 1, 0])  # Example data
N = int(Tb * fs)      # Samples per bit
t = np.arange(0, len(bits) * Tb, 1/fs)

# ============================================================
# Baseband NRZ signal
# ============================================================

baseband = np.repeat(bits, N)

# ============================================================
# ASK (Amplitude Shift Keying)
# ============================================================

A1 = 1.0
A0 = 0.2

ask_signal = (A0 + (A1 - A0) * baseband) * np.cos(2 * np.pi * fc * t)

# ============================================================
# FSK (Frequency Shift Keying)
# ============================================================

f1 = fc + 2_000
f0 = fc - 2_000

fsk_signal = np.cos(2 * np.pi * np.where(baseband == 1, f1, f0) * t)

# ============================================================
# PSK (BPSK)
# ============================================================

psk_signal = np.cos(2 * np.pi * fc * t + np.pi * (1 - baseband))

# ============================================================
# Time Domain Plot
# ============================================================

plt.figure(figsize=(10, 8))
plt.suptitle("ASK vs FSK vs PSK – Time Domain")

# ------------------------------------------------------------
# Baseband
# ------------------------------------------------------------
plt.subplot(4, 1, 1)
plt.plot(t, baseband, color="black", label="Baseband Signal")
plt.legend(loc="upper right")
plt.ylabel("Amplitude")
plt.grid(True)

# ------------------------------------------------------------
# ASK
# ------------------------------------------------------------
plt.subplot(4, 1, 2)
plt.plot(t, ask_signal, color="tab:blue", label="ASK")
plt.legend(loc="upper right")
plt.ylabel("Amplitude")
plt.grid(True)

# ------------------------------------------------------------
# FSK
# ------------------------------------------------------------
plt.subplot(4, 1, 3)
plt.plot(t, fsk_signal, color="tab:orange", label="FSK")
plt.legend(loc="upper right")
plt.ylabel("Amplitude")
plt.grid(True)

# ------------------------------------------------------------
# PSK
# ------------------------------------------------------------
plt.subplot(4, 1, 4)
plt.plot(t, psk_signal, color="tab:green", label="PSK")
plt.legend(loc="upper right")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# ============================================================
# Frequency Domain (FFT)
# ============================================================

def compute_fft(signal, fs):
    N = len(signal)
    fft_vals = np.fft.fft(signal) / N
    freqs = np.fft.fftfreq(N, 1/fs)
    return freqs[:N//2], np.abs(fft_vals[:N//2])

freqs_ask, mag_ask = compute_fft(ask_signal, fs)
freqs_fsk, mag_fsk = compute_fft(fsk_signal, fs)
freqs_psk, mag_psk = compute_fft(psk_signal, fs)

plt.figure()
plt.plot(freqs_ask, mag_ask, label="ASK Spectrum")
plt.plot(freqs_fsk, mag_fsk, label="FSK Spectrum", alpha=0.8)
plt.plot(freqs_psk, mag_psk, label="PSK Spectrum", alpha=0.8)
plt.title("ASK vs FSK vs PSK – Frequency Domain")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)
plt.show()
