
import paho.mqtt.client as mqtt #import the client1
from datetime import datetime
import csv

# Função para salvar mensagem em um arquivo CSV
def save_to_csv(topic, message, csv_filename):
    with open(csv_filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([datetime.now(), topic, message.decode()]) 

# Callback para quando o cliente recebe uma resposta CONNACK do broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT!")
        
    else:
        print(f"Falha na conexão. Código de retorno = {rc}")

# Callback para quando uma mensagem é publicada ao broker
def on_publish(client, userdata, mid):
    print(f"{datetime.now()} Mensagem publicada com sucesso!")

# Callback para quando uma mensagem é recebida do broker
def on_message(client, userdata, message):
    #define o nome do arquivo a ser salvo quando recebe o tópico
    csv_filename = 'mqtt_messages.csv'
    print(f"{datetime.now()} Mensagem recebida no tópico {message.topic}: {message.payload.decode()}")
    save_to_csv(message.topic, message.payload, csv_filename)

#####################################
#Help: https://www.hivemq.com/mqtt/public-mqtt-broker/
#Broker: broker.hivemq.com
#TCP Port: 1883
#Websocket Port: 8000
#TLS TCP Port: 8883
#TLS Websocket Port: 8884

# Configurações do broker MQTT
broker_address = "test.mosquitto.org"  # Coloque o endereço do seu broker MQTT aqui
port = 1883  # Porta padrão para comunicação MQTT
user = ""  # Usuário do broker (se necessário)
password = ""  # Senha do broker (se necessário)
topic = "/LABUSIG/LAB/test"


client = mqtt.Client() #create new instance

# Define as funções de callback
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

if user and password:
    client.username_pw_set(user, password)

print("connecting to broker")
# Conecta ao broker
client.connect(broker_address, port=port)

print("Subscribing to topic",topic)
# Subscreve ao tópico desejado assim que conecta
client.subscribe(topic)

# mensagem a serem publicados
message = "Conexão Iniciada!"
# Publica a mensagem no tópico especificado
client.publish(topic, message)

# Mantém a conexão MQTT em execução
client.loop_forever()