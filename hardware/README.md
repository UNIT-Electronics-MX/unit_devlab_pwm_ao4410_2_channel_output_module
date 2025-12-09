# Hardware

<div align="center">

<a href="./unit_sch_v_0_0_1_ue0083_pwm_module.pdf"><img src="resources/Schematics_icon.jpg?raw=false" width="450px"><br/> Schematics</a>
</div>

## Key Technical Specifications

<div align="center">

| **Parameter** |            **Description**            | **Min** | **Max** | **Unit** |
|:-------------:|:-------------------------------------:|:-------:|:-------:|:--------:|
|      Vin      | Input voltage to power on the module  |   3.3   |    5    |    V     |
|    V Load*    | Maximum voltage for the external load |    -    |   30    |    V     |
|    I Load*    | Maximum current for the external load |    -    |   15    |    A     |
|      P*       |         Maximum power at load         |    -    |   200   |    W     |

</div>

* A DIP switch is provided to couple or isolate the microcontroller ground from the load ground.
* Mode selection**: use jumper bridges to choose "Direct mode" (grounds coupled) or "Isolated mode" (grounds isolated) for improved protection.

***These values were tested at 1 kHz. Performance may vary at other frequencies.**

****Use the jumper bridges and the DIP switch to change between Direct and Isolated modes.**



## Pinout

<div align="center">

<a href="./unit_pinout_v_0_0_2_ue0083_pwm_module_en.pdf"><img src="resources/unit_pinout_v_0_0_2_ue0083_pwm_module_en.jpg" width="500px"><br/> Pinout</a>
<br/><br/>

| Channel           | Description                                                                           | Control Pins | Power Pins | Load Terminals | Typical Use                           |
|-------------------|---------------------------------------------------------------------------------------|--------------|------------|----------------|---------------------------------------|
| **PWM Channel 1** | MOSFET-based driver that amplifies MCU’s PWM output to switch a heavier external load | PWM1, GND    | VCC1, GND  | Load1          | DC motors, high-power LEDs, solenoids |
| **PWM Channel 2** | Identical high-current PWM driver on a second channel                                 | PWM2, GND    | VCC2, GND  | Load2          | Same as Channel 1                     |

<br/>
</div>

## Topology

<div align="center">

<a href="./resources/unit_topology_v_0_0_1_ue0083_PWM-Module.png"><img src="./resources/unit_topology_v_0_0_1_ue0083_PWM-Module.png" width="500px"><br/> Topology</a>

| Ref.  | Description                                                                 |
|-------|-----------------------------------------------------------------------------|
| SW    | Dip Switch for coupling grounds                                             |
| L1    | Channel 1 PWM LED                                                           |
| L2    | Channel 2 PWM LED                                                           |
| J1    | Screw Terminal Block for Channel 1 Load                                     |
| J2    | Screw Terminal Block for Channel 2 Load                                     |
| J3    | JST 1mm Connector for input signals                                         |
| JP1   | Header for Channel 1 mode selection                                         |
| JP2   | Header for input signals                                                    |
| JP3   | Header for Channel 2 mode selection                                         |
</div>

## Dimensions

<div align="center">

<a href="./resources/unit_dimension_v_0_0_1_ue0083_PWM-Module.png"><img src="./resources/unit_dimension_v_0_0_1_ue0083_PWM-Module.png" width="500px"><br/> Dimensions</a>

</div>