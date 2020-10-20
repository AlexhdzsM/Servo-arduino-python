//Mariano Alejandro Hernández Salazar 
//control de servo con python

#include <Servo.h>

Servo myServo;  // Creando el objeto servo

//Variables
String dataString="";
bool dataComplete=false;
int data= 0;



void setup() {
  myServo.attach(9); // asignando el pin 9 al servo
  Serial.begin(9600); 
}


void loop() {
  if (dataComplete){
    data=dataString.toInt();

    ///////////////////////////
    task();
    //////////////////////////
    dataString = "";
    dataComplete=false;
    
  }
}

void serialEvent(){
  while(Serial.available()){
    char inChar=(char)Serial.read();
    dataString+=inChar;
    if (inChar=='\n'){
      dataComplete=true;
    }
  }
}
void task(){
  myServo.write(data);
}

  
