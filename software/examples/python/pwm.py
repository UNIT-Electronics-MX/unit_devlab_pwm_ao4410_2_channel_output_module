# LED Fade + PWM duty print 

from machine import Pin, PWM
from time import sleep_ms

LED_PIN = 2          # Change to your LED pin
STEP    = 512        # Brightness increment per step (0..65535)
DELAY_MS = 500

pwm = PWM(Pin(LED_PIN), freq=1000)  # 1 kHz

MAX_DUTY = 65535

def print_duty(d):
    pct = d * 100.0 / MAX_DUTY
    print("Duty:", d, f"({pct:0.1f}%)")

# Fade loop
while True:
    # Fade up
    for duty in range(0, MAX_DUTY + 1, STEP):
        pwm.duty_u16(duty)
        print_duty(duty)
        sleep_ms(DELAY_MS)

    # Fade down
    for duty in range(MAX_DUTY, -1, -STEP):
        pwm.duty_u16(duty)
        print_duty(duty)
        sleep_ms(DELAY_MS)

