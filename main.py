# Импортирование библиотеки для работы с GCode
from math import pi

# Размеры куба (в мм)
length = 10
width = 10
height = 10

# Настройки 3D-принтера
extruder_temp = 130  # Температура сопла
bed_temp = 220  # Температура стола
feedrate = 4600  # Скорость движения подачи материала

# Открываем файл для записи GCode
gcode_file = open("cube.gcode", "w")

# Функция для записи команды в файл GCode
def write_command(command):
    gcode_file.write(command + "\n")

# Начало программы GCode
write_command("; Начало программы")
write_command("G21") # Установка единиц измерения в миллиметрах
write_command("G90") # Установка абсолютных координат
# write_command("M109 S" + str(extruder_temp))  # Установка температуры сопла и ждать, пока разогреется
# write_command("M104 S" + str(bed_temp))  # Установка температуры стола и не ждать, пока разогреется
# write_command("G28 ; Home all axes")  # Возврат всех осей в начальную позицию
# write_command("G92 E0 ; Reset extruder")  # Сброс экструдера
# write_command("G1 F" + str(feedrate))  # Установка скорости подачи материала
write_command("G0 Z0")
write_command("G0 X0 Y0")

write_command("\n")

for z in range(1, height + 1):
    for x in range(width):
        write_command("G1 X%d Y%d" % (x, length))
        write_command("G0 X%d Y%d" % (x + 1, 0))

    write_command("G0 X0 Y0 Z%d ; new layer" % (z))
    # write_command("G0 X0 Y0")


write_command("\n")

# Завершение программы GCode
write_command("G1 F200 E10")  # Подача материала (конец)
write_command("M104 S0 ; Отключение обогревателя сопла")
write_command("M140 S0 ; Отключение обогревателя стола")
write_command("G92 E0 ; Сброс экструдера")
write_command("G28 ; Возврат всех осей в начальную позицию")
write_command("M84 ; Отключение моторов")

# Закрытие файла GCode
gcode_file.close()

print("Программа GCode для создания куба сгенерирована и сохранена в файле cube.gcode")