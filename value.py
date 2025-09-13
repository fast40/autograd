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
    
    def backward(self, root=True):
        # we need to know the derivative of each operator. that needs to be somewhere.
        # ok lets just do it for mul

        """
        L = loss
        this = this Number
        grad = dL/dthis
        we want dthis/doperator for operator in operators
        then we multiply that by this.grad to get dL/dthis * dthis/do = dL/do
        then we assign that value into the grad field of the operators
        then we call backward on them.
        """

        if root:
            self.grad = 1

        if self.operator == 'mul':
            self.operands[0].grad += self.grad * self.operands[1].value
            self.operands[1].grad += self.grad * self.operands[0].value
        elif self.operator == 'add':
            self.operands[0].grad += self.grad
            self.operands[1].grad += self.grad

        for operand in self.operands:
            operand.backward(root=False)

        # print('backward pass!')
        # print('need to set the grad of everything in the past')



if __name__ == '__main__':
    n1 = Number(5)
    n2 = Number(2)
    n3 = Number(3)

    print(n1 * n2)

    # L1 = n1 * n2
    # L2 = L1 * n3

    # L2 = (n1 + n2) * n3
    L2 = (n1 + n1 + n1) * n1
    L2.backward()
    print('n1 grad (should be 6)', n1.grad)
    print('n2 grad (should be 15)', n2.grad)
    print('n3 grad (should be 10)', n3.grad)
    print('L2 grad (should be 1 obviously)', L2.grad)




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
