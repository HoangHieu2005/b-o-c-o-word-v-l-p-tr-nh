print("Sinh vien:Nguyễn Bá Hoàng Hiếu")
print("Mssv:235752021610036")
n = int(input("Nhập số dòng n: "))
def pascal_triangle(n):
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = row[j - 1] + row[j]
        print(row)
pascal_triangle(n)
