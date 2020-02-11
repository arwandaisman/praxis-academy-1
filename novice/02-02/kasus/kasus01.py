class Bootcamp:
    task = 0
    assesment = 0
    def __init__(self, nama, status):
        self.nama = nama
        self.status = status

    def createTask(self):
        print("Mencari assesment. . .")
        if Bootcamp.assesment == 0:
            print("Belum ada assesment!")
        else:
            print("{} sedang membut tugas.".format(self.nama))
            Bootcamp.assesment -=1
            Bootcamp.task +=1
            print("Sisa assesment {:d}".format(Bootcamp.assesment))

    def say_hi_student(self):
        print("Halo, saya {}, dan saya adalah {}".format(self.nama, self.status))

    def say_hi_mentor(self):
        print("Halo, saya {}, dan saya adalah {}".format(self.nama, self.status))

    def createAssesment(self):
        print("Assesment dibuat!")
        Bootcamp.assesment +=1

    @classmethod
    def how_many_assesment(cls):
        print("Ada {:d} assesment yang belum selesai".format(cls.assesment))
    
    @classmethod
    def how_many_task(cls):
        print("Ada {:d} assesment yang sudah selesai".format(cls.task))

print("Selamat Datang di Bootcamp")
siswa = Bootcamp("Kadek", "Siswa")

print("\nintroduction . . .")
siswa.say_hi_student()
siswa.createTask()

print("\nBreak. . .")

print("\nintroduction . . .")
mentor = Bootcamp("Cahya", "Mentor")
mentor.say_hi_mentor()
mentor.createAssesment()
Bootcamp.how_many_assesment()

print("\nBreak. . .\n")

siswa.createTask()
Bootcamp.how_many_task()

print("\nGood bye. . .")
