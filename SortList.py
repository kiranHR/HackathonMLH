def sort(lst): 
    lst = [str(i) for i in lst] 
    lst.sort() 
    lst = [int(i) if i.isdigit() else i for i in lst ] 
    return lst 
              
# Driver code
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = input("Please enter the Value of %d Element : " %i)
    NumList.append(value)
#lst = ['k', 5, 'e', 3, 'g', 7, 0, 't'] 
print(sort(NumList)) 
