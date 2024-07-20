# Telegram Proxy Bot

A Telegram bot built using Pyrogram that provides proxy information to users.



## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/1ns8/proxy-telegram-bot.git
    cd proxy-telegram-bot
    ```

2. **Install the required Python packages:**

    ```sh
   pip3 install -r requirements.txt
    ```
    or
   ```sh
   pip3 install pyrogram
   pip3 install tgcrypto
   ```

4. **Configure your bot:**

    Replace `'your api_id'`, `'your api_hash'`, and `'your bot_token'` in the proxy-bot/main.py with your actual Telegram API ID, API hash, and bot token.

    ```python
    api_id = int('your api_id')
    api_hash = 'your api_hash'
    bot_token = 'your bot_token'
    ```

5. **Ensure your proxy list is correctly defined:**

    just add your proxys to proxys list in the main.py file
   ```python
   proxys = ['proxy_1', ....]
   ```

## Usage

1. **Run the bot:**

    ```sh
    python main.py
    ```

2. **Interact with the bot on Telegram:**

    - Send `/start` to receive a welcome message.
    

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Contact

- [Telegram Channel](https://t.me/NS8_b)

Feel free to open an issue if you have any questions or suggestions.
