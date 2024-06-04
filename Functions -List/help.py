# Help
# help()
# It return the documentation file of an object that we pass it

print(help(str))

# Help on class int in module builtins:

# class int(object)
#  |  int([x]) -> integer
#  |  int(x, base=10) -> integer
#  |
#  |  Convert a number or string to an integer, or return 0 if no arguments
#  |  are given.  If x is a number, return x.__int__().  For floating point
#  |  numbers, this truncates towards zero.
#  |
#  |  If x is not a number or if base is given, then x must be a string,
#  |  bytes, or bytearray instance representing an integer literal in the
#  |  given base.  The literal can be preceded by '+' or '-' and be surrounded
#  |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
#  |  Base 0 means to interpret the base from the string as an integer literal.
#  |  >>> int('0b100', base=0)
#  |  4
#  |
#  |  Built-in subclasses:
#  |      bool
#  |
#  |  Methods defined here:
#  |
#  |  __abs__(self, /)
#  |      abs(self)
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |
#  |  __and__(self, value, /)
#  |      Return self&value.
#  |
#  |  __bool__(self, /)
#  |      True if self else False
#  |
#  |  __ceil__(...)
#  |      Ceiling of an Integral returns itself.
#  |
#  |  __divmod__(self, value, /)
#  |      Return divmod(self, value).
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __float__(self, /)
#  |      float(self)
#  |
#  |  __floor__(...)
#  |      Flooring an Integral returns itself.
#  |
#  |  __floordiv__(self, value, /)
#  |      Return self//value.
#  |
#  |  __format__(self, format_spec, /)
#  |      Convert to a string according to format_spec.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __getnewargs__(self, /)
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __hash__(self, /)
#  |      Return hash(self).
#  |
#  |  __index__(self, /)
#  |      Return self converted to an integer, if self is suitable for use as an index into a list.
#  |
#  |  __int__(self, /)
#  |      int(self)
#  |
#  |  __invert__(self, /)
#  |      ~self
#  |
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |
#  |  __lshift__(self, value, /)
#  |      Return self<<value.
#  |
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |
#  |  __mod__(self, value, /)
#  |      Return self%value.
#  |
#  |  __mul__(self, value, /)
#  |      Return self*value.
#  |
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |
#  |  __neg__(self, /)
#  |      -self
#  |
#  |  __or__(self, value, /)
#  |      Return self|value.
#  |
#  |  __pos__(self, /)
#  |      +self
#  |
#  |  __pow__(self, value, mod=None, /)
#  |      Return pow(self, value, mod).
#  |
#  |  __radd__(self, value, /)
#  |      Return value+self.
#  |
#  |  __rand__(self, value, /)
#  |      Return value&self.
#  |
#  |  __rdivmod__(self, value, /)
#  |      Return divmod(value, self).
#  |
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |
#  |  __rfloordiv__(self, value, /)
#  |      Return value//self.
#  |
#  |  __rlshift__(self, value, /)
#  |      Return value<<self.
#  |
#  |  __rmod__(self, value, /)
#  |      Return value%self.
#  |
#  |  __rmul__(self, value, /)
#  |      Return value*self.
#  |
#  |  __ror__(self, value, /)
#  |      Return value|self.
#  |
#  |  __round__(...)
#  |      Rounding an Integral returns itself.
#  |
#  |      Rounding with an ndigits argument also returns an integer.
#  |
#  |  __rpow__(self, value, mod=None, /)
#  |      Return pow(value, self, mod).
#  |
#  |  __rrshift__(self, value, /)
#  |      Return value>>self.
#  |
#  |  __rshift__(self, value, /)
#  |      Return self>>value.
#  |
#  |  __rsub__(self, value, /)
#  |      Return value-self.
#  |
#  |  __rtruediv__(self, value, /)
#  |      Return value/self.
#  |
#  |  __rxor__(self, value, /)
#  |      Return value^self.
#  |
#  |  __sizeof__(self, /)
#  |      Returns size in memory, in bytes.
#  |
#  |  __sub__(self, value, /)
#  |      Return self-value.
#  |
#  |  __truediv__(self, value, /)
#  |      Return self/value.
#  |
#  |  __trunc__(...)
#  |      Truncating an Integral returns itself.
#  |
#  |  __xor__(self, value, /)
#  |      Return self^value.
#  |
#  |  as_integer_ratio(self, /)
#  |      Return a pair of integers, whose ratio is equal to the original int.
#  |
#  |      The ratio is in lowest terms and has a positive denominator.
#  |
#  |      >>> (10).as_integer_ratio()
#  |      (10, 1)
#  |      >>> (-10).as_integer_ratio()
#  |      (-10, 1)
#  |      >>> (0).as_integer_ratio()
#  |      (0, 1)
#  |
#  |  bit_count(self, /)
#  |      Number of ones in the binary representation of the absolute value of self.
#  |
#  |      Also known as the population count.
#  |
#  |      >>> bin(13)
#  |      '0b1101'
#  |      >>> (13).bit_count()
#  |      3
#  |
#  |  bit_length(self, /)
#  |      Number of bits necessary to represent self in binary.     
#  |
#  |      >>> bin(37)
#  |      '0b100101'
#  |      >>> (37).bit_length()
#  |      6
#  |
#  |  conjugate(...)
#  |      Returns self, the complex conjugate of any int.
#  |
#  |  is_integer(self, /)
#  |      Returns True. Exists for duck type compatibility with float.is_integer.
#  |
#  |  to_bytes(self, /, length=1, byteorder='big', *, signed=False) 
#  |      Return an array of bytes representing an integer.
#  |
#  |      length
#  |        Length of bytes object to use.  An OverflowError is raised if the
#  |        integer is not representable with the given number of bytes.  Default
#  |        is length 1.
#  |      byteorder
#  |        The byte order used to represent the integer.  If byteorder is 'big',
#  |        the most significant byte is at the beginning of the byte array.  If
#  |        byteorder is 'little', the most significant byte is at the end of the
#  |      signed                                                                                                                                                                         
#  |                                                                                                                                                                                     
#  |  Static methods defined here:                                                                                                                                                       
#  |                                                                                                                                                                                     
#  |  __new__(*args, **kwargs)                                                                                                                                                           
#  |                                                                                                                                                                                     
#  |  Data descriptors defined here:                                                                                                                                                     
#  |                                                                                                                                                                                     
#  |  denominator                                                                                                                                                                        
#  |      the denominator of a rational number in lowest terms                                                                                                                           
#  |                                                                                                                                                                                     
#  |  imag                                                                                                                                                                               
#  |      the imaginary part of a complex number                                                                                                                                         
#  |                                                                                                                                                                                     
#  |  numerator                                                                                                                                                                          
#  |      the numerator of a rational number in lowest terms                                                                                                                             
#  |
#  |  real
#  |      the real part of a complex number
