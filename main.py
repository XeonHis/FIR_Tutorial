from matplotlib import pyplot as plt
import numpy as np


def swap(input_list):
    length = len(input_list)
    temp_list = []
    temp_list[:int(length / 2)] = input_list[int(length / 2):]
    temp_list[int(length / 2):] = input_list[:int(length / 2)]
    return temp_list


def Q1():
    x = np.linspace(-np.pi, np.pi, 200)
    highpass_list = np.ones(len(x))
    # cut_off_freq = int(np.random.random() * (len(highpass_list) / 2))
    cut_off_freq = 50
    # print(cut_off_freq)
    highpass_list[cut_off_freq:-cut_off_freq] = 0

    # plt.plot(x, highpass_list)
    # plt.axvline(x[cut_off_freq - 1], linestyle='--', color='red', label='-w')
    # plt.axvline(x[-cut_off_freq], linestyle='--', color='black', label='w')
    # plt.xlabel('Frequency')
    # plt.ylabel('Amplitude')
    # plt.legend()
    # plt.show()

    return x, highpass_list


def Q3(x_data, y_data):
    inner_x = x_data
    h = np.real(np.fft.ifft(y_data))
    h = swap(h)

    h_blackwindow = h.copy()
    h_blackwindow = h_blackwindow * np.blackman(len(h_blackwindow))

    h_recwindow = h.copy()
    h_recwindow = h_recwindow * np.bartlett(len(h_recwindow))

    # plt.plot(inner_x, h, label='Original')
    # plt.plot(inner_x, h_blackwindow, label='Blackman window')
    # plt.plot(inner_x, h_recwindow, label='Rectangular window')
    hf_blackwindow = np.abs(np.fft.fft(h_blackwindow))
    plt.plot(inner_x, hf_blackwindow, label='Blackman window')

    hf_recwindow = np.abs(np.fft.fft(h_recwindow))
    plt.plot(inner_x, hf_recwindow, label='Rectangular window')

    plt.plot(inner_x, y_data, label='Original')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = Q1()
    Q3(data[0], data[-1])
