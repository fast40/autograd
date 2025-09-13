class Number:
    def __init__(self, value, operator='', operands=[]):
        self.value = value
        self.grad = 0
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return f'Number(value={self.value})'

    def __add__(self, other):
        return Number(self.value + other.value, operator='add', operands=[self, other])

    def __sub__(self, other):
        return Number(self.value - other.value, operator='sub', operands=[self, other])

    def __mul__(self, other):
        return Number(self.value * other.value, operator='mul', operands=[self, other])

    def __div__(self, other):
        return Number(self.value / other.value, operator='div', operands=[self, other])
    
    def backward(self):
        if self.operator == 'mul':
            self.operands[0].grad = self.grad * self.operands[1].value
            self.operands[1].grad = self.grad * self.operands[0].value

        for operand in self.operands():
            operands.backward()
        print('backward pass!')
        print('need to set the grad of everything in the past')



if __name__ == '__main__':
    n1 = Number(5)
    n2 = Number(2)
    n3 = Number(3)

    print(n1 * n2)

    L = n1 * n2
    L2 = n1 * n3
    L.backward()
    print(n1.grad)
    print(n2.grad)
    print(L.grad)




# when I say L.backward(), what happens?
# I probably should do a manual backward pass.
# but I want the .grad of everything that was used to make this value to be equal to Dvalue/d_thatthing
# Ok so L needs to set the grad of the things in its past. Because everything upstream of L doesn't know about L at all. So how would it know what to do?
# well, maybe you could say a given tensor can only be used in one operation. I mean that's super limiting, but maybe you could get away with that. worth looking into.




"""
so each Number needs to keep track of the Numbers that went into it.
And the operation that was used.

operations only work on two tensors.
Or one I guess.
"""
