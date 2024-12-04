class RomanConverter:
    def __init__(self):
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, roman):
        total = 0
        prev_value = 0

        for symbol in reversed(roman):
            value = self.roman_numerals[symbol]

            if value >= prev_value:
                total += value
            else:
                total -= value

            prev_value = value

        return total


converter = RomanConverter()
roman_number = "XV" 
integer_value = converter.roman_to_int(roman_number)
print(f"Số La Mã {roman_number} chuyển thành số nguyên là: {integer_value}")
