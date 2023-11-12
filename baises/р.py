import csv
from datetime import datetime

# Открываем CSV файл для чтения с разделителем пробела
with open('order.csv', 'r', newline='') as infile:
    reader = csv.reader(infile, delimiter=' ')
    header = next(reader)  # Пропускаем заголовок

    # Открываем CSV файл для записи с разделителем пробела
    with open('res1.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=' ')

        # Записываем заголовок в выходной файл
        writer.writerow(header)

        # Итерируемся по строкам и фильтруем по датам
        for row in reader:
            date_str = row[0]  # Предполагаем, что дата находится в первой колонке
            data = row[1]  # Предполагаем, что данные находятся во второй колонке

            # Преобразуем строку даты в объект datetime
            date = datetime.strptime(date_str, '%Y-%m-%d')  # Предполагаем формат даты YYYY-MM-DD

            # Проверяем, что дата находится в январе, феврале или марте 2023 года
            if date.year == 2023 and date.month in (3, 5):
                # Записываем данные в выходной файл
                writer.writerow([date_str, data])
