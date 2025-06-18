bill, tip_percent, people = input().split()
bill = float(bill)
tip_percent = float(tip_percent)
people = int(people)
total_bill = bill + (bill * tip_percent / 100)
per_person = total_bill / people

print(f"Each person pays: {per_person:.2f}")