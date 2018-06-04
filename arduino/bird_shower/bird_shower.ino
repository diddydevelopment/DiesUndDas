/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int pump = A0;
int sensor = 2;

int pumpTime = 2000;
int pumpDelay = 5000;


// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(pump, OUTPUT);
  digitalWrite(pump,LOW);
  pinMode(sensor, INPUT);  
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  Serial.println(digitalRead(sensor));
  
  if(digitalRead(sensor)) {
    digitalWrite(pump, HIGH);
    delay(pumpTime);
    digitalWrite(pump,LOW);
    delay(pumpDelay);

  }
    delay(500);          
          
}
