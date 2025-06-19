# Signal Distance Estimator

This repository contains a Python script that estimates the physical distance between a wireless transmitter and receiver based on the received signal strength (RSSI) and signal frequency. It utilizes a simplified Free Space Path Loss (FSPL) model for approximation.

## Author

Created by **h4ckd4d**

---

## Table of Contents

- [Overview](#overview)
- [What is RSSI](#what-is-rssi)
- [FSPL-Based Distance Formula](#fspl-based-distance-formula)
- [Example Calculations](#example-calculations)
- [Frequency vs RSSI Reference Table](#frequency-vs-rssi-reference-table)
- [Installation](#installation)
- [Usage](#usage)
- [Limitations](#limitations)
- [License](#license)

---

## Overview

The `signal_distance_estimator.py` script provides a quick way to estimate how far a device is from a Wi-Fi antenna or access point using the strength of the received signal. It supports any frequency in MHz and RSSI in dBm.

---

## What is RSSI

**RSSI** (Received Signal Strength Indicator) is a measurement of the power level being received by an antenna. It is typically expressed in **negative dBm values**.

### RSSI Reference Guide

| RSSI (dBm) | Signal Quality   | Description                          |
|------------|------------------|--------------------------------------|
| -30        | Excellent         | Strong, very close to AP             |
| -50        | Very Good         | Same room or nearby                  |
| -70        | Weak              | May experience interruptions         |
| -90        | Very Poor         | Likely not usable                    |

---

## FSPL-Based Distance Formula

This tool uses the following equation, based on the **Free Space Path Loss** model:



Distance = 10 ^ ((27.55 - 20 * log10(2400) + 40) / 20)
Distance ≈ 1.00 meters




### 2. RSSI = -40 dBm at 5 GHz


Distance ≈ 0.60 meters


---

## Frequency vs RSSI Reference Table

| Frequency | RSSI (dBm) | Estimated Distance |
|-----------|------------|---------------------|
| 2400 MHz  | -30        | 0.32 m              |
| 2400 MHz  | -50        | 3.16 m              |
| 2400 MHz  | -70        | 31.62 m             |
| 5000 MHz  | -30        | 0.18 m              |
| 5000 MHz  | -50        | 1.78 m              |
| 5000 MHz  | -70        | 17.78 m             |

---

## Installation

Clone the repository and ensure Python 3 is installed on your system.


git clone https://github.com/h4ckd4d/signal-distance-estimator.git
cd signal-distance-estimator


## Usage

Run the script with Python 3:

python3 signal_distance_estimator.py

You can modify the script to input your own RSSI and frequency values.
