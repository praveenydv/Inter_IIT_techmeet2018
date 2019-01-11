void setup() {
 Serial.begin(9600);
 pinMode(A3,INPUT);// put your setup code here, to run once:
pinMode(A5,INPUT);// put your setup code here, to run once:

}

void loop() {
  
  int i=0;
 int m=0;
  while(i<30){
    
     m=m+analogRead(A5); 
     i=i+1;
  }
  m=m/30;
  Serial.println(m);
  // put your main code here, to run repeatedly:

}
