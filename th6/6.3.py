print('sinh vien: Nguyễn Bá Hoàng Hiếu')
print('mssv:235752021610036')
print('##########')

class Nguoi:
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

aNam = Nam()
aNu = Nu()

print(aNam.getGender())  
print(aNu.getGender())   
