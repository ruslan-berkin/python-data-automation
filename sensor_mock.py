"""
Скрипт: sensor_mock.py
Описание: Генератор "сырых" данных с виртуального датчика температуры.
Имитирует непрерывный поток данных для тестирования систем АСУ ТП.
"""

import random

def generate_sensor_data(num_samples=100, interval=0.1, base_temp=23.5, sensor_id=1):
    """
    Генерирует список словарей с показаниями датчика.
    
    :param num_samples: Количество записей (точек данных)
    :param interval: Временной шаг между записями (в секундах)
    :param base_temp: Стартовая температура
    :param sensor_id: Уникальный идентификатор датчика
    :return: Список словарей вида {'time': float, 'value': float, 'sensor_id': int}
    """
    sensor_data = []
    current_time = 0.0
    current_temp = base_temp
    
    for _ in range(num_samples):
        # Имитируем физический процесс: температура меняется плавно
        # Добавляем случайное колебание от -0.2 до 0.2 градуса на каждом шаге
        fluctuation = random.uniform(-0.2, 0.2)
        current_temp += fluctuation
        
        # Формируем запись 
        record = {
            'time': round(current_time, 2),
            'value': round(current_temp, 2),
            'sensor_id': sensor_id
        }
        
        sensor_data.append(record)
        
        # Увеличиваем время для следующего шага
        current_time += interval
        
    return sensor_data

# --- Блок тестирования скрипта ---
if __name__ == "__main__":
    # Генерируем 10 записей с датчика №1, начиная с 25.0 градусов
    raw_data = generate_sensor_data(num_samples=10, interval=0.1, base_temp=25.0, sensor_id=1)
    
    print(f"Сгенерировано записей: {len(raw_data)}")
    print("Пример первых 5 полученных значений:")
    
    for entry in raw_data[:5]:
        print(entry)
