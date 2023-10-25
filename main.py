import os
import logging
import requests
import openai
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler


load_dotenv()
BOT_TOKEN = os.getenv("BOT_API_KEY")
RAPID_TOKEN = os.getenv("RAPID_API_KEY")
WEATHER_TOKEN = os.getenv("WEATHER_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

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

    if data["status"] != "error":
        dog_photo = data["message"]
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=dog_photo)
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=data["message"],
        )


async def dad_joke(update, context):
    request_url = "https://dad-jokes.p.rapidapi.com/random/joke"
    headers = {
        "X-RapidAPI-Key": RAPID_TOKEN,
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


async def gpt_chat(update, context):
    msg = " ".join(context.args)
    if msg:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": msg}
            ]
        )
        respone = completion.choices[0].message["content"]

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=respone,
        )

    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please provide message like so: /gpt Hello!",
        )


async def gpt_img(update, context):
    msg = " ".join(context.args)
    if msg:
        image = openai.Image.create(
            prompt=msg,
            n=1,
            size="512x512"
        )
        image_url = image["data"][0]["url"]

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=image_url
        )

    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Please provide image description like so: /img flying bear",
        )


if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)
    dog_handler = CommandHandler("dog", dog)
    dad_joke_handler = CommandHandler("dad_joke", dad_joke)
    weather_now_handler = CommandHandler("weather", weather_now)
    gpt_chat_handler = CommandHandler("gpt", gpt_chat)
    gpt_img_handler = CommandHandler("img", gpt_img)

    handlers = [
        start_handler,
        dog_handler,
        dad_joke_handler,
        weather_now_handler,
        gpt_chat_handler,
        gpt_img_handler,
    ]
    application.add_handlers(handlers)

    application.run_polling(stop_signals=None)
