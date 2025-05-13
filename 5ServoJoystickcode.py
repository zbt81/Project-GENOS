from machine import Pin, PWM, ADC
import time

# Setup joystick
joystick_x = ADC(26)  # GP26 = ADC0

# Setup servos on GP0 - GP4
servo_pins = [0, 1, 2, 3, 4]
servos = []

for pin in servo_pins:
    pwm = PWM(Pin(pin))
    pwm.freq(50)
    servos.append(pwm)

# Helper to convert joystick to servo duty
def map_joystick_to_duty(adc_val):
    # Map 0-65535 to 1638-8192 (approx 0° to 180° for servo)
    return int((adc_val / 65535) * (8192 - 1638) + 1638)

while True:
    x_val = joystick_x.read_u16()
    duty = map_joystick_to_duty(x_val)

    for servo in servos:
        servo.duty_u16(duty)

    time.sleep(0.02)  # Small delay for smooth control
