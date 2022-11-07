class Validations:

    def search_validation(self, value: str) -> bool:
        if len(value) < 3 or any(char.isdigit() for char in value):
            return False
        return True
