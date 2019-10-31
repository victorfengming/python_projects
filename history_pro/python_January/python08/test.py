a = "sjkda"
b = "sjkda"
c = "jhsdagk"

print("a的地址", id(a))
print("b的地址", id(b))
print("c的地址", id(c))
b = a + 'asdgf'
# a,b = b,a+b
print("a的地址", id(a))
print("b的地址", id(b))
print("c的地址", id(c))
