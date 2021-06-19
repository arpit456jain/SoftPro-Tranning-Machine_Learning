print("Enter 10 mumbers in one line with space betwenn them")
lst = [int(x) for x in input().split()]

sum1 = sum(lst)
avg = sum1//10

print("Sum is ",sum1,"and average is ",avg)
