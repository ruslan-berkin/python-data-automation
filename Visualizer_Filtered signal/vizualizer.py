import numpy as np
import matplotlib.pyplot as plt

# --- 1. ЧТЕНИЕ ДАННЫХ ИЗ CSV ---
# Указываем путь к нашему лог-файлу
file_path = '/Users/gumball/Documents/SelfStudy/matplotlib/motor_logs.csv'

# Читаем матрицу.
data = np.loadtxt(file_path, delimiter=',', skiprows=1)

# Разделяем матрицу на два одномерных массива (оси X и Y)
t = data[:, 0]
noisy_signal = data[:, 1]

# --- 2. ФИЛЬТРАЦИЯ СИГНАЛА ---
window_size = 15
weights = np.ones(window_size) / window_size

# Применяем фильтр. mode='same' сохраняет исходную длину массива t
filtered_signal = np.convolve(noisy_signal, weights, mode='same')

# --- 3. ПОСТРОЕНИЕ ГРАФИКА ---
plt.figure(figsize=(12,6))

# Рисуем зашумленный сигнал, 
plt.plot(t, noisy_signal, color='gray', alpha=0.4, label='Сырые данные (Шум)')

#Рисуем чистый сигнал
plt.plot(t, filtered_signal, color='blue', linewidth=2.5, label='Отфильтрованный сигнал (Чистый)')

# --- Оформление ---
plt.title('Обработка логов мотора: Подавление высокочастотного шума')
plt.xlabel('Время(с)')
plt.ylabel('Амплитуда сигнала (B)')
plt.grid(True)
plt.legend()

# --- Сохранение и вывод ---
# Save image in the same folder
save_img_path = '/Users/gumball/Documents/SelfStudy/matplotlib/filtered_analysis.png'
plt.savefig(save_img_path, dpi=300, bbox_inches='tight')
print(f"Готово! График сохранен в: {save_img_path}")

plt.show()
