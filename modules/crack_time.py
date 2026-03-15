import math

def estimate_crack_time(entropy):

    guesses_per_second = {
        "CPU": 1e6,
        "GPU": 1e9,
        "Supercomputer": 1e12
    }

    results = {}

    for device, gps in guesses_per_second.items():

        guesses = 2 ** entropy
        seconds = guesses / gps

        years = seconds / (60 * 60 * 24 * 365)

        results[device] = round(years, 4)

    return results