# Phase-Locked Loop (PLL) Architecture

A Phase-Locked Loop (PLL) is a closed-loop control system that synchronizes the phase and frequency of a locally generated signal (VCO) with a stable reference signal.

## High-Level Block Diagram

```
          ┌──────────┐
          │ Reference│
          │ Oscillator
          └─────┬────┘
                │
                ▼
        ┌────────────────┐
        │ Phase Detector │◄──────────────┐
        │ (PD / PFD)     │               │
        └─────┬──────────┘               │
              │                          │
              ▼                          │
        ┌────────────────┐               │
        │ Gain / Charge  │               │
        │ Pump (Kpd)     │               │
        └─────┬──────────┘               │
              │                          │
              ▼                          │
        ┌────────────────┐               │
        │ Loop Filter    │               │
        │ (LPF)          │               │
        └─────┬──────────┘               │
              │                          │
              ▼                          │
        ┌────────────────┐               │
        │ VCO / NCO      │               │
        │ (Kvco)         │               │
        └─────┬──────────┘               │
              │                          │
              ▼                          │
        ┌────────────────┐               │
        │ Frequency      │               │
        │ Divider (÷N)   │               │
        └─────┬──────────┘               │
              │                          │
              └──────────────────────────┘
```

## Functional Blocks

### 1. Reference Oscillator
Provides a stable frequency reference, typically a crystal oscillator.

- Output: square or sine wave
- Frequency: `f_ref`
- Stability dominates PLL accuracy

### 2. Phase Detector (PD) / Phase-Frequency Detector (PFD)
Compares the phase (and optionally frequency) of the reference signal and the divided VCO output.

Common types:
- XOR phase detector
- PFD with charge pump

### 3. Gain / Charge Pump
Converts the phase detector output into a control signal.

- Gain: `Kpd`
- Produces voltage or current proportional to phase error

### 4. Loop Filter
Filters the detector output and defines loop dynamics.

- Removes high-frequency components
- Sets loop bandwidth and stability

### 5. Voltage-Controlled Oscillator (VCO)
Generates the output frequency controlled by the loop filter voltage.

```
f_vco(t) = f_center + Kvco · V_control(t)
```

### 6. Frequency Divider (÷N)
Divides the VCO output frequency before comparison.

```
f_out = N · f_ref
```

## Closed-Loop Operation

When locked:
- Reference phase ≈ divided VCO phase
- Output frequency is stable
- Phase error is near zero

## Key PLL Parameters

| Parameter | Description |
|----------|-------------|
| f_ref | Reference frequency |
| N | Divider ratio |
| Kvco | VCO gain |
| Kpd | Phase detector gain |
| Loop BW | Loop bandwidth |
| Phase Margin | Stability metric |
