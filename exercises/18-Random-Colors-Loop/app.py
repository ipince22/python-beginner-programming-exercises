import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    example_color = 0
    students_array = []
    #your loop here
    for i in range(10):
        students_array.append(get_color(random.randrange(0,5)))

    for x in students_array:
      print(x)


    



print(get_allStudentColors())