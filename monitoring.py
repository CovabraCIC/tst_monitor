from components.collect_scheduler import get_all_tasks
from datetime import timedelta
from components.models import Monitoramento
from utils import *

from sqlalchemy import func, not_


tasks_in_table = session.query(Monitoramento).filter(
    (func.date(Monitoramento.data_hora_combinacao) == data_hoje) &
    (not_(Monitoramento.trigger_tipo.startswith('OLD')))
).all()


tasks_in_scheduler = get_all_tasks()

for task in tasks_in_scheduler:

    # Defina uma margem de erro de 2 minutos para a Hora de Última Execução.
    h_limit_upper = (datetime.combine(task.data_ultima_execucao, task.hora_ultima_execucao) + timedelta(minutes=2))
    h_limit_lower = (datetime.combine(task.data_ultima_execucao, task.hora_ultima_execucao) - timedelta(minutes=2))

    # Selecionando no Monitoramento a tarefa mapeada que corresponde à iteração.
    task_target = session.query(Monitoramento).filter(
        (Monitoramento.nome == task.nome) &
        (Monitoramento.trigger_tipo == task.trigger_tipo) &
        (Monitoramento.data_hora_combinacao >= h_limit_lower) & 
        (Monitoramento.data_hora_combinacao <= h_limit_upper)
    ).first()

    if task_target:
        # Atualizar o resultado da tarefa alvo (já armazenada no banco de dados).
        task_target.ultimo_resultado = task.ultimo_resultado
        task_target.edit(session)
    else:
        logger.info(f"A task {task.nome} no modelo {task.trigger_tipo} não obteve correspondência.")