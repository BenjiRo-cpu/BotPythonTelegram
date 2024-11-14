import os
import telebot
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar el token del bot
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Base de datos de vuelos simulados
vuelos = [
    {"origen": "Ciudad de México", "destino": "Cancún", "fecha": "2024-11-20", "precio": "$1500"},
    {"origen": "Ciudad de México", "destino": "Nueva York", "fecha": "2024-11-21", "precio": "$1600"},
    {"origen": "Ciudad de México", "destino": "Toronto", "fecha": "2024-11-22", "precio": "$1400"},
    {"origen": "Guadalajara", "destino": "Monterrey", "fecha": "2024-11-20", "precio": "$1200"},
    {"origen": "Guadalajara", "destino": "Tijuana", "fecha": "2024-11-23", "precio": "$1700"},
    {"origen": "Cancún", "destino": "Ciudad de México", "fecha": "2024-11-24", "precio": "$1800"},
    {"origen": "Monterrey", "destino": "Guadalajara", "fecha": "2024-11-25", "precio": "$1300"},
    {"origen": "Ciudad de México", "destino": "Los Cabos", "fecha": "2024-11-22", "precio": "$2000"},
    {"origen": "Estado de México", "destino": "Veracruz", "fecha": "2024-11-28", "precio": "$2000"},
    {"origen": "Guadalajara", "destino": "Ciudad de México", "fecha": "2024-11-22", "precio": "$3000"}
]

# Maneja el comando /start y /hello
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy el bot de Aerolínea Benjíro. Usa /buscar [destino] para encontrar vuelos simulados.")

# Comando para buscar vuelos por destino
@bot.message_handler(commands=['buscar'])
def buscar_vuelos(message):
    try:
        # Obtener el destino buscado
        destino_buscado = message.text.split(" ", 1)[1].strip()
        vuelos_encontrados = [
            vuelo for vuelo in vuelos if vuelo["destino"].lower() == destino_buscado.lower()
        ]

        # Generar la respuesta
        if vuelos_encontrados:
            respuesta = "Vuelos encontrados:\n\n"
            for vuelo in vuelos_encontrados:
                respuesta += (
                    f"Origen: {vuelo['origen']}\n"
                    f"Destino: {vuelo['destino']}\n"
                    f"Fecha: {vuelo['fecha']}\n"
                    f"Precio: {vuelo['precio']}\n\n"
                )
        else:
            respuesta = f"No se encontraron vuelos para el destino: {destino_buscado}"

        bot.reply_to(message, respuesta)

    except IndexError:
        bot.reply_to(message, "Por favor, indica el destino después del comando /buscar. Ejemplo: /buscar Cancún")

# Echo para otros mensajes
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
