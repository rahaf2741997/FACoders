
a = input("Enter student's name : ")

s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

i = [s1, s2, s3]
test = 0
for x in i:
        variable = a in x
        if variable ==1 :
            print(a , sum(x[1 : 6]))
            break
        else :
            test += 1
if test == 3:
            print("Student is not recorded 0")
