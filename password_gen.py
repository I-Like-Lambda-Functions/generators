from random import choice, shuffle, randint

# default ASCII
def password_generator(num_of_lower: int = 1, num_of_capital: int = 1, num_of_spec_chars: int = 1, include_non_printable: bool = False, num_of_digits: int = 1, random_order: bool = True) -> str:
    spec_chars_list = list(
        (set(range(32, 48)) |
         set(range(58, 65)) |
         set(range(91, 97)) |
         set(range(123, 127))) ^
        (set(range(32), 127) if include_non_printable else set())
    )
    lower = [chr(randint(97, 122)) for _ in range(num_of_lower)]
    capital = [chr(randint(65, 90)) for _ in range(num_of_capital)]
    # Python pozwala na operacje logiczne między zbiorami zbiorami (setami).
    special = [chr(choice(spec_chars_list)) for _ in range(num_of_spec_chars)]
    digits = [chr(randint(48, 57)) for _ in range(num_of_digits)]
    password = lower + capital + special + digits
    if random_order: shuffle(password)
    return ''.join(password)

assert len(password_generator(4, 4, 4, False, 4, True)) == 16
assert len(password_generator(1, 1, 2, False, 10, False)) == 14
