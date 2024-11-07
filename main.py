import os
import telebot
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar el token del bot
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Maneja el comando /start y /hello
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy el bot de Aerolínea Benjíro. Usa los comandos para encontrar vuelos simulados.")

# Comando simulado de búsqueda de vuelos
@bot.message_handler(commands=['buscar_simulado'])
def buscar_vuelos_simulado(message):
    # Simulación de respuesta de búsqueda
    origen = "CDMX"
    destino = "Cancún"
    fecha = "2024-12-15"
    precio = "$3000 MXN"

    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: {origen}\n"
        f"Destino: {destino}\n"
        f"Fecha: {fecha}\n"
        f"Precio: {precio}"
    )

    bot.reply_to(message, respuesta)

# Comandos simulados adicionales
@bot.message_handler(commands=['buscar_vuelo1'])
def buscar_vuelo1(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: CDMX\n"
        f"Destino: Guadalajara\n"
        f"Fecha: 2024-12-20\n"
        f"Precio: $2500 MXN"
    )
    bot.reply_to(message, respuesta)

@bot.message_handler(commands=['buscar_vuelo2'])
def buscar_vuelo2(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: Monterrey\n"
        f"Destino: CDMX\n"
        f"Fecha: 2024-12-25\n"
        f"Precio: $2800 MXN"
    )
    bot.reply_to(message, respuesta)

@bot.message_handler(commands=['buscar_vuelo3'])
def buscar_vuelo3(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: CDMX\n"
        f"Destino: Mérida\n"
        f"Fecha: 2025-01-05\n"
        f"Precio: $3500 MXN"
    )
    bot.reply_to(message, respuesta)

@bot.message_handler(commands=['buscar_vuelo4'])
def buscar_vuelo4(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: Tijuana\n"
        f"Destino: CDMX\n"
        f"Fecha: 2024-11-30\n"
        f"Precio: $2700 MXN"
    )
    bot.reply_to(message, respuesta)

@bot.message_handler(commands=['buscar_vuelo5'])
def buscar_vuelo5(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: CDMX\n"
        f"Destino: Los Cabos\n"
        f"Fecha: 2024-12-10\n"
        f"Precio: $3200 MXN"
    )
    bot.reply_to(message, respuesta)

@bot.message_handler(commands=['buscar_vuelo6'])
def buscar_vuelo6(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: Cancún\n"
        f"Destino: CDMX\n"
        f"Fecha: 2024-12-15\n"
        f"Precio: $3000 MXN"
    )
    bot.reply_to(message, respuesta)

@bot.message_handler(commands=['buscar_vuelo7'])
def buscar_vuelo7(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: CDMX\n"
        f"Destino: Oaxaca\n"
        f"Fecha: 2024-12-05\n"
        f"Precio: $2600 MXN"
    )
    bot.reply_to(message, respuesta)

@bot.message_handler(commands=['buscar_vuelo8'])
def buscar_vuelo8(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: Puebla\n"
        f"Destino: CDMX\n"
        f"Fecha: 2024-12-08\n"
        f"Precio: $2200 MXN"
    )
    bot.reply_to(message, respuesta)

@bot.message_handler(commands=['buscar_vuelo9'])
def buscar_vuelo9(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: CDMX\n"
        f"Destino: Villahermosa\n"
        f"Fecha: 2024-12-18\n"
        f"Precio: $3100 MXN"
    )
    bot.reply_to(message, respuesta)

@bot.message_handler(commands=['buscar_vuelo10'])
def buscar_vuelo10(message):
    respuesta = (
        f"Vuelos simulados encontrados:\n"
        f"Origen: León\n"
        f"Destino: CDMX\n"
        f"Fecha: 2024-12-12\n"
        f"Precio: $2400 MXN"
    )
    bot.reply_to(message, respuesta)

# Echo para otros mensajes
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
