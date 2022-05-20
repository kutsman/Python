class Complex:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __add__(self, other):
        a = Complex.list_number(self.number)[0] + Complex.list_number(other.number)[0]
        b = Complex.list_number(self.number)[1] + Complex.list_number(other.number)[1]
        return Complex(str(a) + '+' + str(b) + 'i' if b >= 0 else str(a) + str(b) + 'i')

    def __mul__(self, other):
        x1, y1 = Complex.list_number(self.number)
        x2, y2 = Complex.list_number(other.number)
        a = x1 * x2 - y1 * y2
        b = x1 * y2 + x2 * y1
        return Complex(str(a) + '+' + str(b) + 'i' if b >= 0 else str(a) + str(b) + 'i')

    @staticmethod
    def list_number(number):
        number = number.replace('i', '')
        if '+' in number:
            new_number = number.split('+')
            # print(number.split('+'))
        else:
            new_number = number.split('-')
            if number[0] == '-':
                new_number.pop(0)
                new_number[0] = '-' + new_number[0]
            new_number[1] = '-' + new_number[1]
        return tuple(map(int, new_number))


number1 = Complex('11+5i')
number2 = Complex('7+3i')
print(number1 + number2)
print(number1 * number2)
