def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
with open('C:\\Users\\LENOVO\\OneDrive\\Desktop\\New folder\\second year\\q2\\about.txt', 'r') as f:
    myNames = [line.strip() for line in f]

s1 = myNames[0]
s2=s1.split()
lst = []
for txt in s2:
    if len(txt)>=6:
        print(txt)

print("most frequent word",most_frequent(lst));
