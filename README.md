# telegram-fr33bot
Telegram bot that can send you dog pics, tell you the weather, crack dad jokes and use OpenAI models.


## ✅ 1. Functionality

This bot supports the following commands:

| Command               | Description |
|-----------------------|-------------|
| `/dog`                | Get a random dog picture |
| `/dog breed`          | Get a random picture of a specific dog breed |
| `/dad_joke`           | Get a random dad joke |
| `/weather cityname`   | Get current weather data for a given city |
| `/gpt your message`   | Get a response from ChatGPT-3.5 |
| `/img description`    | Generate an image using DALL·E based on your description |

---

## 🛠️ 2. Installation (with [`uv`](https://github.com/astral-sh/uv))

Follow these steps to get the bot running on your machine:

### Prerequisites

- Python 3.13
- [uv](https://github.com/astral-sh/uv) for dependency management


### Step 1: Clone the Repository

```bash
git clone https://github.com/m-evtimov96/telegram-fr33bot.git
cd telegram-fr33bot
```

### Step 2: Set Up the Virtual Environment

Install [UV](https://docs.astral.sh/uv/)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Setup environment and install packages
```bash
uv sync --locked
```

### Step 3: Create a Telegram Bot

Create a new Telegram bot using [BotFather](https://core.telegram.org/bots/features#creating-a-new-bot) and obtain your bot token.

### Step 4: Get API Keys

You will need to sign up and generate API keys for the following services:

- **Dad Jokes API**  
  Sign up at [https://dadjokes.io/documentation/getting-started](https://dadjokes.io/documentation/getting-started) to get an API key.

- **OpenWeatherMap**  
  Create an account at [https://openweathermap.org/guide](https://openweathermap.org/guide) and get your API key from the dashboard.

- **OpenAI API**  
  Go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) and generate your API key.

After that use the provided **sample.env** renaming it to **.env** and populating it with the generated API keys.

### Step 5: Run the Bot

You can run the bot in a terminal, using [Screen](https://linuxize.com/post/how-to-use-linux-screen/), systemd service or any other way you want.

```bash
uv run python3 main.py
```

---

## 🌐 Used APIs & Resources

This bot integrates with several public APIs to provide its features:

- 🐶 **Dog API**  
  [https://dog.ceo/dog-api/about](https://dog.ceo/dog-api/about)  
  Used to fetch random dog images, including breed-specific photos.

- 😂 **Dad Jokes API**  
  [https://dadjokes.io/](https://dadjokes.io/)  
  Provides random dad jokes for light-hearted humor.

- 🌦️ **OpenWeatherMap API**  
  [https://openweathermap.org/](https://openweathermap.org/)  
  Retrieves current weather data for any specified city.

- 🤖 **OpenAI API (ChatGPT & DALL·E)**  
  [https://openai.com/](https://openai.com/)  
  Powers text generation with ChatGPT and image generation with DALL·E.
