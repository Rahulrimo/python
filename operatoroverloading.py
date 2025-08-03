class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
        
    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    
c1 = complex(2, 3)
c2 = complex(4, 5)
c3 = c1 + c2
print(c3.real,"+ i" ,c3.imag)  # Output: 6 8