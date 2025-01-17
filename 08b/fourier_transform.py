import numpy as np

def compute_fourier_transform(data_time_domain):
    math_i = 1j # This is how to write sqrt(-1) = i in python.
    N = len(data_time_domain) # How many points in the data
    k = np.arange(N)
    n = np.arange(N)
    data_frequency_domain = np.zeros(N,dtype=np.complex128)
    for j in k:
        for i in n:
            data_frequency_domain[j] += data_time_domain[i] * \
                (np.cos(2 * np.pi * j  * i / N) - math_i * np.sin(2 * np.pi * j * i / N))
    return data_frequency_domain

def compute_inverse_fourier_transform(data_frequency_domain):
    math_i = 1j # This is how to write sqrt(-1) = i in python.
    N = len(data_frequency_domain) # How many points in the data
    k = np.arange(N)
    n = np.arange(N)
    data_time_domain = np.zeros(N,dtype=np.complex128)
    for i in n:
        for j in k:
            data_time_domain[j] += data_frequency_domain[i] * \
                (np.cos(2 * np.pi * j  * i / N) + math_i * np.sin(2 * np.pi * j * i / N))
    return data_time_domain / N

