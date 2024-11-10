storage = 1.44
pages = 100
strings_per_page = 50
symbols_per_string = 25
symbol_weight = 4
total_symbols = pages * strings_per_page * symbols_per_string
book_weight = total_symbols * symbol_weight
total_books = storage * 1024 ** 2 // book_weight
print("Количество книг, помещающихся на дискету:", int(total_books))
