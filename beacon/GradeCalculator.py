name=input("Enter Student name: ")
marks=list(map(int,input("Enter marks seperated by space:").split()))
print(f"student:",name)
print("Marks:",marks)
avg=sum(marks)/len(marks)
print("average:",avg)
if 100<avg<80:
    print("Grade:A")
elif 80<avg<70:
    print("Grade:B")
elif 70 <avg<50:
    print("grade:c")