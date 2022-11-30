#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  while (Serial.available() > 0) {
    long value = Serial.parseInt(); //숫자로 된 문자열을 숫자로 바꿔준다.
    myservo.write(value);
    delay(15);
  }
}
