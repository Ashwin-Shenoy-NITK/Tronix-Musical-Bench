/*
 * 18th October, 2016 [5:10am]
 * 
 * 2 : LSB
 * 5 : MSB
 */
#define THRESH 10
#define SIG_INTERVAL  20

#define OUT_READY_PIN 7
#define LED_PIN_R 10
#define LED_PIN_G 11
#define LED_PIN_B 9

unsigned int ip, part_id, parts[]={10,40,60,80,100,120,140,160,180,200,220,240,260,280};
byte intensityR[] = {255, 230, 80, 170, 240, 10, 100, 190, 280, 70, 60, 40, 25, 115, 210};
byte intensityB[] = {0, 35, 200, 80, 250, 130, 120, 110, 100, 190, 180, 170, 65, 235, 20};
byte intensityG[] = {255, 100, 215, 225, 140, 160, 80, 100, 130, 155, 185, 215, 230, 25};

int x = 40;

void sendSignal(unsigned int s)
{
  //Disable the output reading
  digitalWrite(OUT_READY_PIN, LOW);
  //Set the new output
  unsigned int temp = 1;
  for(int i = 2; i < 6; i++)
  {
    digitalWrite(i, ((s & temp) ? HIGH : LOW) );
    temp = temp << 1;
  }
  //Enable the output reading
  digitalWrite(OUT_READY_PIN, HIGH);
}

void setup()
{
  pinMode(A0, INPUT);
  part_id = 0;

  //LED strip pin
  pinMode(LED_PIN_R, OUTPUT);
  pinMode(LED_PIN_G, OUTPUT);
  pinMode(LED_PIN_B, OUTPUT);
  
  
  //Required as the output change happens in 4 steps
  pinMode(OUT_READY_PIN, OUTPUT);
  digitalWrite(OUT_READY_PIN,LOW);

  for(int i = 2; i < 6; i++)
    pinMode(i, OUTPUT);

  Serial.begin(9600);
}

void loop()
{
  for (int i=1;i<14;i++)
   {
  parts[i] = parts[i - 1] + x;
   }

  part_id = 0;
  ip = 1023 - analogRead(A0);
  
  if(ip > THRESH)
  {
    while(ip > parts[part_id++]);
  }
  else
  {
    part_id = 0;
  }

  Serial.println(part_id);
  sendSignal(part_id);
  //Set the brightness of the LED strips
  analogWrite(LED_PIN_R,255-intensityR[part_id]);
  delay(SIG_INTERVAL);
  analogWrite(LED_PIN_G,255-intensityG[part_id]);
  delay(SIG_INTERVAL);
  analogWrite(LED_PIN_B,255-intensityB[part_id]);
  delay(SIG_INTERVAL);
  
}
