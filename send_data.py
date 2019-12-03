import data

data = data.Data("/dev/ttyACM0")

while True:
  try:
    line = input("Enter data:")
    data.send_char(line.encode())
  except KeyboardInterrupt:
    print("Keyboard interrupt, terminating")
    break

data.close()

