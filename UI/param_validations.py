def search_validation(value: str) -> bool:
    if len(value) < 3 or any(char.isdigit() for char in value):
        raise ValueError ("didn't pass validation, please enter a search string with more than two characters and without any digits")
