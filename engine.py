
"""
Скрипт: engine.py
Описание: Моделирование сигнала мотора и зашумления данных датчика.
Демонстрирует генерацию временных рядов, работу с атрибутом shape 
и поэлементные математические операции над массивами NumPy, 
а также визуализацию результатов с помощью Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Создаем вектор времени (как задание шага симуляции)
t = np.linspace(0, 10, 500)

# 2. Генерируем чистый сигнал мотора
amplitude = 2.0
clean_signal = amplitude * np.sin(t)

# 3. Генерируем шум (вибрацию)
# np.random.normal(среднее, стандартное_отклонение, размер)
noise_level = 0.5
noise = np.random.normal(0, noise_level, t.shape)

# 4. Складываем сигнал и шум
# Здесь применяется поэлементная операция сложения массивов одинаковой формы.
# Каждый элемент шума прибавляется к соответствующему элементу синусоиды.
noisy_signal = clean_signal + noise

# --- Блок визуализации  ---
plt.figure(figsize=(10, 5))

# Строим зашумленный сигнал
plt.plot(t, noisy_signal, label='Сигнал с шумом датчика', color='red', alpha=0.6)

# Строим чистый сигнал поверх (синий)
plt.plot(t, clean_signal, label='Идеальный сигнал мотора', color='blue', linewidth=2)

plt.title('Моделирование вибрации мотора')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)
plt.show()

# --- Добавляем экспорт данных в CSV ---
# Склеиваем массивы времени и зашумленного сигнала
log_data = np.column_stack((t, noisy_signal))

# Сохраняем в файл. 
np.savetxt('motor_logs.csv', log_data, delimiter=',', header='time,signal', comments='')
print("Данные успешно сохранены в motor_logs.csv")
