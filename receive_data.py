import data

port = input("Enter port (ACM0, GS0): ")

data = data.Data("/dev/tty" + port)


while True:
  try:
    response = data.read_char()
    if response != b'':
      print(response)
  except KeyboardInterrupt as e:
    print("Keyboard interupt, terminating")
    break

data.close()
