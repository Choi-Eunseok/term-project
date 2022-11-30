#include <Servo.h>
Servo myservo;
int currPos = 0;

#include <SoftwareSerial.h>
#include "TFMini.h"
TFMini tfmini;

SoftwareSerial SerialTFMini(10, 11);

void getTFminiData(int* distance, int* strength) {
  static char i = 0;
  char j = 0;
  int checksum = 0;
  static int rx[9];
  if (SerialTFMini.available()) {
    rx[i] = SerialTFMini.read();
    if (rx[0] != 0x59) {
      i = 0;
    } else if (i == 1 && rx[1] != 0x59) {
      i = 0;
    } else if (i == 8) {
      for (j = 0; j < 8; j++) {
        checksum += rx[j];
      }
      if (rx[8] == (checksum % 256)) {
        *distance = rx[2] + rx[3] * 256;
        *strength = rx[4] + rx[5] * 256;
      }
      i = 0;
    } else {
      i++;
    }
  }
}

int availAngle[] = {0, 153};

void radar() {
  Serial.println(availAngle[1]);
  for (currPos; currPos <= 153; currPos += 1) {
    myservo.write(currPos);
    delay(100);
    int distance = 0;
    int strength = 0;
    getTFminiData(&distance, &strength);
    while (!distance) {
      getTFminiData(&distance, &strength);
    }
    Serial.println(distance);
    delay(10);
  }
  moveServo(0);
}

void moveServo(int goalPos) {
  while (goalPos != currPos) {
    if (goalPos > currPos) {
      currPos++;
    }
    else if (currPos > goalPos) {
      currPos--;
    }
    else currPos = goalPos;
    myservo.write(currPos);
    delay(10);
  }
}

void setup() {
  Serial.begin(9600);
  myservo.attach(9);

  SerialTFMini.begin(TFMINI_BAUDRATE);
  tfmini.begin(&SerialTFMini);

  for (currPos = 0; currPos < 153; currPos += 1) {
    myservo.write(currPos);
    delay(10);
  }
  delay(500);
  for (currPos = 153; currPos >= 0; currPos -= 1) {
    myservo.write(currPos);
    delay(10);
  }
}

void loop() {
  while (Serial.available() > 0) {
    long value = Serial.parseInt();
    if (value == 1000) {
      radar();
    }
    else {
      int pos = map(value, 0, 360, availAngle[0], availAngle[1]);
      moveServo(pos);
      Serial.println("Servo Move Finished");
    }
  }
}

