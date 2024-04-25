/*This script controls two stepper motors to rotate in sync 
in order to move up or down a compressor acting on a waste
bin. When there is no movement of the motors, a green LED
is activated, being that a yellow LED starts blinking when
there is movement (either compression or retraction)*/

#include <CheapStepper.h> //Stepper motor library
const int passos = 2048*6; //Number of steps (one turn corresponds to 2048)
char sentido; //Stores the char provided by the user

CheapStepper myStepper1(8, 9, 10, 11); //Initializes the motor using pins 8, 10, 9, 11
CheapStepper myStepper2(2, 3, 4, 5); //Initializes the motor using pins 2, 4, 3, 5

void setup() {
  myStepper1.setRpm(24);
  myStepper2.setRpm(24);
  pinMode(6, OUTPUT); // Yellow LED
  pinMode(7, OUTPUT); // Green LED
  Serial.begin(9600); // Inicializa a comunicação serial
  digitalWrite(7, HIGH);
}

void loop() {

  if (Serial.available()) { // Checks if Serial receives something
    sentido = Serial.read(); // Reads the char and saves it
    Serial.println(sentido);
  }

  switch (sentido) {
    case 'A':
      horario(); // Clockwise motion
      break;
    case 'B':
      antihorario(); // Counter-clockwise motion
      break;
  }
}


/*Clockwise motion.
When the motors are running the green LED is deactivated 
and the yellow LED blinks to indicate movement of the compressor.*/
void horario() { 
  bool check1 = true;
  digitalWrite(7, LOW);
  delay(1000);
  digitalWrite(6, HIGH);
  Serial.println("Girando no sentido Horario!");
  for (int i = 0; i < passos; i++) {
    myStepper1.step(true);
    myStepper2.step(true);
    delay(1); // Delay to slow down the stepping speed

    if (i%200 == 0 && i!=0){ 
      if(check1 == true){
        digitalWrite(6, LOW);
      }

      else if (check1 == false){
        digitalWrite(6, HIGH);
      }
      
      check1 = !check1;
    }
  }

  digitalWrite(6, LOW);
  delay(1000);
  digitalWrite(7, HIGH);
  sentido = 'C';
}


/*Counter Clockwise motion.
When the motors are running the green LED is deactivated 
and the yellow LED blinks to indicate movement of the compressor.*/
void antihorario() {
  bool check = true;
  digitalWrite(7, LOW);
  delay(1000);
  digitalWrite(6, HIGH);
  Serial.println("Girando no sentido AntiHorario!");
  for (int i = 0; i < passos; i++) {
    myStepper1.step(false);
    myStepper2.step(false);
    delay(1); //Delay to slow down the stepping speed

    if (i%200 == 0 && i!=0){
      if(check == true){
        digitalWrite(6, LOW);
      }

      else if (check == false){
        digitalWrite(6, HIGH);
      }
      
      check = !check;
    }
  }
  digitalWrite(6, LOW);
  delay(1000);
  digitalWrite(7, HIGH);
  sentido = 'C';
}