import serial 


BAUDRATE = 38400
PORT = 'COM1'

s = serial.Bluetooth()
s.baudrate = BAUDRATE 
s.port = PORT


# s = serial.Serial("COM3",9600,timeout = 2)
# s.write(bytes("hello!",'utf-8'))