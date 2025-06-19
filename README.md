# Signal Distance Estimator

Estimate the distance (in meters) between a device and a wireless access point based on signal strength (RSSI in dBm) and frequency (MHz).

## 📌 Features
- Simple and accurate estimation formula using Free Space Path Loss (FSPL)
- Written in Python, easy to modify or expand
- Author: [h4ckd4d](https://github.com/h4ckd4d)

## 🧪 Formula Used
Distance = 10 ^ ((27.55 - (20 * log10(frequency)) + |RSSI|) / 20)

- `frequency`: in MHz (e.g. 2400 for 2.4 GHz Wi-Fi)
- `RSSI`: Received Signal Strength Indicator in dBm

## ▶️ Usage
```bash
python3 signal_distance_estimator.py
