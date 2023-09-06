from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self): # prints the value
        return str(self.value)
    
    def __repr__(self): #calling the object - prints the class with instance value
        return f'MutInt({self.value!r})'

    def __format__(self, fmt): # enables some shennanigans
        return format(self.value, fmt)
    
    # Implement the "+" operator. Forward operands (MutInt + other)
    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else: 
            return NotImplemented

    # Support for reversed operands (other + MutInt)  
    __radd__ = __add__

    # Support for in-place update (MutInt += other)
    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else: 
            return NotImplemented
    
    # Support for equality testing
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else: 
            return NotImplemented
        
    # One relation(comparison ex equality operator & more than) is needed for @total_ordering decorator. It fills in others
    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
    
    # Conversions to int() and float()
    def __int__(self):
        return self.value
    
    __index__ = __int__     # Make indexing work
    
    def __float__(self):
        return float(self.value)