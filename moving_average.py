import numpy as np

def moving_average(signal, window_size):
    ### Replace with your own code (begin) ###
    signal = np.array(signal, dtype=float)
    n = len(signal)
    k = (window_size - 1) // 2

    result = np.zeros(n, dtype=float)

    for i in range(n):
        # межі вікна
        left = max(0, i - k)
        right = min(n - 1, i + k)

        window = signal[left:right + 1]
        result[i] = np.mean(window)

    return result
    ### Replace with your own code (end)   ###

