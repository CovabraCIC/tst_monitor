from components.collect_scheduler import tasks_in_scheduler
from datetime import timedelta
from components.models import Monitoramento

# MONITORAMENTO
for task in tasks_in_scheduler:

    print(task.data_proxima_execucao)
#     t_name = task.get("nome")
#     t_status = task.get("status")
#     t_last_result = task.get("ultimo_resultado")
#     t_last_rundate = datetime.strptime(task.get("data_ultima_execucao"), '%Y-%m-%d').date()
#     t_last_runtime = datetime.strptime(task.get("hora_ultima_execucao"), '%H:%M:%S').time()

#     t_last_run_datetime = datetime.combine(t_last_rundate, t_last_runtime)

#     historys = session.query(Monitoramento).filter_by(nome=t_name, data_proxima_execucao = t_last_rundate).all()

#     if len(historys) > 1:
#         print(f"Duplicata detectada para a tarefa: {t_name} com {len(historys)} entradas no histórico.")

#     for history in historys: # Para cada tarefa no histórico
#         # print(history.status)
#         h_next_runtime = datetime.combine(history.data_proxima_execucao, history.hora_proxima_execucao) # Transforme a Hora de Próxima Execução em DateTime

#         # Defina uma margem de erro de 2 minutos para a Hora de Próxima Execução
#         h_limit_upper = (h_next_runtime + timedelta(minutes=2))
#         h_limit_lower = (h_next_runtime - timedelta(minutes=2))

#         # Verifica se a Hora de Última Execução está dentro da margem de erro 
#         if (h_limit_lower <= t_last_run_datetime <= h_limit_upper) and history.ultimo_resultado in ["Aguardando", "Em execução"]:

#             # history.data_ultima_execucao = t_last_rundate
#             # history.hora_ultima_execucao = t_last_runtime
#             history.ultimo_resultado = task.get("ultimo_resultado")

#             session.commit()
# session.close()
