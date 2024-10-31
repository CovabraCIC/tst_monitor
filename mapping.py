from components.collect_scheduler import tasks_in_scheduler
from datetime import timedelta
from utils import *

@logger_time()
def main():
    for task in tasks_in_scheduler:

        try:
            if task.trigger_tipo == 'Único' and task.hora_proxima_execucao >= hora_hoje:
                if task.data_proxima_execucao == data_hoje :
                    task.set_data_hora_combinacao()
                    if not task.verify_existing(nome=task.nome, trigger_tipo=task.trigger_tipo, data_hora_combinacao=task.data_hora_combinacao):
                        task.save(session)
                        logger.info(f'Execução {task.nome} no modelo "{task.trigger_tipo}" adicionada para monitoramento, prevista para {task.data_hora_combinacao}.')
                    else:
                        logger.info(f'Execução {task.nome} no modelo "{task.trigger_tipo}" prevista para {task.data_hora_combinacao} já existe.')

            if task.trigger_tipo == 'Diário':
                if task.data_ultima_execucao + timedelta(days=task.trigger_intervalo_dias) == data_hoje and task.hora_proxima_execucao >= hora_hoje:
                    task.set_data_hora_combinacao()
                    if not task.verify_existing(nome=task.nome, trigger_tipo=task.trigger_tipo, data_hora_combinacao=task.data_hora_combinacao):
                        task.save(session)
                        logger.info(f'Execução {task.nome} no modelo "{task.trigger_tipo}" adicionada para monitoramento, prevista para {task.data_hora_combinacao}.')
                    else:
                        logger.info(f'Execução {task.nome} no modelo "{task.trigger_tipo}" prevista para {task.data_hora_combinacao} já existe.')

            if task.trigger_tipo == 'Semanal':
                if dia_da_semana_hoje in task.trigger_dias_da_semana and task.hora_proxima_execucao >= hora_hoje:
                    task.set_data_hora_combinacao()
                    if not task.verify_existing(nome=task.nome, trigger_tipo=task.trigger_tipo, data_hora_combinacao=task.data_hora_combinacao):
                        task.save(session)
                        logger.info(f'Execução {task.nome} no modelo "{task.trigger_tipo}" adicionada para monitoramento, prevista para {task.data_hora_combinacao}.')
                    else:
                        logger.info(f'Execução {task.nome} no modelo "{task.trigger_tipo}" prevista para {task.data_hora_combinacao} já existe.')

            if task.trigger_tipo == 'Mensal':
                if dia_hoje in task.trigger_dias_do_mes and mes_do_ano_hoje in task.trigger_meses_do_ano and task.hora_proxima_execucao >= hora_hoje:
                    task.set_data_hora_combinacao()
                    if not task.verify_existing(nome=task.nome, trigger_tipo=task.trigger_tipo, data_hora_combinacao=task.data_hora_combinacao):
                        task.save(session)
                        logger.info(f'Execução {task.nome} no modelo "{task.trigger_tipo}" adicionada para monitoramento, prevista para {task.data_hora_combinacao}.')
                    else:
                        logger.info(f'Execução {task.nome} no modelo "{task.trigger_tipo}" prevista para {task.data_hora_combinacao} já existe.')

        except Exception:
            logger.exception('Erro ao salvar o mapeamento.')

    session.close()

if __name__ == "__main__":
    main()