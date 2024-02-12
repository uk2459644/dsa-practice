
# Test cases
for _ in range(int(input())):
    # current status of tasks remaining to the employe
    task_li=list(map(int,input().split()))

    # number of employee to the task to be distributed
    employess=len(task_li)

    # sort task array in ascending order employe with the task remaining
    # least will be first, and most remaining task will be last and so on..
    task_li.sort()
    # number of new tasks to assign
    new_tasks=int(input())

    # total tasks
    total_tasks=new_tasks + sum(task_li)
    # total tasks per employee
    task=total_tasks//employess

    # extra task in case of float division
    extra_task=total_tasks-(task*employess)

    # to get number of task to assign to per employee
    # substract task from their remining taks
    assigned_task=list()
    for prevtask_per_employee in task_li:

        # you can assign extra task to employee with lower tasks remaining
        if extra_task>0:
            assigned_task.append(1+task-prevtask_per_employee)
            extra_task-=1
        else:
            assigned_task.append(task-prevtask_per_employee)
    
    # Print total task per employee
    print(task)

    # Print how many new task assign to an  employee
    print(*assigned_task)

        




