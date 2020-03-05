import serial
ser=serial.Serial("/dev/tty.usbserial-142420",9600,timeout=0.5)

while 1:
    ser.flush()
    Formaldehyde=ser.readall()
    print(Formaldehyde[4]*256+Formaldehyde[5])
