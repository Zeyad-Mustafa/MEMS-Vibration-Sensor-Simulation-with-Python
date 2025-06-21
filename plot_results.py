import matplotlib.pyplot as plt

def plot_signals(time, input_signal, output_signal):
    plt.figure(figsize=(10, 4))
    plt.plot(time, input_signal, label='Input Signal')
    plt.plot(time, output_signal, label='Sensor Output', linestyle='--')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('MEMS Vibration Sensor Simulation')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
