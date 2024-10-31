from loguru import logger


EXECUTION_ID = 555
VAR_LETTER = 'A'

logger.remove()

logger.add(f'files/logs/{EXECUTION_ID}{VAR_LETTER}.log',
        format='{time:YYYY-MM-DD HH:mm:ss} - {level}: {message}',
        rotation='50 MB', 
        retention='14 days', 
        compression='gz',
        level='INFO')

logger = logger.bind(execution_id=EXECUTION_ID, var_letter=VAR_LETTER)