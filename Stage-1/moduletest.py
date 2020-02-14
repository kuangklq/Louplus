import sys
import os

sys.path.append('/home/shiyanlou')

from louplus.test.hello import message


print('Python 引入对象的路径：')
for path in sys.path:
    print('\t', os.path.abspath(path))
print(message)
