def task_1():
    name = str(input("Name: ")).title()
    salary = int(input("Salary as number: "))
    if isinstance(salary, int):
        print(f"{name}, the tax level you will pay with the salary {salary} is {salary * 0.2}")
    else:
        print(f"{name}, you are idiot")


def task_2():
    user_input = str(input("Number: ")).replace(", ", "")

    lists = []

    for number in user_input:
        number = int(number)
        lists.append(number)

    print(sum(lists))


# task_2()

def task_3():
    user_input = int(input("Number: "))
    f1, f2, = 0, 1
    count = 0
    while count < user_input:
        count += 1
        f1, f2 = f2, f1 + f2

    print(f2)


# task_3()

def task_4():
    # Apple, banana, kiwi, orange, mango, apple, lime, berry, lime
    user_input = int(input("""Please chose the task you want to perform:
1.	Enter items
2.	Exit:
"""))
    dicts = {}
    sets = ()
    dauletsuper = 0

    if user_input == 1:
        user_input_str = str(input("Please enter items separated by comma: ")).lower().split(", ")
        lists = user_input_str

        for letters in lists:
            count = lists.count(letters)

            if count > 1:
                sets += (letters, count)
                lists.remove(letters)
            else:
                dauletsuper += 1
                dicts[dauletsuper] = letters
        print(sets)
        print(dicts)
    else:
        return None

# task_4()

def task_5():
    print("""1. Add Task
2. View All Tasks
3. Mark Task as Completed
4. View All Completed Tasks
5. Exit
""")
    lists = []
    completed = []

    user_input = int(input("What do u want: "))

    if user_input == 1:
        name = input("Name: ")
        lists.append(name)
        print("Your task added!")

    elif user_input == 2:
        if len(lists) == 0:
            print("Your to do list is empty!")
        else:
            for i in enumerate(lists, 1):
                print(i)

    elif user_input == 3:
        number_task = input("Number: ")
        name_task = input("Enter the name of the task: ")
        completed.append([name_task, number_task])

        if name_task in lists:
            lists.remove(name_task)

    elif user_input == 4:
        print(completed)

    else:
        return None

# task_5()