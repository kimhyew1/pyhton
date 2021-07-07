ELEMENTS= 5

values = []
for i in range(ELEMENTS):
    values.append(float(input("Enter a value : ")))


#total에 값 누적
total = 0
for i in range(ELEMENTS):
    total = total + values[i]

average = total / ELEMENTS

if average < 10 :
    print("Average value is less than 10")