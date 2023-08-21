
Task_list=[]
def schedule_Tasks(Task,priority=False):
    if priority==True:
        Task_list.insert(0,Task)
    else:
        Task_list.append(Task)
    print(f'Task List : {Task_list}')

T1=schedule_Tasks('Going to Office',True)
T2=schedule_Tasks('Going to Friend\'s house')
T3=schedule_Tasks('Project Call',True)
T4=schedule_Tasks('Office Lunch')
T5=schedule_Tasks('Office Work',True)
T6=schedule_Tasks('Going to Gym')

