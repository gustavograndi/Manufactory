import paho.mqtt.client as mqtt
import random
import time

#####################################
#Help: https://www.hivemq.com/mqtt/public-mqtt-broker/
#Broker: broker.hivemq.com
#TCP Port: 1883
#Websocket Port: 8000
#TLS TCP Port: 8883
#TLS Websocket Port: 8884

# Configurações do broker MQTT
broker_address = "broker.hivemq.com"  # Coloque o endereço do seu broker MQTT aqui
port = 1883  # Porta padrão para comunicação MQTT
user = ""  # Usuário do broker (se necessário)
password = ""  # Senha do broker (se necessário)
topic = "teste/topico"

# Cria um cliente MQTT
client = mqtt.Client()

# Define usuário e senha (se necessário)
if user and password:
    client.username_pw_set(user, password)

# Conecta ao broker
client.connect(broker_address, port=port)

# Função para gerar e publicar um número randômico em um tópico MQTT
def publish_random_number():
    random_number = random.randint(10, 40)  # Gera um número randômico entre 1 e 100
    topic = "teste/topico"
    client.publish(topic, random_number)
    print(f"Número randômico enviado: {random_number}")

# Loop principal para gerar e publicar um número randômico a cada segundo
while True:
    publish_random_number()
    time.sleep(random.randint(1, 40) )  # Aguarda 1 segundo antes de gerar o próximo número