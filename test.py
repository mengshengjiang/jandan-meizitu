import os

a = 'c:' # removed slash
b = 'myFirstDirectory' # removed slash
c = 'mySecondDirectory'
d = 'myThirdDirectory'
e = 'myExecutable.exe'

print(os.path.join(a, b, c, d, e))
print(os.sep)