from matplotlib import pyplot as plt
import numpy as np


def Q1():
    x = np.linspace(-np.pi, np.pi, 200)
    highpass_list = np.ones(len(x))
    cut_off_freq = int(np.random.random() * (len(highpass_list)/2))
    print(cut_off_freq)
    highpass_list[cut_off_freq:-cut_off_freq] = 0
    # highpass_list[0:cut_off_freq] = 0
    plt.plot(x, highpass_list)
    plt.axvline(x[cut_off_freq - 1], linestyle='--', color='red', label='-w')
    plt.axvline(x[-cut_off_freq], linestyle='--', color='black', label='w')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    Q1()
