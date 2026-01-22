import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Simulation parameters
# ===============================
fs = 1e6                 # Simulation sample rate (Hz)
dt = 1 / fs
t_end = 0.01              # Simulation time (seconds)
t = np.arange(0, t_end, dt)

# ===============================
# PLL parameters
# ===============================
f_ref = 10e3              # Reference frequency (Hz)
N = 10                    # Divider ratio
f_vco_center = 100e3      # VCO free-running frequency (Hz)
Kvco = 50e3               # VCO gain (Hz / volt)
Kpd = 1.0                 # Phase detector gain

# Loop filter (1st order RC)
R = 1e3
C = 1e-6
alpha = dt / (R * C + dt)

# ===============================
# Signal initialization
# ===============================
ref = np.zeros_like(t)
vco = np.zeros_like(t)
div = np.zeros_like(t)
pd_out = np.zeros_like(t)
lf_out = np.zeros_like(t)

# Internal states
vco_phase = 0.0
div_counter = 0
vco_freq = f_vco_center

# ===============================
# Generate reference square wave
# ===============================
ref = np.sign(np.sin(2 * np.pi * f_ref * t))

# ===============================
# Main simulation loop
# ===============================
for i in range(1, len(t)):

    # --- VCO ---
    vco_freq = f_vco_center + Kvco * lf_out[i-1]
    vco_phase += 2 * np.pi * vco_freq * dt
    vco[i] = np.sign(np.sin(vco_phase))

    # --- Frequency divider ---
    if vco[i] > 0 and vco[i-1] <= 0:  # Rising edge detect
        div_counter += 1
        if div_counter >= N:
            div_counter = 0
            div[i] = 1
        else:
            div[i] = -1
    else:
        div[i] = div[i-1]

    # --- Phase detector (XOR for square waves) ---
    pd_out[i] = Kpd * (ref[i] != div[i])

    # --- Loop filter (RC low-pass) ---
    lf_out[i] = lf_out[i-1] + alpha * (pd_out[i] - lf_out[i-1])

# ===============================
# Plot results
# ===============================
plt.figure(figsize=(12, 10))

plt.subplot(5, 1, 1)
plt.plot(t, ref)
plt.title("Reference Signal")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(5, 1, 2)
plt.plot(t, div)
plt.title("Divider Output")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(5, 1, 3)
plt.plot(t, pd_out)
plt.title("Phase Detector Output")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(5, 1, 4)
plt.plot(t, lf_out)
plt.title("Loop Filter Output (VCO Control Voltage)")
plt.ylabel("Volts")
plt.grid()

plt.subplot(5, 1, 5)
plt.plot(t, vco)
plt.title("VCO Output")
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")
plt.grid()

plt.tight_layout()
plt.show()
