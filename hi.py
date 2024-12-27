    if direction == 1 and y_value > 0 - blockSize:
        snake_location.clear()
        for i in range(0, tail_length):
            snake_location.insert(0, x_value)
            snake_location.insert(1, y_value - blockSize * i)
        y_value -= blockSize
    if direction == 2 and y_value < WINDOW_HEIGHT:
        snake_location.clear()
        for i in range(0, tail_length):
            snake_location.insert(0, x_value)
            snake_location.insert(1, y_value + blockSize * i)
        y_value += blockSize
    if direction == 3 and x_value > 0 - blockSize:
        snake_location.clear()
        for i in range(0, tail_length):
            snake_location.insert(0, x_value - blockSize * i)
            snake_location.insert(1, y_value)
        x_value -= blockSize
    if direction == 4 and x_value < WINDOW_WIDTH:
        snake_location.clear()
        for i in range(0, tail_length):
            snake_location.insert(0, x_value + blockSize * i)
            snake_location.insert(1, y_value)
        x_value += blockSize

        