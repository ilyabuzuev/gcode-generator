f = open('test.txt', 'r')
o = open('test2.txt', 'w')

for line in f:
  print(line)

  newLine = line.replace(',', '.')

  o.write(newLine)

f.close()
o.close()