// LED Fade + PWM duty print on Serial Monitor (simple version)

int LED_PIN = 9;      // PWM pin
int STEP    = 5;      // Brightness increment per step

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);          // Match this baud rate in the Serial Monitor
  delay(200);                    // Small pause to avoid garbage at start
  Serial.println("Starting fade...");
}

void loop() {
  // Fade up
  for (int duty = 0; duty <= 255; duty += STEP) {
    analogWrite(LED_PIN, duty);
    Serial.print("Duty: ");
    Serial.println(duty);
    delay(500);
  }

  // Fade down
  for (int duty = 255; duty >= 0; duty -= STEP) {
    analogWrite(LED_PIN, duty);
    Serial.print("Duty: ");
    Serial.println(duty);
    delay(500);
  }
}
