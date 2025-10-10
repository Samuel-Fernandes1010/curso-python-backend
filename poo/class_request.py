import datetime
from abc import ABC, abstractmethod
import requests


class IVerificador(ABC):
    @abstractmethod
    def verificar(self) -> bool:
        pass


class IAlerta(ABC):
    @abstractmethod
    def enviar_alerta(self, mensagem: str):
        pass


class VerificadorAPI(IVerificador):
    def __init__(self, url: str):
        self.__url = url
        
    def verificar(self) -> bool:
        try:
            response = requests.get(self.__url,timeout=5)
            if response.status_code == 200:
                print("--> Status: OK (200)")
                return True
            else:
                print('--> Status: ERRO')
        except requests.exceptions.RequestException as e:
            print(f'--> ERRO DE CONEXÃO: {e}')
            return False





class AlertaSlack(IAlerta):
    def __init__(self, webhook_url: str):
        self.__webhook_url = webhook_url
        
    def enviar_alerta(self, mensagem: str):
        
        payload = {"text:": f'ALERTA URGENTE \n{mensagem}'}
        
        try:
            print("(ALERTA) Enviando para o slack...")
            requests.post(self.__webhook_url, json=payload, timeout=5).raise_for_status()
            print('Alerta enviado com sucesso!')
        
        except requests.exceptions.RequestException as e:
            print(f'--> ERRO ao enviar o alerta de slack: {e}')
        
        
class AlertaEmail(IAlerta):
    def __init__(self, destinatario: str):
        self._destinatario = destinatario
    
    def enviar_alerta(self, mensagem: str):
        print(f'(ALERTA) Gerando e-mail {self._destinatario}')


class Monitor:
    def __init__(self, verificador: IVerificador, alerta: IAlerta):
        self._verificador = verificador
        self._alerta = alerta
    
    def rodar_ciclo(self):
        
        print('Iniciando novo ciclo...')
        if not self._verificador.verificar():
            self._alerta.enviar_alerta('O serviço está offline ou retornando erro.')
        else:
            print('Serviço funcionando normalmente.')
            
            
url_webhook = 'https://webhook.site/b62902c7-b14b-4efd-baf2-cebd28a3f790'
url_real = 'https://moodle.softexpe.org.br/login/index.php'
url_fake = 'https://www.fakke.br/'


alerta_para_slack = AlertaSlack(url_webhook)
alerta_para_email = AlertaEmail('zumzum@gmail.com')

verificador_ok = VerificadorAPI(url=url_real)
verificador_not_ok = VerificadorAPI(url=url_fake)

#1 cenário: Ok

monitor_principal = Monitor(verificador_ok, alerta_para_slack)
monitor_principal.rodar_ciclo()

#2 cenário: Not Ok

monitor_secundario = Monitor(verificador_not_ok, alerta_para_slack)
monitor_secundario.rodar_ciclo()