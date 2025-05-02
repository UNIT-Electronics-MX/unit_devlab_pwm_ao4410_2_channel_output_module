---
title: "PWM module"
version: "1.0"
modified: "2025-04-30"
output: "pwm_module"
subtitle: "Universal Programmer for AVR, ARM (CMSIS-DAP), and CPLD (MAX II)
"
---

<!--
# README_TEMPLATE.md
Este archivo sirve como entrada para generar un PDF técnico estilo datasheet.
Edita las secciones respetando el orden, sin eliminar los encabezados.
-->
 <!-- logo -->

# PWM Module

![product](./images/product.jpg)

## Introduction

This two-channel PWM module PCB is purpose-built to amplify pulse-width modulation signals from a microcontroller, allowing it to switch external loads at voltages and currents well beyond the device’s native limits. Its compact design, featuring clearly labeled screw-terminal connectors, is ideal for applications such as motor speed control, high-power LED dimming, or any project requiring precise PWM regulation. Additionally, a QWIIC-compatible 4-pin header is included for convenient plug-and-play wiring and daisy-chaining of power and PWM signals with standard Qwiic cables.

## Functional Description

- 

## Electrical Characteristics & Signal Overview

- 

## Applications

-

## Features

- The module contains two devices that share the same features but are connected to separate input and output controls, allowing for independent operation.



## Pin & Connector Layout


| Device | Input Control               | Output Control                | Features                                               |
|--------|-----------------------------|-------------------------------|--------------------------------------------------------|
| PWM 1  | Dedicated input for control | Dedicated output for driving  | MOSFET driver with precise control and transient protection |
| PWM 2  | Dedicated input for control | Dedicated output for driving  | MOSFET driver with precise control and transient protection |

## Settings

### Interface Overview

| Interface  | Signals / Pins            | Typical Use                                         |
|------------|----------------------------|-----------------------------------------------------|
| -       | - | -      |


###  Supports 


| Symbol | I/O   | Description                         |
| ------ | ----- | ----------------------------------- |
| VCC    | Input | Power supply (3.3V or 5V)           |

  

## Block Diagram

![Function Diagram](images/function-diagram.jpg)

## Dimensions

![Dimensions](images/dimensions.png)

## Usage

Works with:

- 

## Downloads

- [Schematic PDF](docs/schematic.pdf)
- [MAX1704X Library](https://github.com/UNIT-Electronics/MAX1704X_lib)


## Purchase

- [Buy from UNIT Electronics](https://www.uelectronics.com)
