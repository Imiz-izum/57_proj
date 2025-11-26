#include <NewPing.h>
#define PIN_TRIG A0
#define PIN_ECHO A1

NewPing sonar(PIN_TRIG, PIN_ECHO);


void setup()
{
  Serial.begin(9600);
}

void loop()
{
  double distanse1 = sonar.ping_cm() / 100.00;
  delay(1000);
  double distanse2 = sonar.ping_cm() / 100.00;
  float vobj = (distanse2 - distanse1) * 1.00;
  delay(1000);
  Serial.println(vobj);
}