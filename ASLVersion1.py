from machine import PWM, Pin
import time

# === Setup ===
finger_pins = [0, 1, 2, 3, 4]  # thumb, index, middle, ring, pinky
servos = []

# Initialize servos
for pin in finger_pins:
    pwm = PWM(Pin(pin))
    pwm.freq(50)
    servos.append(pwm)

# === Helper Functions ===
# Map degree (0 to 90) to duty cycle (just an example mapping)
def degree_to_duty(degrees):
    # Example mapping from degrees to servo duty (0-90 degrees -> 2000-8000 duty)
    return int(2000 + (degrees / 90) * (8000 - 2000))

# Smooth movement for safe operation (added specific handling for middle finger)
def smooth_move(servo, current, target, step=20, delay=0.01):
    if current == target:
        return target
    direction = 1 if target > current else -1
    # Move in smaller increments, to smooth out the motion
    for duty in range(current, target, direction * step):
        servo.duty_u16(duty)
        time.sleep(delay)
    servo.duty_u16(target)  # Ensure we end exactly at the target
    return target

# === Preset Positions ===
# Use degrees here (0° = fully closed, 90° = fully open)
def set_pose(thumb_deg, index_deg, middle_deg, ring_deg, pinky_deg):
    # Map degrees to servo duty cycles
    positions = [
        degree_to_duty(thumb_deg), 
        degree_to_duty(index_deg),
        degree_to_duty(middle_deg),
        degree_to_duty(ring_deg),
        degree_to_duty(pinky_deg)
    ]
    
    # Apply position with smoothing
    for i in range(5):
        current_duty = servos[i].duty_u16()
        # If the middle finger is the one moving, make the transition even smoother
        if i == 2:  # Middle finger (pin 2)
            smooth_move(servos[i], current_duty, positions[i], step=10, delay=0.015)  # Smoother transition
        else:
            smooth_move(servos[i], current_duty, positions[i])  # Regular smoothing
    time.sleep(5)  # Hold position for 5 seconds

# === ASL Poses ===

# C Pose
def pose_C():
    set_pose(50, 60, 30, 90, 0)  # Adjust degrees as needed for C

# Y Pose
def pose_Y():
    set_pose(90, 90, 20, 100, 90)  # Adjust degrees as needed for Y

# L Pose
def pose_L():
    set_pose(50, 90, 0, 0, 90)  # Adjust degrees as needed for L

# === Run through poses ===
while True:
    print("C Pose")
    pose_C()

    print("Y Pose")
    pose_Y()

    print("L Pose")
    pose_L()
