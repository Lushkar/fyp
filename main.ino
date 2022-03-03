#include "SoftwareSerial.h"
SoftwareSerial serial_connection(10, 11); // The Tx and Rx pins for bluetooth

#define BUFFER_SIZE 64 
#define BAUD_RATE 9600

char inData[BUFFER_SIZE];
char inChar=-1;
int count=0
int i=0;

void setup() {
    Serial.begin(BAUD_RATE);
    serial_connection.begin(BAUD_RATE);
    serial_connection.println("READY TO CONNECT ON BLUETOOTH"); // This will never be seen 
    Serial.println("Started");
}


void loop() {
    byte byte_count = serial_connection.available(); // This gets the number of bytes that were sent by the python script
    if (byte_count) {
        Serial.println("Incoming Data");
        int first_bytes = byte_count; // Initialize the number of bytes that we might handle 
        int remaining_bytes=0; // Initialize the bytes that we may have to burn off to prevent a buffer overrun 

        if (first_bytes >= BUFFER_SIZE - 1) {
            remaining_bytes = byte_count - (BUFFER_SIZE - 1);
        }

        for (i=0; i < first_bytes; i++){
            inChar = serial_connection.read(); // Read one byte
            inData[i] = inChar;
        }
        inData[i] = '\0';
        
        Serial.println(inData[2]);

        for (i=0; i < remaining_bytes; i++){
            inChar = serial_connection.read();
        }

        count++;
        
    }
    delay(100);
}