import matplotlib.pyplot as plt

cellSize = 3

def fillLayer(width, length):
  xCoords = []
  yCoords = []

  big = cellSize
  mid = big * 2 / 3
  small = big - mid

  x0 = 0
  y0 = 0

  for line in range(width):
    currentX = x0
    currentY = y0

    if (line % 2 == 0):
      for cell in range(length):
        # начало
        xCoords.append(currentX)
        yCoords.append(currentY)

        # большая линия вверх
        x = currentX
        y = big

        currentX = x
        currentY += y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # большая линия вправо
        x = big
        y = currentY

        currentX += x
        currentY = y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # средняя линия вниз
        x = currentX
        y = mid

        currentX = x
        currentY -= y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # малая линия влево
        x = small
        y = currentY

        currentX -= x
        currentY = y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # малая линия вверх
        x = currentX
        y = small

        currentX = x
        currentY += y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # малая линия влево
        x = small
        y = currentY

        currentX -= x
        currentY = y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # средняя линия вниз
        x = currentX
        y = mid

        currentX = x
        currentY -= y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # большая линия вправо
        x = big
        y = currentY

        currentX += x
        currentY = y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # ячейка построена

    else:
      for cell in range(length):
        # начало
        xCoords.append(currentX)
        yCoords.append(currentY)

        # большая линия вверх
        x = currentX
        y = big

        currentX = x
        currentY += y


        xCoords.append(currentX)
        yCoords.append(currentY)

        # большая линия влево
        x = big
        y = currentY

        currentX -= x
        currentY = y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # средняя линия вниз
        x = currentX
        y = mid

        currentX = x
        currentY -= y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # малая линия вправо
        x = small
        y = currentY

        currentX += x
        currentY = y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # малая линия вверх
        x = currentX
        y = small

        currentX = x
        currentY += y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # малая линия вправо
        x = small
        y = currentY

        currentX += x
        currentY = y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # средняя линия вниз
        x = currentX
        y = mid

        currentX = x
        currentY -= y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # большая линия влево
        x = big
        y = currentY

        currentX -= x
        currentY = y

        xCoords.append(currentX)
        yCoords.append(currentY)

        # ячейка построена
      
    # переход на новую линию
    y0 = max(yCoords) + small
    x0 = currentX

    xCoords.append(currentX)
    yCoords.append(currentY)
    

  return xCoords, yCoords



# def main():
#     num_loops = 14
#     loop_width = 30
#     loop_height = 80

#     coordinates = generate_meander_coordinates(num_loops, loop_width, loop_height)
#     plot_meander(coordinates)

# if __name__ == "__main__":
#     main()

xCrds, yCrds = fillLayer(36, 36)

print( xCrds )
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print( yCrds )

plt.plot(xCrds, yCrds)
plt.show()
