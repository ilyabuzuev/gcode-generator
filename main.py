import math

# Задание параметров куба
cub_side_length = 10.0    # Длина стороны куба в мм
cub_height = 5.0          # Высота куба в мм
layer_height = 0.2        # Высота слоя в мм
feed_rate = 500           # Скорость подачи в мм/мин

# Рассчёт количества шагов для двигателей в каждом направлении
steps_per_mm = 200       # Шагов на мм для 3д принтера
x_steps = int(cub_side_length * steps_per_mm)
y_steps = int(cub_side_length * steps_per_mm)
z_steps = int(cub_height * steps_per_mm)

# Настройка начальной точки и скорости перемещения
start_x = 0
start_y = 0
start_z = 0
start_feed_rate = 0

# Создание заголовка G-кода (определение начальной точки, метрическая система, скорость и т.д.)
gcode = "G21 ; Установка в метрическую систему\n"
gcode += "G90 ; Абсолютные координаты\n"
gcode += "G1 F%d ; Установка скорости подачи\n" % feed_rate
gcode += "M107 ; Остановка обдува\n"
gcode += "G28 X Y Z ; Выход в стартовую точку\n"

# Создание G-кода для каждого куба
for z in range(0, z_steps, int(layer_height * steps_per_mm)):
    end_x = start_x + x_steps
    end_y = start_y + y_steps

    # Движение по оси Z
    gcode += "G1 X%d Y%d Z%d F%d\n" % (start_x, start_y, z / steps_per_mm, feed_rate)

    # Создание контура куба
    gcode += "G1 X%d Y%d F%d\n" % (end_x, start_y, feed_rate)
    gcode += "G1 X%d Y%d F%d\n" % (end_x, end_y, feed_rate)
    gcode += "G1 X%d Y%d F%d\n" % (start_x, end_y, feed_rate)
    gcode += "G1 X%d Y%d F%d\n" % (start_x, start_y, feed_rate)
    gcode += "G1 X%d Y%d F%d\n" % (end_x, start_y, feed_rate)

    # Подъем на следующий слой
    gcode += "G1 Z%d ; Подъем на следующий слой\n" % ((z + int(layer_height * steps_per_mm)) / steps_per_mm)

# Завершение работы и сохранение файла G-кода
gcode += "M107 ; Остановка обдува\n"
gcode += "G28 X Y Z ; Выход в стартовую точку\n"
gcode += "M84 ; Остановка двигателей\n"

# Сохранение файла G-кода
file_name = "cube_%d_%d.gcode" % (cub_side_length, cub_height)
with open(file_name, "w") as gcode_file:
    gcode_file.write(gcode)

print("G-код создан и сохранён в файле %s" % file_name)
