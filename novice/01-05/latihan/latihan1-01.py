import pickle

class Animal:
    def __init__(self, number_of_papaws, color):
        self.number_of_papaws = number_of_papaws
        self.color = color
        
class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)

mary = Sheep("white")

print (str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_papaws))
my_pickled_mary = pickle.dumps(mary)

#binary_file = open('my_pickled_mary.bin',mode='wb')
#my_pickled_mary = pickle.dump(mary, binary_file)
#binary_file.close()

print ("Would you like to see her pickled? Here she is!")
print (my_pickled_mary)


# Output
#
# My sheep mary is white and has 4 paws
# Would you like to see her pickled? Here she is!
# None
# 
# Output without binary_file.close()
# My sheep mary is white and has 4 paws
# Would you like to see her pickled? Here she is!
# b'\x80\x03c__main__\nSheep\nq\x00)\x81q\x01}q\x02(X\x10\x00\x00\x00number_of_papawsq\x03K\x04X\x05\x00\x00\x00colorq\x04X\x05\x00\x00\x00whiteq\x05ub.'
