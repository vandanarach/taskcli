import argparse
import json 
from datetime import datetime
import os.path
from tabulate import tabulate



parser = argparse.ArgumentParser(
    prog="taskly_todo", 
    usage="whoa, use: %(prog)s [options]",
    description="Creates a todo list of tasks",
    epilog="You can add update and delete tasks")

# Task actions
parser.add_argument("-a", "--add", action="store_true", help="Add a task")
parser.add_argument("-r", "--remove", action="store_true", help="Remove a task")
parser.add_argument("-u", "--update", action="store_true", help="Update a task")
parser.add_argument("-l", "--list", action="store_true", help="List all tasks")

# Task details
parser.add_argument("-d", "--description", type=str, help="Task description")
parser.add_argument("-i", "--id", type=int, help="Task ID")
parser.add_argument("-s", "--status", type=str, help="Task status - todo, done, in-progress")
parser.add_argument("-t", "--time", type=str, help="Task date - 2026-10-11T16:01:11", default="")



args = parser.parse_args()


file = "data.json"
def add_task():
    id_new = 1
    try:
        with open(file, "x+") as f:
            data = {}
    except Exception as d:
        with open(file, "r") as f:
            data = json.load(f)
    f.close()
    if data != {}:
        sorted_keys = sorted(data.keys())
        id_new = int(sorted_keys[-1]) + 1

    if args.description is not None:
        description = args.description
    else:
        print("Mandatory command line arg is missing - description")
    data_dict = {}
    date = datetime.today().isoformat(timespec="seconds")
    data_dict = {str(id_new): {
        "description": description,
        "status": "todo",
        "created_at": date,
        "updated_at": date
    }}
    data.update(data_dict)
    with open(file, "w") as f:
        json.dump(data, f, indent=4)  # indent for readability
    f.close()
    
    table = [[task_id, task["description"], task["status"], task["created_at"], task["updated_at"]] for task_id, task in data_dict.items()]
    print(tabulate(table, headers=["Task ID", "Description", "Status", "Created Date", "Updated Date"], tablefmt="grid"))

def del_task(id):
    data_dict = {}
    with open(file, "r") as f:
        data_dict = json.load(f)
    del data_dict[str(id)]
    with open(file, "w") as f:
        json.dump(data_dict, f, indent=4)  # indent for readability
    table = [[task_id, task["description"], task["status"], task["created_at"], task["updated_at"]] for task_id, task in data_dict.items()]
    print(tabulate(table, headers=["Task ID", "Description", "Status", "Created Date", "Updated Date"], tablefmt="grid"))

def list_tasks():
    with open(file, "r") as f:
        data = json.load(f)
    table = [[task_id, task["description"], task["status"], task["created_at"], task["updated_at"]] for task_id, task in data.items()]
    print(tabulate(table, headers=["Task ID", "Description", "Status", "Created Date", "Updated Date"], tablefmt="grid"))


def list_tasks_timebased():
    with open(file, "r") as f:
        data = json.load(f)
    table = [
    [task_id, task["description"], task["status"], task["created_at"], task["updated_at"]]
    for task_id, task in data.items()
    if task["created_at"] > args.time
    ]
    print(tabulate(table, headers=["Task ID", "Description", "Status", "Created Date", "Updated Date"], tablefmt="grid"))

def list_tasks_statuswise():
    with open(file, "r") as f:
        data = json.load(f)
    table = [[task_id, task["description"], task["status"], task["created_at"], task["updated_at"]]
        for task_id, task in data.items()
            if task["status"] == args.status]
    print(tabulate(table, headers=["Task ID", "Description", "Status", "Created Date", "Updated Date"], tablefmt="grid"))

def update_task():
    with open(file, "r") as f:
        data = json.load(f)
    if args.id is not None:
        for task_id, task in data.items():
            if int(task_id) == int(args.id):
                if args.description is not None:
                    data[task_id]["description"] = args.description
                if args.status is not None:
                    data[task_id]["status"] = args.status
                data[task_id]["updated_at"] = datetime.today().isoformat(timespec="seconds")
    with open(file, "w") as f:
        json.dump(data, f, indent=4)  # indent for readability
    f.close()
    table = [[task_id, task["description"], task["status"], task["created_at"], task["updated_at"]] for task_id, task in data.items()]
    print(tabulate(table, headers=["Task ID", "Description", "Status", "Created Date", "Updated Date"], tablefmt="grid"))

def main():
    if args.add:
        if(args.description is not None):
            add_task()
        else:
            print("Task Description is missing")
    else:
        pass

    if args.remove:
        if (args.description is not None):
            if(args.id is not None):
                del_task(str(args.id))
            else:
                print("Mandatory command line arg missing - id")
        else:
            print("Mandatory command line arg missing - description")
    else:
        pass

    if args.list:
        list_tasks()
    else:
        pass

    if args.time:
        list_tasks_timebased()
    else:
        pass

    if args.update and args.id and (args.status or args.description):
        update_task()
    else:
        pass

    if args.status and not args.update:
        list_tasks_statuswise()
    else:
        pass



if __name__ == "__main__":
    main()

