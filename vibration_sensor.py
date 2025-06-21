import numpy as np

def simulate_sensor_response(input_signal, gain=1.5, delay=5):
    # Add delay and amplify the signal
    delayed_signal = np.roll(input_signal, delay)
    output = gain * delayed_signal
    return output
