import matplotlib.pyplot as plt

file = open('test2.txt', 'r')

x = []
y = []

symbol = 'X'

for line in file:
  if not symbol in line:
    continue
  else:
    splittedLine = line.split(' ')

  x.append(float(splittedLine[1].replace('X', '')))
  y.append(float(splittedLine[2].replace('Y', '')))

file.close()

print(x)
print(y)

plt.plot(x, y)
plt.show()
