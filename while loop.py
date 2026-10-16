total_chores=4
original_count=total_chores
print(f"you have {original_count}chores to finish today!\n")
completed_count = 0
chore_num = 1
while chore_num <= total_chores:
    if chore_num == 1: next_chore = "make your bed"
    elif chore_num == 2: next_chore = "feeed the pet"
    elif chore_num == 3: next_chore = "take out the trash"
    else: next_chore = "wash the dishes"
    answer = input(f"have you finished: {next_chore}? (yes/no):")
    if answer == "yes":
        