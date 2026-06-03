import numpy as np

no = int(input("Enter no of elements:-"))
ele = []
for i in range(no):
    element = int(input("Enter Element:-"))
    ele.append(element)
print(ele)
a = np.array(ele)
no_b = int(input("Enter no of elements:-"))
ele_b = []
for i in range(no_b):
    element_b = int(input("Enter Element:-"))
    ele_b.append(element_b)
print(ele_b)
b = np.array(ele_b)

choice = int(input("Enter Choice 1 (for printing array)\n2 (for mathematical operation)\n3 (for aggraetation operation)\n4 (converting multidimensional to one dimension)\n5 (broadcasting)\n6 (Exit):-"))

if choice==1:
    print("\nARRAY A\n")
    print(a)
    print("\nArray B\n")
    print(b)

elif choice==2:
    print("\nMathematcial Operation of A")
    print("Addition = ",a+b,"\n","Sub = ",a-b,"\n","Multiplication",a*b,"\n","Div",a/b)
elif choice==3:
    print("\nAggreatation Operations of A")
    print("\n",np.sum(a),"\n",np.mean(a),"\n",np.median(a),"\n",np.sqrt(64))
    print("\nAggreatation Operations of B")
    print("\n",np.sum(b),"\n",np.mean(b),"\n",np.median(b),"\n",np.sqrt(100))
elif choice==4:
   rows = int(input("Enter Rows:-"))
   cols = int(input("Enter Columns:-"))
   mat = []
   for i in range(rows):
        temp = []
        for j in range(cols):
            ele = int(input("Enter Elements:-"))
            temp.append(ele)
        mat.append(temp)
   print(mat)
   c = np.array(mat)
   print(c)
   #print(matrix(rows,cols))
   print("\n1D Array using flatten\n")
   print(c.flatten())
   print("\nArray B using ravel\n")
   print(c.ravel())
elif choice==5:
   rows = int(input("Enter Rows:-"))
   cols = int(input("Enter Columns:-"))
   mat = []
   for i in range(rows):
        temp = []
        for j in range(cols):
            ele = int(input("Enter Elements:-"))
            temp.append(ele)
        mat.append(temp)
   d = np.array(mat)
   print("Broadcasting")
   print(d+10)
elif choice==6:
    exit()
else:
    print("Invalid Chocie Please Try Again")