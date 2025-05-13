from machine import Pin, PWM, ADC
import time

# Setup joystick
joystick_x = ADC(26)  # GP26 = ADC0

# Setup servos on GP0 - GP4
servo_pins = [0, 1, 2, 3, 4]
servos = []

# Define reversed orientation for each servo (True = invert)
reversed_servo = [False, True, False, True, False]

# Common PWM range for most hobby servos
MIN_DUTY = 1638   # ≈0°
MAX_DUTY = 8192   # ≈180°

for pin in servo_pins:
    pwm = PWM(Pin(pin))
    pwm.freq(50)
    servos.append(pwm)

# Updated mapping function with correct inversion and ring finger adjustment
def map_joystick_to_duty(adc_val, invert=False, is_ring_finger=False):
    if invert:
        # Flip ADC value first to keep full range
        adc_val = 65535 - adc_val

    # If it's the ring finger, adjust the range to go down more
    if is_ring_finger:
        return int((adc_val / 65535) * (MAX_DUTY - MIN_DUTY) + MIN_DUTY * 1.1)  # Adjust this factor

    return int((adc_val / 65535) * (MAX_DUTY - MIN_DUTY) + MIN_DUTY)

while True:
    x_val = joystick_x.read_u16()

    for i, servo in enumerate(servos):
        # Check if this is the ring finger (pin 3)
        is_ring_finger = (servo_pins[i] == 3)
        duty = map_joystick_to_duty(x_val, reversed_servo[i], is_ring_finger)
        servo.duty_u16(duty)

    time.sleep(0.02)
