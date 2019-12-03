import data

data = data.Data('/dev/ttyACM0', 9600)

data.send_char(b"Hello!\n")

data.close()

