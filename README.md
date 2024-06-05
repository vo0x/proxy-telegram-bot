# Telegram Proxy Bot

A Telegram bot built using Pyrogram that provides proxy information to users.

## Features

- Responds to `/start` command with a welcome message.
- Responds to `/getproxy` command by providing a random proxy from a predefined list.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/littleponyhh/proxy-telegram-bot.git
    cd telegram-proxy-bot
    ```

2. **Install the required Python packages:**

    ```sh
    pip install pyrogram
    pip install tgcrypto
    ```

3. **Configure your bot:**

    Replace `'your api_id'`, `'your api_hash'`, and `'your bot_token'` in the script with your actual Telegram API ID, API hash, and bot token.

    ```python
    api_id = int('your api_id')
    api_hash = 'your api_hash'
    bot_token = 'your bot_token'
    ```

4. **Ensure your proxy list is correctly defined:**

    Create a `proxys.py` file containing a list of proxies. Each proxy should be a dictionary with keys `server`, `port`, and `secret`.

    ```python
    proxys = [
        {"server": "proxy1.server.com", "port": "1234", "secret": "secret1"},
        {"server": "proxy2.server.com", "port": "5678", "secret": "secret2"}
        # Add more proxies as needed
    ]
    ```

## Usage

1. **Run the bot:**

    ```sh
    python bot.py
    ```

2. **Interact with the bot on Telegram:**

    - Send `/start` to receive a welcome message.
    - Send `/getproxy` to receive a random proxy from the predefined list.

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
