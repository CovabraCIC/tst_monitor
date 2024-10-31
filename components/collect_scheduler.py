import win32com.client
from components.models import Monitoramento

# Scheduler
scheduler = win32com.client.Dispatch("Schedule.Service")
scheduler.Connect()
root_folder = scheduler.GetFolder("\\")
ignored_folders = ["Microsoft"]

def get_tasks_from_folder(folder):
    tasks = folder.GetTasks(0)
    task_list = []
    for task in tasks:
        if folder.Name != "\\":
            for trigger in task.Definition.Triggers:
                agendamento = Monitoramento(task=task, trigger=trigger, folder=folder)
                task_list.append(agendamento)
    return task_list

def get_tasks_in_subfolders(folder):
    tasks_in_subfolders = []
    if folder.Name not in ignored_folders:
        tasks_in_subfolders.extend(get_tasks_from_folder(folder))
    subfolders = folder.GetFolders(0)
    for subfolder in subfolders:
        if subfolder.Name not in ignored_folders:
            tasks_in_subfolders.extend(get_tasks_in_subfolders(subfolder))
    return tasks_in_subfolders

tasks_in_scheduler = get_tasks_in_subfolders(root_folder)
