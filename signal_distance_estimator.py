# signal_distance_estimator.py
# Signal Distance Estimator
# Author: h4ckd4d
# Calculates estimated distance from RSSI (dBm) and signal frequency (MHz)

import math

def estimate_distance(rssi, frequency_mhz):
    exponent = (27.55 - (20 * math.log10(frequency_mhz)) + abs(rssi)) / 20.0
    return round(pow(10.0, exponent), 2)

# Example usage
if __name__ == "__main__":
    frequency = 2400  # MHz (Wi-Fi 2.4 GHz)
    rssi = -50        # dBm
    distance = estimate_distance(rssi, frequency)
    print(f"Estimated distance: {distance} meters")
