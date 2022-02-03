def idiot_speak(s):
  snew = ''
  i = 0
  while i < len(s) - 1:
    snew = snew + s[i].lower()
    snew = snew + s[i+1].upper()
    i = i + 2
  if i < len(s):
    snew = snew + s[i].lower()
  return snew

def idiotify_file(file_name):
  idiot = ''
  try:
    f = open(file_name, 'r')
    idiot = idiot_speak(f.read())
    f.close()
    f = open('idiotified_'+file_name, 'w')
    f.write(idiot)
    f.close()
  except FileNotFoundError as e:
    print('file "' + file_name + '" does not exist!')
  except UnicodeDecodeError as e:
    print('file "' + file_name + '" could not be opened, reason being: ')
    print(e)

file_name = input('name of file to be idiotified: ')
idiotify_file(file_name)
