import data

data = data.Data("/dev/ttyGS0", 9600)

while True:
  try:
    response = data.read_char()
    if response != b'':
      print(response)
  except Exception as e:
    print("ERROR:", e)
    break
  except KeyboardInterrupt as e:
    print("Keyboard interupt, terminating")
    break

data.close()
