# Is Sub Class

# issubclass()
class A:
    pass
class B:
    pass
class C(B):
    pass
class D(C):
    pass
class E(A):
    pass
class F(D):
    pass


# Now Check If they are really the sub class of other or not


print(issubclass(A,B))
print(issubclass(B,D))
print(issubclass(E,A))
print(issubclass(E,F))
print(issubclass(C,B))
print(issubclass(C,E))
print(issubclass(F,D))
print(issubclass(D,B))
# Output
False
False
True
False
True
False
True
True