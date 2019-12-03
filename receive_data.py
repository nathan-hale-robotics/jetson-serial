import data

data = data.Data("/dev/ttyGS0")

while True:
  try:
    response = data.read_char()
    if response != b'':
      print(response)
  except KeyboardInterrupt as e:
    print("Keyboard interupt, terminating")
    break

data.close()
