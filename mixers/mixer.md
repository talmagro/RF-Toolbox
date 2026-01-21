## Mixer Theory

An ideal RF mixer is simply a multiplier in the time domain. The direct consequence is that, in the frequency domain, new spectral components appear at the sum and difference of the original frequencies.

Assume:

- IF (Intermediate Frequency, or baseband) signal:

```math
x(t) = \cos(2\pi f_{IF} t)
```

- Local Oscillator (LO):

```math
y(t) = \cos(2\pi f_{LO} t)
```

The mixer output is the multiplication of both signals:

```math
z(t) = x(t)\cdot y(t)
```

Using the trigonometric identity:

```math
\cos A \cdot \cos B = \frac{1}{2}\left[\cos(A+B) + \cos(A-B)\right]
```

we obtain:

```math
z(t) = \frac{1}{2}
\left[
\cos\left(2\pi(f_{LO}+f_{IF})t\right) +
\cos\left(2\pi(f_{LO}-f_{IF})t\right)
\right]
```

### Frequency-domain interpretation

In the spectrum of the mixed signal, two main components appear:

- **Sum component**:

```math
f_{\text{sum}} = f_{LO} + f_{IF}
```

- **Difference component**:

```math
f_{\text{diff}} = |f_{LO} - f_{IF}|
```

These two components form the basis of:
- Upconverters  
- Downconverters  
- RF mixers in general  

In practical systems, a filter after the mixer is used to select the desired component and reject the unwanted one.
