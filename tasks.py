tasks = input(print("Enter your tasks for today seprareted by comma:")).split(", ")
list2 =[]
list=[]
for task in tasks:
    print(task)
    do_it = input(print(f"Dis you finish {task} already?(Y/N)"))
    if do_it.lower() == "y":
        print("nice job")
        list.append(task)
    else:
        print("Try to end the task") 
        list2.append(task)

progress = input(print("Do you want to see your today´s progress?(Y/N)"))
if progress.lower() == "y":
    print(f"""
     *******DONE TASKS******
          {list}
     *******ONGOING TASKS***
        {list2}
""")        
