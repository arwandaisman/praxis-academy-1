class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

s = Student('Swaroop', 25, 75) 
#sudah memanggil class student dengan parameter dikirim pada school member
t = Teacher('Mrs. Shrividya', 40, 30000)


# prints a blank line
print()

members = [t, s]
for member in members:
    member.tell()


# Output
# (Initialized SchoolMember: Swaroop)
# (Initialized Student: Swaroop)
# (Initialized SchoolMember: Mrs. Shrividya)
# (Initialized Teacher: Mrs. Shrividya)
#
# Name:"Mrs. Shrividya" Age:"40" Salary: "30000"
# Name:"Swaroop" Age:"25" Marks: "75"


# alur program
# 1. Class Student() dipanggil
# 2. Class SchoolMember dipanggil dari Class Student() 
#    dengan nilai parameter dikirim dari Student(SchoolMember)
# 3. SchoolMember memanggil method __init__ 
#    (init disini sebagai objek yang menampung method)
#    memberikan output "Initialized SchoolMember . . ."
# 4. Class Student melanjutkan prosesnya dengan memanggil method pada __init__
# 5. Objek __init__ berisikan method untuk memanggil Class SchoolMember untuk menyimpan nilai Mark
#    dan memberikan Output "Initialized Student . . ."
# 6. Selanjutnya diilakukannya perulangan untuk memanggil masing-masing atribut

