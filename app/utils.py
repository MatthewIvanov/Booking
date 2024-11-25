



def format_number_thousand_separator(
    number: int,
    separator: str = " ",
):
    return f"{number:,}".replace(",", separator)
