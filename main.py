# Размеры куба (в мм)
length = 10
width = 10
height = 10

# Настройки 3D-принтера
extruder_temp = 200  # Температура сопла
bed_temp = 60  # Температура стола

# Открываем файл для записи GCode
gcode_file = open("cube.gcode", "w")

# Функция для записи команды в файл GCode
def write_command(command):
    gcode_file.write(command + "\n")

# Начало программы GCode
write_command("; Start program")
write_command("M140 S" + str(bed_temp))  # Запустить прогрев столика до указанной температуры и немедленно перейти к выполнению следующих команд
write_command("M105") # Получить текущую температуру экструдера
write_command("M190 S" + str(bed_temp))  # Установить температуру столика и ждать полного прогрева перед выполнением следующих команд
write_command("M104 S" + str(extruder_temp)) # Установить температуру хотэнда и немедленно перейти к следующей команде
write_command("M105") # Получить текущую температуру экструдера
write_command("M109 S" + str(extruder_temp)) # Установить температуру хотэнда и ждать прогрева
write_command("G28") # Перемещение в начало ("домой")
write_command("G1 Z15.0 F6000") # Перемещение платформы вниз на 15 мм
write_command("G92 E0")
write_command("G1 F200 E3")
write_command("G92 E0")
write_command("G92 E0")
write_command("G92 E0")
write_command("G1 F1500 E-6.5")

write_command("\n")

for z in range(1, height + 1):
    for x in range(width):
        write_command("G1 X%d Y%d" % (x, length))
        write_command("G0 X%d Y%d" % (x + 1, 0))

    write_command("G0 X0 Y0 Z%d ; new layer" % (z))

write_command("\n")

# Завершение программы GCode
write_command("M140 S0")
write_command("M107") 
write_command("M104 S0")
write_command("M140 S0")
write_command("G92 E1")
write_command("G1 E-1 F300")
write_command("G28 X0 Y0")
write_command("M84")
write_command("M82")
write_command("M104 S0")

# Закрытие файла GCode
gcode_file.close()

print("Программа GCode для создания куба сгенерирована и сохранена в файле cube.gcode")
