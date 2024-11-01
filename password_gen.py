from random import choice, shuffle

# default ASCII
def password_generator(
    num_of_lower: int = 1,
    num_of_capital: int = 1,
    num_of_spec_chars: int = 1,
    include_non_printable: bool = False,
    num_of_digits: int = 1,
    random_order: bool = True) -> str:
    lower = [chr(choice(range(97, 123))) for _ in range(num_of_lower)]
    capital = [chr(choice(range(65, 91))) for _ in range(num_of_capital)]
    special = [chr(choice(list((set(range(32, 48)) | set(range(58, 65)) | set(range(91, 97)) | set(range(123, 127))) ^ (set(range(32), 127) if include_non_printable else set())))) for char in range(num_of_spec_chars)]
    digits = [chr(choice(range(48, 58))) for _ in range(num_of_digits)]
    chars = lower + capital + special + digits
    password = []
    # Python pozwala na operacje logiczne między zbiorami zbiorami (setami).
    for char in chars:
        password += [char]
    if random_order:
        shuffle(password)
    return ''.join(password)

print(password_generator(4, 4, 4, False, 4, True))
