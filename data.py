import serial

class Data:
  def __init__(self, port):
    self.ser = serial.Serial()
    self.ser.port = port
    self.serConf()
    self.ser.open()

    self.ser.flushInput()
    self.ser.flushOutput()

  def send_cmd(self, cmd):
    pass

  def read_cmd(self):
    pass

  def send_char(self, char):
    self.ser.write(char)

  def read_char(self):
    return self.ser.read()

  def serConf(self):
    self.ser.baudrate = 9600
    self.ser.bytesize = serial.EIGHTBITS
    self.ser.parity = serial.PARITY_NONE
    self.ser.stopbits = serial.STOPBITS_ONE
    self.ser.timeout = 0 # Non-Block reading
    self.ser.xonxoff = False # Disable Software Flow Control
    self.ser.rtscts = False # Disable (RTS/CTS) flow Control
    self.ser.dsrdtr = False # Disable (DSR/DTR) flow Control
    self.ser.writeTimeout = 2

  def close(self):
    self.ser.close()

