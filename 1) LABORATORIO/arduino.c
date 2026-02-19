#include <SoftwareSerial.h>

SoftwareSerial picSerial(2, 3); // RX, TX

void setup() {
  Serial.begin(9600);    // con PC
  picSerial.begin(9600); // con PIC
}

void loop() {
  // De PC a PIC
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    picSerial.println(cmd);
  }
  
  // De PIC a PC
  if (picSerial.available()) {
    String resp = picSerial.readStringUntil('\n');
    Serial.println(resp);
  }
}