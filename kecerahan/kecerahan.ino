int pinBt1 = 2;
int pinBt2 = 3;
int pinLED = 9;

void setup() {
  pinMode(pinBt1, INPUT);
  pinMode(pinBt2, INPUT);
  pinMode(pinLED, OUTPUT);
  digitalWrite(pinBt1, HIGH);
  digitalWrite(pinBt2, HIGH);
}
int b = 0;
void loop() {
  if(digitalRead(pinBt1) == LOW){
    b++;
  }else if(digitalRead(pinBt2) == LOW){
    b--;
  }
  b = constrain(b,0,255);
  analogWrite(pinLED, b);
  delay(20);
}
