# Software Examples for PWM AO4410 2-Channel Output Module

This directory contains example code demonstrating how to use the PWM AO4410 2-Channel Output Module with different programming platforms.

## Overview

The PWM AO4410 module amplifies PWM signals from microcontrollers to control external loads at higher voltages and currents. The examples show how to generate PWM signals that can be used for:

- Motor speed control
- High-power LED dimming
- Variable power output control
- Load switching applications

## Available Examples

### 📁 C/Arduino Examples (`examples/c/`)

#### `pwm.ino` - LED Fade with PWM Control
**Platform:** Arduino IDE compatible boards (Arduino Uno, ESP32, etc.)

**Description:** 
This example demonstrates basic PWM control by fading an LED up and down. It shows how to:
- Configure a PWM output pin
- Generate variable duty cycle signals
- Monitor PWM duty cycle values via Serial Monitor
- Create smooth fading effects

**Key Features:**
- Uses `analogWrite()` function for PWM generation
- Configurable brightness step size
- Serial output for debugging and monitoring
- Simple fade up/down pattern

**Hardware Connections:**
- Connect PWM output pin (default: pin 9) to the module's PWM input
- Connect LED or load to the module's output terminals
- Ensure proper power supply connections

**Usage:**
1. Open in Arduino IDE
2. Select your board and port
3. Upload the sketch
4. Open Serial Monitor at 115200 baud
5. Observe the LED fading and duty cycle values

### 📁 Python Examples (`examples/python/`)

#### `pwm.py` - MicroPython PWM Control
**Platform:** MicroPython (ESP32, Raspberry Pi Pico, etc.)

**Description:**
This MicroPython example shows how to control PWM outputs using the `machine.PWM` class. It demonstrates:
- High-resolution PWM control (16-bit duty cycle)
- Frequency configuration
- Percentage-based duty cycle calculation
- Continuous fading loop

**Key Features:**
- 16-bit duty cycle resolution (0-65535)
- Configurable PWM frequency (default: 1 kHz)
- Percentage calculation for easy understanding
- Continuous fade pattern

**Hardware Connections:**
- Connect PWM output pin (default: GPIO 2) to the module's PWM input
- Connect LED or load to the module's output terminals
- Ensure proper power supply connections

**Usage:**
1. Upload to your MicroPython device
2. Run the script
3. Observe the console output showing duty cycle values
4. Watch the connected load fade smoothly

## Module Specifications

### PWM Input Requirements
- **Voltage:** 3.3V or 5V logic levels
- **Frequency Range:** 1 Hz - 100 kHz (recommended)
- **Duty Cycle:** 0-100%

### Output Characteristics
- **Channels:** 2 independent outputs
- **Maximum Voltage:** 30V DC
- **Maximum Current:** 4A per channel
- **MOSFET:** AO4410 N-channel
- **Control:** Low-side switching

## Connection Guide

### QWIIC/4-Pin Header Connections
| Pin | Function | Color (Standard) |
|-----|----------|------------------|
| 1   | GND      | Black            |
| 2   | VCC      | Red              |
| 3   | PWM1     | Blue             |
| 4   | PWM2     | Yellow           |

### Screw Terminal Connections
- **VIN+/VIN-:** External power supply for loads
- **OUT1+/OUT1-:** Channel 1 output to load
- **OUT2+/OUT2-:** Channel 2 output to load

## Safety Considerations

⚠️ **Important Safety Notes:**
- Always ensure proper power supply ratings
- Use appropriate wire gauge for current requirements
- Verify load compatibility before connection
- Never exceed maximum voltage/current ratings
- Ensure proper heat dissipation for high-power applications

## Troubleshooting

### Common Issues:
1. **No PWM Output:** 
   - Check PWM signal connections
   - Verify code is generating PWM on correct pin
   - Ensure proper power supply

2. **Insufficient Load Power:**
   - Check external power supply voltage/current
   - Verify load requirements are within module limits

3. **Erratic Behavior:**
   - Check for proper grounding
   - Verify PWM frequency is within acceptable range
   - Ensure stable power supply

## Getting Started

1. **Choose your platform** (Arduino/C or MicroPython)
2. **Wire the module** according to the connection guide
3. **Load the example code** for your platform
4. **Modify parameters** as needed for your application
5. **Test with a simple load** (LED) before connecting high-power devices

## Additional Resources

- [Hardware Documentation](../hardware/README.md)
- [Schematic Files](../hardware/resources/)
- [Product Datasheet](../hardware/resources/)
- [Online Documentation](https://unit-electronics-mx.github.io/unit_pwm_module/)

## Support

For technical support and questions:
- GitHub Issues: [Open an issue](https://github.com/UNIT-Electronics-MX/unit_devlab_pwm_ao4410_2_channel_output_module/issues)
- Website: [uelectronics.com](https://uelectronics.com/)
- Documentation: [Product Wiki](https://unit-electronics-mx.github.io/unit_pwm_module/)
