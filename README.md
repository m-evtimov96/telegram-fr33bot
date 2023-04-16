# telegram-fr33bot
Simple telegram bot

#### 1. Installation
- Clone the repository
- Create and activate virtual environment by your prefer method (venv, conda, poetry etc.)
- In the project folder run `pip install -r requirements.txt` to install the required packages
- Create a new telegram bot following this https://core.telegram.org/bots/features#creating-a-new-bot or anny other tutorial 
- Generate the required KEYS for the API's that the project uses:  <br />
-- https://dadjokes.io/documentation/getting-started  <br />
-- https://openweathermap.org/guide <br />
-- https://platform.openai.com/docs/api-reference/
- Create .env file in the project directory and populate it with the 3 API keys and the Bot key you got from BotFather
- Run the main.py file with python `python3 main.py`

#### 2. Functionality
List of the commands you can use with this bot:
- /dog  - get a random dog picture
- /dog breed  - get a random dog picture from the specified breed
- /dad_joke  - get a random dad joke
- /weather cityname  - get the current weather for the specified city
- /gpt msg body - get respone from ChatGPT3.5
- /img image description - generate image with DALL-E

#### 3. Used resources
- Dog api - https://dog.ceo/dog-api/about
- OpenWeatherMap - https://openweathermap.org/
- DadJokes api - https://dadjokes.io/
- OpenAI - https://openai.com/
