#  Project GENOS: ASL Robotic Hand

A low-cost, servo-driven robotic hand designed to replicate American Sign Language (ASL) gestures using a Raspberry Pi Pico. This project focuses on accessibility, affordability, and education — offering an open-source alternative to high-cost systems like the Neuromaker Hand.

---

##  Project Overview

Project GENOS uses five servo motors to manipulate each finger independently, forming ASL letters such as `C`, `Y`, and `L`. An OLED screen is used to visually display which letter the hand is performing in real-time. Smooth motion transitions are implemented in software to protect the servos and make the movement realistic and safe.

---

##  Impact

Originally envisioned as a prosthetic for users with limb differences, GENOS evolved to focus on accessibility in the ASL community — especially in education and demonstration contexts. By lowering the hardware and software barrier, GENOS opens up possibilities for students, developers, and educators who cannot afford commercial options like the ~$300 Neuromaker.

---


---

##  Features

-  Five servo-controlled fingers (thumb to pinky)
-  0.96" OLED screen displays current letter
-  Smooth transition logic avoids sudden servo jerks
-  Degrees-based finger tuning for custom Range of Motion (ROM)
-  Fully programmable via MicroPython
-  Cycles through preset ASL letters with precise movements

---

## 🛠️ Hardware Used

| Component               | Quantity |
|------------------------|----------|
| Raspberry Pi Pico      | 1        |
| SG90 Micro Servos      | 5        |
| UCTRONICS OLED (SSD1306, I2C) | 1        |
| Breadboard / Jumper Wires | as needed |
| Power Supply (5V recommended) | 1        |
| DC to DC Buck Converter| 1        |
| 8.4 Volts 32 Wh Lithium-ion battery | 1    |
| Joystick    |   1     |

---

##  File Structure
- `5FingerTest.py` — Test for servos in alternating directions after redoing servo orientations  
- `5ServoJoystickcode.py` — Testing 5 servos in the same direction  
- `5ServoTest.py` — Auto test for servo motion  
- `ASLVersion1.py` — Working automated test for the ASL characters  
- `Backup_oled.py` — Backup working code for OLED  
- `Joystick&Servo.py` — Joystick test for a single servo  
- `Project-Genos(with_oled).py` — ✅ Final working code for the project — use this on Pico Pi 
