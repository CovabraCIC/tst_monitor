from datetime import datetime


def choice_trigger_type(type_id):
    if type_id == 1:
        return "Único"
    elif type_id == 2:
        return "Diário"
    elif type_id == 3:
        return "Semanal"
    elif type_id == 4:
        return "Mensal"
    else:
        return "Indefinido"

def get_trigger_days_interval(days_interval_bits:int):
    if days_interval_bits:
        return days_interval_bits
    return "Não aplica-se."


def get_trigger_days_of_week(days_of_week_bits:int):
    if days_of_week_bits:
        week_days = {
            1: "Domingo", 2: "Segunda", 4: "Terça", 8: "Quarta",
            16: "Quinta", 32: "Sexta", 64: "Sábado"
        }

        dias = [name for mask, name in week_days.items() if days_of_week_bits & mask]
        dias_str = ", ".join(dias)
        return dias_str
    return "Não aplica-se."

def get_trigger_days_of_month(days_of_month_bits:int):
    if days_of_month_bits:
        dias_do_mes = {i: i for i in range(1, 32)}
        dias = [dia for dia, bit in dias_do_mes.items() if days_of_month_bits & (1 << (dia - 1))]
        return dias
    return "Não aplica-se."



def get_trigger_months_of_year(months_of_year_bits:int):
    if months_of_year_bits:
        meses_do_ano = {
        1: "Janeiro", 2: "Fevereiro", 4: "Março", 8: "Abril",
        16: "Maio", 32: "Junho", 64: "Julho", 128: "Agosto",
        256: "Setembro", 512: "Outubro", 1024: "Novembro", 2048: "Dezembro"
    }
        """Retorna uma lista de meses a partir do valor de bits `meses_bits`."""
        meses = [nome for bit, nome in meses_do_ano.items() if months_of_year_bits & bit]
        return meses
    return "Não aplica-se.."

def get_normal_day_of_week(days_of_week_code:int):
    days_week = {
        0: "Segunda", 1: "Terça", 2: "Quarta",
        3: "Quinta", 4: "Sexta", 5: "Sábado", 6: "Domingo", 
    }
    return days_week.get(days_of_week_code)

def get_normal_month_of_year(months_of_year_code:int):
    months_year = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    return months_year.get(months_of_year_code)



hoje = datetime.now()
data_hoje = hoje.date()
hora_hoje = hoje.time()
dia_hoje = hoje.day
dia_da_semana_hoje = get_normal_day_of_week(hoje.weekday())
mes_hoje = hoje.month
mes_do_ano_hoje = get_normal_month_of_year(mes_hoje)
ano_hoje = hoje.year