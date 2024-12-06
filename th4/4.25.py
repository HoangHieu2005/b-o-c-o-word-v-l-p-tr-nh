print("Sinh vien:Nguyễn Bá Hoàng Hiếu")
print("Mssv:235752021610036")
numbers = input("Nhập các số, phân tách bằng dấu phẩy: ").split(',')
odd_numbers = [int(num) for num in numbers if int(num) % 2 != 0]
print(",".join(map(str, odd_numbers)))
