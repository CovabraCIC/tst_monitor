from loguru import logger
from functools import wraps
from datetime import datetime as dt
from . import EXECUTION_ID, VAR_LETTER



logger.remove()
logger.add(f'files/logs/{EXECUTION_ID}{VAR_LETTER}.log',
           format='{time:YYYY-MM-DD HH:mm:ss} - {level}: {message}',
           rotation='50 MB', 
           retention='14 days', 
           compression='gz',
           level='INFO',
           enqueue=True)

logger = logger.bind(execution_id=EXECUTION_ID, var_letter=VAR_LETTER)

def logger_time():
    def decorator(func):

        def wrapper(*args, **kwargs):
            if func.__name__ == "main":
                logger.info(f"Execução {EXECUTION_ID}{VAR_LETTER} iniciada.")
                start_time = dt.now()
                result = func(*args, **kwargs)
                end_time = dt.now()
                execution_time = end_time - start_time
                execution_hours, remainder = divmod(execution_time.total_seconds(), 3600)
                execution_minutes, execution_seconds = divmod(remainder, 60)
                logger.info(f"Execução {EXECUTION_ID}{VAR_LETTER} finalizada em {int(execution_hours)}h {int(execution_minutes)}m {execution_seconds:.4f}s.\n\n")
            else:
                logger.info(f'Iniciando a execução da função "{func.__name__}"')
                start_time = dt.now()
                result = func(*args, **kwargs)
                end_time = dt.now()
                execution_time = end_time - start_time
                execution_hours, remainder = divmod(execution_time.total_seconds(), 3600)
                execution_minutes, execution_seconds = divmod(remainder, 60)
                logger.info(f'Função "{func.__name__}" finalizada em {int(execution_hours)}h {int(execution_minutes)}m {execution_seconds:.4f}s.\n\n')
            return result
        return wrapper
    return decorator


class ExecutionSafetyError(Exception):
    """Exceção levantada quando a execução não é considerada segura para prosseguir."""
    pass
