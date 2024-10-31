import win32com.client
from components.models import Monitoramento
from typing import List


def get_all_tasks(mapping:bool=False) -> List[Monitoramento]:
    # Scheduler
    scheduler = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()
    root_folder = scheduler.GetFolder("\\")
    ignored_folders = ["Microsoft"]
    tasks_in_scheduler = []

    def retrieve_tasks(folder):
        # Obtém tarefas da pasta atual
        tasks = folder.GetTasks(0)
        for task in tasks:
            if folder.Name != "\\":
                for trigger in task.Definition.Triggers:
                    agendamento = Monitoramento(task=task, trigger=trigger, folder=folder, mapping=mapping)
                    tasks_in_scheduler.append(agendamento)

        # Recursivamente obtém tarefas em subpastas
        subfolders = folder.GetFolders(0)
        for subfolder in subfolders:
            if subfolder.Name not in ignored_folders:
                retrieve_tasks(subfolder)

    # Inicia a busca a partir da pasta raiz
    retrieve_tasks(root_folder)
    return tasks_in_scheduler