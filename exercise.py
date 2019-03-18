seats = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]



row_index = 0
seats_index = 0
for row_index, row in enumerate(seats):
    for seats_index, seat in enumerate(row):
        if seat == None:
            print("Row {} seat {} is empty. Sit there? (y/n)".format(row_index + 1, seats_index + 1))
            user_input = input()
            if user_input == 'y':
                print("What is your name?")
                user_name = input()
                seats[row_index][seats_index] = user_name
                break
    seats_index += 1
row_index += 1

print(seats)
