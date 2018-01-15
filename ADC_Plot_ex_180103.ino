const int analogIn = A0;
int analogVal = 0;

void setup() {
  Serial.begin(19200);
}

void loop() {

  analogVal = analogRead(analogIn);
  Serial.println(analogVal);
  delay(300);
}

