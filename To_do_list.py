tasks=[]
while True:
    print("\n1.show tasks\n2.add task\n3.delete task\n4.exit")
    choice = input("Choose (1-4): ")
    if choice == '1':
        print("tasks"if tasks else "No tasks found")
        for i,t in enumerate(tasks,1):
            print(f'{i}.{t}')
    elif choice=='2':
        task = input("New task: ").strip()
        task.append(task)
    elif choice=='3':
        for i,t in enumerate(tasks,1):
            print(f'{i}.{t}')
        try:
            indx= int(input("Remove task #: "))
            if 1<=indx<=len(tasks):
                tasks.pop(indx-1)
        except:
            print("Invalid input. Please enter a valid task number.")

    elif choice=='4':
        print("Exting the program.")
        break