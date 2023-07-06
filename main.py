# Размеры куба (в мм)
cubeLength = 10
cubeWidth = 10
cubeHeight = 10

# Настройки 3D-принтера
extruderTemp = 230  # Температура экструдера
bedTemp = 110  # Температура стола
layerHeight = 0.2 # Высота слоя
extrudedMaterialWidth = 0.4 # Ширина выдавливаемого материала

# Открываем файл для записи GCode
gcodeFile = open("cube-l%s-w%s-h%s.gcode" % (cubeLength, cubeWidth, cubeHeight), "w")

# Функция для вычисления к-ва слоев
def calcLayerCount(cubeHeight, layerHeight):
    return cubeHeight / layerHeight

# Функция для вычисления начального X
def calcX0(cubeWidth, extrudedMaterialWidth):
    return (0 - cubeWidth) / 2 - extrudedMaterialWidth / 2

# Функция для вычисления начального Y
def calcY0(cubeLength, extrudedMaterialWidth):
    return (0 - cubeLength) / 2 - extrudedMaterialWidth / 2

# Функция для вычисления начального Z
def calcZ0(layerHeight):
    return 0 + layerHeight

# Функция для записи команды в файл GCode
def writeGcodeCommand(gcodeCommand):
    gcodeFile.write(gcodeCommand + "\n")
                
# Начало программы GCode
def header():
    writeGcodeCommand("; Header")
    writeGcodeCommand("M136") # Enable build
    writeGcodeCommand("M73 P0")
    writeGcodeCommand("G162 X Y F2000") # Home XY axes maximum
    writeGcodeCommand("G161 Z F900") # Home Z axis minimum
    writeGcodeCommand("G92 X0 Y0 Z-5 A0 B0") # Set Z to -5
    writeGcodeCommand("G161 Z F100") # Home Z axis minimum
    writeGcodeCommand("M132 X Y Z A B") # Recall stored home offsets for XYZAB axis
    writeGcodeCommand("G92 X152 Y72 Z0 A0 B0")
    writeGcodeCommand("G1 X-112 Y-73 Z150 F3300.0") # Move to waiting position
    writeGcodeCommand("G130 X20 Y20 A20 B20") # Lower stepper Vrefs while heating
    writeGcodeCommand("M109 S110 T0")
    writeGcodeCommand("M134 T0")
    writeGcodeCommand("M135 T0")
    writeGcodeCommand("M104 S230 T0")
    writeGcodeCommand("M133 T0")
    writeGcodeCommand("G130 X127 Y127 A127 B127") # Set Stepper motor Vref to defaults
    writeGcodeCommand("G1 X105.400 Y-74.000 Z0.270 F9000.000") # Extruder Prime Dry Move
    writeGcodeCommand("G1 X-112 Y-73 Z0.270 F1800.000 E25.000") # Extruder Prime Start
    writeGcodeCommand("G92 A0 B0") # Reset after prime
    writeGcodeCommand("G1 Z0.000000 F1000")
    writeGcodeCommand("G1 X-112.0 Y-73.0 Z0.0 F1000 E0.0")
    writeGcodeCommand("G92 E0")
    writeGcodeCommand("G1 X-112.000 Y-73.000 Z0.000 F1500 A-1.30000") # Retract
    writeGcodeCommand("G1 X-112.000 Y-73.000 Z0.000 F3000") # Retract
    writeGcodeCommand("G1 X-112.000 Y-73.000 Z0.300 F1380") # Travel Move

# Завершение программы GCode
def tail():
    writeGcodeCommand("; Footer")
    writeGcodeCommand("G1 X3.827 Y4.114 Z10.970 F1500 A325.69237") # Retract
    writeGcodeCommand("M127 T0") # Fan off
    writeGcodeCommand("M18 A B") # Turn off A and B Steppers
    writeGcodeCommand("G1 Z155 F900")
    writeGcodeCommand("G162 X Y F2000")
    writeGcodeCommand("M18 X Y Z") # Turn off steppers after a build
    writeGcodeCommand("M109 S0 T0")
    writeGcodeCommand("M104 S0 T0")
    writeGcodeCommand("M73 P100") # End  build progress
    writeGcodeCommand("M70 P5") # We <3 Making Things!
    writeGcodeCommand("M72 P1 ") # Play Ta-Da song
    writeGcodeCommand("M137") # Build end notification

def generateCubeGcode(cubeLength, cubeWidth, cubeHeight):
    writeGcodeCommand("; Main")

    layers = int(calcLayerCount(cubeHeight, layerHeight))

    # x0 = calcX0(cubeWidth, extrudedMaterialWidth)
    # y0 = calcY0(cubeLength, extrudedMaterialWidth)
    z0 = calcZ0(layerHeight)

    currentLayer = z0

    for layer in range(layers):
        for x in range(0, cubeWidth + 1):
            writeGcodeCommand("G1 X%s Y%s Z%s ; Travel Move" % (x, 0, round(currentLayer, 1)))
            writeGcodeCommand("G1 X%s Y%s Z%s" % (x, cubeLength, round(currentLayer, 1)))

        currentLayer += layerHeight

    # writeGcodeCommand("G1 X0 Y0")
    # writeGcodeCommand("G1 X0 Y10")
    # writeGcodeCommand("G1 X4 Y0")
    # writeGcodeCommand("G1 X4 Y10")
    # writeGcodeCommand("G1 X8 Y0")
    # writeGcodeCommand("G1 X8 Y10")
    # writeGcodeCommand("G1 X12 Y0")
    # writeGcodeCommand("G1 X12 Y10")
    # writeGcodeCommand("G1 X16 Y0")
    # writeGcodeCommand("G1 X16 Y10")

header()
generateCubeGcode(cubeLength, cubeWidth, cubeHeight)
tail()

# Закрытие файла GCode
gcodeFile.close()

print("GCode сгенерирован и сохранен в файле cube-l%s-w%s-h%s.gcode" % (cubeLength, cubeWidth, cubeHeight))
