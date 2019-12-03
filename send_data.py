import data

port = input("Enter port (ACM0, GS0): ")

data = data.Data("/dev/tty" + port)

while True:
  try:
    line = input("Enter data: ")
    data.send_char(line.encode())
  except KeyboardInterrupt:
    print("Keyboard interrupt, terminating")
    break

data.close()

