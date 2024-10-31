from dotenv import load_dotenv

load_dotenv()


EXECUTION_ID = 201
VAR_LETTER = 'A'

from .dts import *
from .db import *
from .log import *