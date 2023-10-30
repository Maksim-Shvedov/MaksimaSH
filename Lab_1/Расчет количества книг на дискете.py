# TODO Найдите количество книг, которое можно разместить на дискете
total_capacity = 1.44 # Объем дискеты
page_per_book = 100 # Страниц в книге
strings_per_page_ = 50 # Строк в страницу
character_per_string = 25 # Символов в строке
character_capacity = 4 # Объем символа
capacity_of_one_book = (character_capacity * character_per_string * strings_per_page_ * page_per_book) # Объем одной книги
total_capacity_B = total_capacity * 1024 * 1024 # Объем книги в Байтах
quantities_of_book = total_capacity_B / capacity_of_one_book # Количество книг
print("Количество книг, помещающихся на дискету:", round(quantities_of_book))
