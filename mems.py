# MEMS Vibration Sensor Simulation

This project simulates a simplified MEMS (Micro-Electro-Mechanical Systems) vibration sensor using Python. It is a fun and educational project designed to help understand how sensor signals can be simulated and processed.

## Features
- Generate synthetic vibration signals (sinusoidal)
- Simulate a basic sensor response (gain and delay)
- Visualize both input and output signals

## Files
- `vibration_sensor.py`: Contains the function for simulating sensor output
- `signal_generator.py`: Generates a simple sinusoidal signal
- `plot_results.py`: Plots the input and output signals
- `main`: Executes the simulation

## Getting Started

### Requirements
Install dependencies using pip:
```bash
pip install -r requirements.txt
```

### Run the simulation
```bash
python mems_vibration_sim.py
```

## Requirements File (`requirements.txt`):
```
numpy
matplotlib
```

---

## Main Script

```python
import numpy as np
import matplotlib.pyplot as plt

# --- signal_generator.py ---
def generate_signal(frequency=5, amplitude=1, duration=2, sample_rate=1000):
    t = np.linspace(0, duration, int(sample_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

# --- vibration_sensor.py ---
def simulate_sensor_response(input_signal, gain=1.5, delay=10):
    delayed_signal = np.roll(input_signal, delay)
    output_signal = gain * delayed_signal
    return output_signal

# --- plot_results.py ---
def plot_signals(time, input_signal, output_signal):
    plt.figure(figsize=(10, 4))
    plt.plot(time, input_signal, label='Input Signal')
    plt.plot(time, output_signal, label='Sensor Output', linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('MEMS Vibration Sensor Simulation')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# --- main script ---
if __name__ == "__main__":
    t, input_sig = generate_signal(frequency=5, amplitude=1, duration=2, sample_rate=1000)
    output_sig = simulate_sensor_response(input_sig, gain=2, delay=20)
    plot_signals(t, input_sig, output_sig)
```
