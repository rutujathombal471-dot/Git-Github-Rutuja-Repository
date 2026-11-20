name = input("Enter your name:")


m1 = int(input("Enter  Python marks:"))
m2 = int(input("Enter  SQL marks:"))
m3 = int(input("Enter  Excel marks:"))

total = m1 + m2 + m3
percentage = total / 3 * 100


print("Welcome to Grade System.")

if percentage >= 90 and percentage <= 100:
    print("Grade A+")
elif percentage >= 80 and percentage < 90:
    print("Grade A")
elif percentage >= 70 and percentage < 80:
    print("Grade B+")
elif percentage >= 60 and percentage < 70:
    print("Grade B")
else:
    print("Grade F")

print(f"Student Name {name} \n Total Marks: {total} \n Percentage: {percentage}")
