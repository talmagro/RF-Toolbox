import numpy as np
import matplotlib.pyplot as plt

# Characteristic impedance
Z0 = 50  # ohms

# Frequency range (Hz)
f = np.linspace(1e6, 3e9, 1000)

# Example load: resistor + capacitor (frequency dependent)
R = 75  # ohms
C = 1e-12  # 1 pF

# Load impedance
ZL = R + 1 / (1j * 2 * np.pi * f * C)

# Reflection coefficient (S11)
S11 = (ZL - Z0) / (ZL + Z0)

# Convert to dB
S11_dB = 20 * np.log10(np.abs(S11))

# Plot
plt.figure()
plt.plot(f / 1e9, S11_dB)
plt.xlabel("Frequency (GHz)")
plt.ylabel("|S11| (dB)")
plt.title("Input Reflection (S11)")
plt.grid(True)
plt.show()
