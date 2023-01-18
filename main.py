import os
import logging
import requests
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler


load_dotenv()
BOT_TOKEN = os.getenv("BOT_API_KEY")
DAD_JOKE_TOKEN = os.getenv("DAD_JOKE_KEY")
WEATHER_TOKEN = os.getenv("WEATHER_API_KEY")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def dog(update, context):
    request_url = "https://dog.ceo/api/breeds/image/random"

    args = context.args
    if args:
        dog_breed = "/".join(args[::-1])
        request_url = f"https://dog.ceo/api/breed/{dog_breed}/images/random"

    data = requests.get(url=request_url).json()

    try:
        dog_photo = data["message"]
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=dog_photo)
    except KeyError:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Breed not found",
        )


async def dad_joke(update, context):
    request_url = "https://dad-jokes.p.rapidapi.com/random/joke"
    headers = {
        "X-RapidAPI-Key": DAD_JOKE_TOKEN,
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
    }

    data = requests.get(url=request_url, headers=headers).json()
    joke_start = data["body"][0]["setup"]
    joke_end = data["body"][0]["punchline"]

    await context.bot.send_message(chat_id=update.effective_chat.id, text=joke_start)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=joke_end)


async def weather_now(update, context):
    try:
        city = context.args[0]
        request_link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_TOKEN}"
        data = requests.get(url=request_link).json()
        msg_string = f"""Current weather for {city}:\n
        Description: {data["weather"][0]["description"]}\n
        Temperature: {data["main"]["temp"]}℃\n
        Feels like: {data["main"]["feels_like"]}℃\n
        Humidity: {data["main"]["humidity"]}%"""

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=msg_string,
        )

    except IndexError:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please provide city name like so: /weather Cityname",
        )
    except KeyError:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please provide valid city name.",
        )


if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)
    dog_handler = CommandHandler("dog", dog)
    dad_joke_handler = CommandHandler("dad_joke", dad_joke)
    weather_now_handler = CommandHandler("weather", weather_now)

    application.add_handler(start_handler)
    application.add_handler(dog_handler)
    application.add_handler(dad_joke_handler)
    application.add_handler(weather_now_handler)

    application.run_polling(stop_signals=None)
