# Pruebas de control de calidad: UE0054 módulo PWM

**Departamento de I2D**

**Versión:** 1.0

**Fecha:** 22/07/2025

1. **Objetivo**
   
    Asegurar el correcto funcionamiento y calidad de los módulos PWM de UNIT Electronics tras su fabricación, mediante
    inspección visual y pruebas funcionales, verificando iluminación LED 

2. **Revisión visual inicial**
   
   **Importante**: Antes de conectar o energizar el módulo:

   - Verificar que todos los componentes estén correctamente soldados y no falte ninguno.
   - Revisar posibles cortocircuitos visibles, componentes desalineados o soldaduras frías.
   - Comprueba que “PWM1 GND” y “PWM2 GND” están unidos al GND del conector central. 
   - Verifica que no hay corto entre “Load +” y “Load –” en cada canal.
   - Confirmar que el LED está correctamente orientado y soldado.
   - Confirmar que este soldado el conector JST
   
3. **Prueba de encendido básico**

    - Conecta la fuente solo al conector de entrada de potencia del módulo.
      -  Energizar el módulo mediante una fuente de alimentación conectando a las terminales **Load +** y **Load -**
      - Mide consumo en reposo.
      - Comprueba que ningún componente se calienta

   - Lleva el pin “PWM1” a un nivel alto fijo (duty = 100 % o 1 lógico).

   - Observa si el LED azul correspondiente se enciende.

   - Repite con PWM2.

4. **Prueba usando la Dual MCU**

    - La Dual MCU debe de estar en modo RP2040 
    - Copia y pega el siguiente código en Thonny IDE:
    ```python
    from machine import Pin, PWM
    from time import sleep_ms

    PWM_PIN = 2          
    STEP    = 512        # Brightness increment per step (0..65535)
    DELAY_MS = 500

    pwm = PWM(Pin(PWM_PIN), freq=1000)  # 1 kHz

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

    ```
   - Conecta el pin GPIO2 al canal PWM1 y su GND respectivamente 

5. **Aprobación**

    El módulo pwm se considera aprobado si: 

       - Los canales 1 y 2 de potencia funcionan correctamente.
       - Los canales 1 y 2 de señales PWM hacen funcionar los canales de potencia  