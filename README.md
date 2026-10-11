# taskcli

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

# Usage:
## Add an entry:
====================
taskcli>taskly_todo -a -d "tame the lion"

+-----------+---------------+----------+---------------------+---------------------+
|   Task ID | Description   | Status   | Created Date        | Updated Date        |
+===========+===============+==========+=====================+=====================+
|         1 | tame the lion | todo     | 2026-10-11T19:07:16 | 2026-10-11T19:07:16 |
+-----------+---------------+----------+---------------------+---------------------+

## Delete an entry:
======================
taskcli>taskly_todo -r -d "goto the doc" -i 4
+-----------+------------------+----------+---------------------+---------------------+
|   Task ID | Description      | Status   | Created Date        | Updated Date        |
+===========+==================+==========+=====================+=====================+
|         1 | tame the lion    | todo     | 2026-10-11T19:07:16 | 2026-10-11T19:07:16 |
+-----------+------------------+----------+---------------------+---------------------+
|         2 | pat the dog      | todo     | 2026-10-11T19:07:23 | 2026-10-11T19:07:23 |
+-----------+------------------+----------+---------------------+---------------------+
|         3 | visit grandma    | todo     | 2026-10-11T19:07:35 | 2026-10-11T19:07:35 |
+-----------+------------------+----------+---------------------+---------------------+
|         5 | goto the dentist | todo     | 2026-10-11T19:08:04 | 2026-10-11T19:08:04 |
+-----------+------------------+----------+---------------------+---------------------+

## Update an entry:
=======================
taskcli>taskly_todo -u -d "goto the doc" -i 3

+-----------+------------------+----------+---------------------+---------------------+
|   Task ID | Description      | Status   | Created Date        | Updated Date        |
+===========+==================+==========+=====================+=====================+
|         1 | tame the lion    | todo     | 2026-10-11T19:07:16 | 2026-10-11T19:07:16 |
+-----------+------------------+----------+---------------------+---------------------+
|         2 | pat the dog      | todo     | 2026-10-11T19:07:23 | 2026-10-11T19:07:23 |
+-----------+------------------+----------+---------------------+---------------------+
|         3 | goto the doc     | todo     | 2026-10-11T19:07:35 | 2026-10-11T19:12:50 |
+-----------+------------------+----------+---------------------+---------------------+
|         5 | goto the dentist | todo     | 2026-10-11T19:08:04 | 2026-10-11T19:08:04 |
+-----------+------------------+----------+---------------------+---------------------+

taskcli>taskly_todo -u -s "in-progress" -i 3

+-----------+------------------+-------------+---------------------+---------------------+
|   Task ID | Description      | Status      | Created Date        | Updated Date        |
+===========+==================+=============+=====================+=====================+
|         1 | tame the lion    | todo        | 2026-10-11T19:07:16 | 2026-10-11T19:07:16 |
+-----------+------------------+-------------+---------------------+---------------------+
|         2 | pat the dog      | todo        | 2026-10-11T19:07:23 | 2026-10-11T19:07:23 |
+-----------+------------------+-------------+---------------------+---------------------+
|         3 | goto the doc     | in-progress | 2026-10-11T19:07:35 | 2026-10-11T19:13:07 |
+-----------+------------------+-------------+---------------------+---------------------+
|         5 | goto the dentist | todo        | 2026-10-11T19:08:04 | 2026-10-11T19:08:04 |
+-----------+------------------+-------------+---------------------+---------------------+


## List all tasks:
============================
taskcli>taskly_todo -l
+-----------+------------------+-------------+---------------------+---------------------+
|   Task ID | Description      | Status      | Created Date        | Updated Date        |
+===========+==================+=============+=====================+=====================+
|         1 | tame the lion    | todo        | 2026-10-11T19:07:16 | 2026-10-11T19:07:16 |
+-----------+------------------+-------------+---------------------+---------------------+
|         2 | pat the dog      | todo        | 2026-10-11T19:07:23 | 2026-10-11T19:07:23 |
+-----------+------------------+-------------+---------------------+---------------------+
|         3 | goto the doc     | in-progress | 2026-10-11T19:07:35 | 2026-10-11T19:13:07 |
+-----------+------------------+-------------+---------------------+---------------------+
|         5 | goto the dentist | todo        | 2026-10-11T19:08:04 | 2026-10-11T19:08:04 |
+-----------+------------------+-------------+---------------------+---------------------+

## List tasks after a particular date and time:
===================================================
taskcli>taskly_todo -t 2026-10-11T19:07:23
+-----------+------------------+-------------+---------------------+---------------------+
|   Task ID | Description      | Status      | Created Date        | Updated Date        |
+===========+==================+=============+=====================+=====================+
|         3 | goto the doc     | in-progress | 2026-10-11T19:07:35 | 2026-10-11T19:13:07 |
+-----------+------------------+-------------+---------------------+---------------------+
|         5 | goto the dentist | todo        | 2026-10-11T19:08:04 | 2026-10-11T19:08:04 |
+-----------+------------------+-------------+---------------------+---------------------+

## List tasks status wise:
===============================
taskcli>taskly_todo -s in-progress
+-----------+---------------+-------------+---------------------+---------------------+
|   Task ID | Description   | Status      | Created Date        | Updated Date        |
+===========+===============+=============+=====================+=====================+
|         3 | goto the doc  | in-progress | 2026-10-11T19:07:35 | 2026-10-11T19:13:07 |
+-----------+---------------+-------------+---------------------+---------------------+

taskcli>taskly_todo -s todo
+-----------+------------------+----------+---------------------+---------------------+
|   Task ID | Description      | Status   | Created Date        | Updated Date        |
+===========+==================+==========+=====================+=====================+
|         1 | tame the lion    | todo     | 2026-10-11T19:07:16 | 2026-10-11T19:07:16 |
+-----------+------------------+----------+---------------------+---------------------+
|         2 | pat the dog      | todo     | 2026-10-11T19:07:23 | 2026-10-11T19:07:23 |
+-----------+------------------+----------+---------------------+---------------------+
|         5 | goto the dentist | todo     | 2026-10-11T19:08:04 | 2026-10-11T19:08:04 |
+-----------+------------------+----------+---------------------+---------------------+

**Requirements:**
===================
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

* Add, Update, and Delete tasks
* Mark a task as in progress or done
* List all tasks
* List all tasks that are done
* List all tasks that are not done
* List all tasks that are in progress



**Here are some constraints to guide the implementation:**
==========================================================
* You can use any programming language to build this project.
* Use positional arguments in command line to accept user inputs.
* Use a JSON file to store the tasks in the current directory.
* The JSON file should be created if it does not exist.
* Use the native file system module of your programming language to interact with the JSON file.
* Do not use any external libraries or frameworks to build this project.
* Ensure to handle errors and edge cases gracefully.


**Task Properties:**
=========================
Each task should have the following properties:

* id: A unique identifier for the task

* description: A short description of the task

* status: The status of the task (todo, in-progress, done)

* createdAt: The date and time when the task was created

* updatedAt: The date and time when the task was last updated

Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.

