one_char = 4  # размер одного символа в байтах
pages = 100
lines = 50
chars = 25
diskette = 1.44

total_chars = chars * lines * pages
total_bytes = total_chars * one_char
disk_size = diskette * 1024 * 1024  # размер в байтах
num_books = int(disk_size // total_bytes)

print("Количество книг, помещающихся на дискету:", num_books)
