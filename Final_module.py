from two_column_text_read import two_column_text_read, x_column, y_column

str = two_column_text_read('volumes_energies.txt')

x= x_column(str)
print(x)