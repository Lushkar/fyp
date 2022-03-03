import serial
import time

print("Start")
port="COM4" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
print("Connected")
bluetooth.flushInput() #This gives the bluetooth a little kick

print('Pinging')
bluetooth.write(b'TEST')
time.sleep(0.1)

# for i in range(5): #send 5 groups of data to the bluetooth
# 	print("Ping")
# 	bluetooth.write(b"BOOP "+str.encode(str(i)))#These need to be bytes not unicode, plus a number
# 	input_data=bluetooth.readline()#This reads the incoming data. In this particular example it will be the "Hello from Blue" line
# 	print(input_data.decode())#These are bytes coming in so a decode is needed
# 	time.sleep(0.1) #A pause between bursts


bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")


# import serial 



# BAUDRATE = 38400
# PORT = 'COM5'

# # # s = serial.Bluetooth()
# # # s.baudrate = BAUDRATE 
# # # s.port = PORT


# s = serial.Serial("COM5",38400,timeout = 2)
# print('connected!')
# # s.write(bytes("hello!",'utf-8'))
# s.write(b'a')     
# s.close()
# print('closed')


# import serial  
# import time  
# print("Start")  
# port="/dev/tty.HC-06-DevB"  
# bluetooth=serial.serial(port,9600)  
# print("Connected")
# bluetooth.flushInput()  
# for i in range(5):
#     print("ping")  
#     bluetooth.Write(b"Boop"+str.encode(str(i)))  
#     input-date = bluetooth readline()  
#     print(input_data.decode())  
#     time.sleep(0.1)  
# bluetooth.close()  
# print("Done")  
