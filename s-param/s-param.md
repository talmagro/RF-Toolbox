## S-Parameters

In RF, we don’t like talking about voltages and currents directly because:

- Signals are high frequency and measuring V/I accurately is hard at GHz
- Circuits are often distributed (transmission lines, not lumped parts)

Microwave theory models devices and circuits by parameters that can be obtained through the measurement of power quantities (easier to measure). These parameters are called S-parameters.

So instead, we think in terms of waves:

- A wave goes into a circuit
- A wave comes back (reflected) or goes out another port

S-parameters describe how waves scatter through a network.

## What problem do S-parameters solve?

They tell you:
- How much signal is reflected
- How much is transmitted
- How much is lost
- How ports interact as a function of frequency

They are:

- Frequency-dependent
- Easy to measure with a VNA (Vector Network Analyzer)
- Perfect for RF/microwave systems

## One-port case (S11): the most important one

Imagine this:

S11 = reflection coefficient
- S11 = 0 → perfect match (nothing reflected)
- |S11| = 1 → total reflection
- Usually shown in dB

Examples:
- Antennas, Filters, Amplifier inputs

If you’ve heard of Return Loss or VSWR, they all come from S11.

## Two-port network (most RF blocks)

![2 Port Networks](https://cdn.rohde-schwarz.com/image/products/test-and-measurement/essentials-test-equipment/understanding-s-parameters-article-essentials-infographic-rohde-schwarz_200_107022_3.svg)

| Parameter | Meaning                                  |
| --------- | ---------------------------------------- |
| **S11**   | Input match/reflection (Return Loss)     |
| **S21**   | Forward transmission (gain or loss)      |
| **S12**   | Reverse transmission (Reverse Isolation) |
| **S22**   | Output match/reflection (Return Loss)    |

Typical interpretations:

- S21 → gain of an amplifier or insertion loss of a filter
- S11 / S22 → how well ports are matched
- S12 → isolation / reverse coupling

## Why RF engineers love S-parameters

Because they:
- Work naturally with 50 Ω systems
- Are easy to cascade
- Are measured directly, not calculated indirectly
- Scale cleanly with frequency

That’s why almost every RF datasheet is just S-parameters.

### Mental model to remember forever

S11 → “How much comes back?”
S21 → “How much gets through?”
S22 → “Is the output happy?”
S12 → “Does it leak backwards?”