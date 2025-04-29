# Hardware


<a href="#"><img src="resources/Schematics_icon.jpg?raw=false" width="500px"><br/> Schematics</a>




# Pinout

<a href="#"><img src="resources/pwm_pinout.jpg" width="500px"><br/> Pinout</a>


| Channel          | Description                                         | Control Pins   | Power Pins      | Load Terminals             | Typical Use                          |
|------------------|-----------------------------------------------------|----------------|-----------------|----------------------------|--------------------------------------|
| **PWM Channel 1**| MOSFET-based driver that amplifies MCU’s PWM output to switch a heavier external load | PWM1, GND      | VCC1, GND       | Load1     |    DC motors, high-power LEDs, solenoids |
| **PWM Channel 2**| Identical high-current PWM driver on a second channel | PWM2, GND      | VCC2, GND       | Load2        | Same as Channel 1                    |
