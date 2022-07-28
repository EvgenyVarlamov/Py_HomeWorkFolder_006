# Таблица умножения
def print_operation_table(operation, num_columns=9, num_rows=9):
    for col in range(1, num_columns+1):
        print()
        for row in range(1, num_rows+1):
            print(operation(col, row), end='\t')

    # print(*[operation(col,row) for col in range(1, num_columns+1) for row in range(1, num_rows+1)])


print_operation_table(lambda x, y: x*y, 6)
