from utils import *
from components.task_results import results

from sqlalchemy import Column, String, Date, Time, DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Monitoramento(Base):
    __tablename__ = 'monitoramento_pywin'
    __table_args__ = {'schema': "monitoramento"}

    # Dados da Tarefa
    nome = Column(String, primary_key=True)
    ultimo_resultado = Column(String)   
    hora_ultima_execucao = Column(Time)
    hora_proxima_execucao = Column(Time)
    data_ultima_execucao = Column(Date)
    data_proxima_execucao = Column(Date)
    status = Column(String)
    pasta = Column(String)
    caminho = Column(String)
    autor = Column(String)
    tipo_erros = Column(String, default=None)
    # Dados da Trigger
    trigger_tipo = Column(String, default=None, primary_key=True)
    trigger_hora = Column(Time, default=None)
    trigger_intervalo_dias = Column(String, default=None)
    trigger_dias_da_semana = Column(String, default=None)
    trigger_dias_do_mes = Column(String, default=None)
    trigger_meses_do_ano = Column(String, default=None)
    
    data_hora_combinacao = Column(DateTime, primary_key=True)

    def __init__(self, task, trigger, folder):
        # Dados da Tarefa
        self.nome = task.Name
        # self.ultimo_resultado = results.get(str(task.LastTaskResult), f"Situação desconhecida, [CODE]: {str(task.LastTaskResult)}"),
        self.ultimo_resultado = "Aguardando"
        self.hora_proxima_execucao = datetime.fromisoformat(str(task.NextRunTime)).time()
        self.hora_ultima_execucao = datetime.fromisoformat(str(task.LastRunTime)).time()
        self.data_proxima_execucao = datetime.fromisoformat(str(task.NextRunTime)).date()
        self.data_ultima_execucao = datetime.fromisoformat(str(task.LastRunTime)).date()
        self.status = "Ativa" if task.Enabled else "Inativa"
        self.pasta = folder.name
        self.caminho = folder.Path
        self.autor = task.Definition.RegistrationInfo.Author
        
        # Dados da Trigger
        if trigger.Type in (1, 2, 3, 4):
            self.trigger_tipo = choice_trigger_type(trigger.Type)
            self.trigger_hora = datetime.fromisoformat(trigger.StartBoundary).time() # Data é descartável para esse campo
            self.trigger_intervalo_dias = get_trigger_days_interval(getattr(trigger, "DaysInterval", None))
            self.trigger_dias_da_semana = get_trigger_days_of_week(getattr(trigger, "DaysOfWeek", None))
            self.trigger_dias_do_mes = get_trigger_days_of_month(getattr(trigger, "DaysOfMonth", None))
            self.trigger_meses_do_ano = get_trigger_months_of_year(getattr(trigger, "MonthsOfYear", None))

    def set_data_hora_combinacao(self):
        """Motor de Combinação Tarefa + Trigger (inerente e exclusivo p/ execução com menor data, as demais não são previsíveis)"""
        self.data_hora_combinacao = datetime.combine(self.data_proxima_execucao, self.trigger_hora)

    def __str__(self):
        return f"{self.nome}"
    
    def __repr__(self):
        return f"<Agendamento(nome={self.nome}, combinacao_horario={self.data_horario_combinacao})>"
    
    def save(self, session):
        session.add(self)
        session.commit()


    @classmethod
    def verify_existing(cls, **primary_keys:dict) -> bool:
        """Retorna True se a consulta existir."""
        existing_item = db.session.query(cls).filter_by(**primary_keys).first()
        return True if existing_item else False

# Criação da tabela no banco de dados (python -m components.models)
Base.metadata.create_all(engine)
