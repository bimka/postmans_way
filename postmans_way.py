# Входные данные
points_coord = ((0,2), (2, 5), (5, 2), (6, 6), (8, 3))

def shortest_way(points_coord: tuple) -> str:
    """Функция shortest_way() возвращает строку, показывающую координаы
    ближайших графов и расстояние между ними"""

    matrix_size = len(points_coord) 
    matrix = []

    # Сразу добавим первую координату, из которой выйдет почтальон
    postmans_way = f'{points_coord[0]} --> '

    # Создамим матрицу с расстояниями между точками
    # Добавим строки матрицы
    for row in range(matrix_size):
        # Добавим столбцы матрицы
        matrix_row = []
        for column in range(matrix_size):
            dist = ((points_coord[column][0] - points_coord[row][0])**2 + 
                    (points_coord[column][1] - points_coord[row][1])**2)**0.5
            matrix_row.append(dist)
        matrix.append(matrix_row)

    # Будем для каждой строки начинаяя с первой (координата Почтового 
    # отделения) находить минимальное значение строки (расстояние между 
    # точками), добавлять в строку postmans_way координаты точек и расстояние
    # между ними, далее транспонировать матрицу и также находить минимильное 
    # значение строки
    i = 0
    row_min_val_index = 0
    positions = [0]
    way_len = 0
    while i < matrix_size - 1:
        # Находим минимальное значение строки
        row_min_val = sorted(matrix[positions[-1]])
        row_min_val = min([j for j in row_min_val if j != 0])

        # Добавим расстояние между точкими к общему расстоянию
        way_len += row_min_val

        # Найдем индекс минимального значения в строке
        row_min_val_index = matrix[row_min_val_index].index(row_min_val) 

        # Обнулим обработанную строку   
        matrix[positions[-1]] = [0 for j in range(len(matrix[row_min_val_index]))]

        # Транспонируем матрицу
        matrix = [[matrix[row][col] for row in range(len(matrix))] for col in  range(len(matrix[0]))]
        ola = points_coord[row_min_val_index]

        # Добавим полученные значения в строку ответа
        postmans_way += f'{ola}  [{way_len}] --> ' 
        positions.append(row_min_val_index)
        i += 1

    # Почтальон дошел до конечной точки, топерь ему необходимо 
    # вернуться в начало пути
    first_point = points_coord[0]
    last_point = points_coord[positions[-1]]
    dist = ((last_point[0] - first_point[0])**2 + 
            (last_point[1] - first_point[1])**2)**0.5
    way_len += dist

    # Добавим полученные значения в строку ответа
    postmans_way += f'{points_coord[0]} [{way_len}] = {way_len}'
        
    return postmans_way

# Вызов функции
print(shortest_way(points_coord))