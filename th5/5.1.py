print('sinh vien: Nguyễn Bá Hoàng Hiếu')
print('mssv:235752021610036')
print('##########')

import mymath # Note no .py
values = [2,4,6,8,10]
print('Squares:')
for v in values:
    print(mymath.square(v))
print('Cubes:')
for v in values:
    print(mymath.cube(v))
print('Average: ' + str(mymath.average(values)))
