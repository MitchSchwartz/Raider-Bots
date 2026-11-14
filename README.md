# Raider Bots

Discord bots I wrote in 2022 for the Crypto Raiders community. One Python script runs all of them, so a single free worker covers the lot.

- **Price bots** show the $RAIDER and $AURUM prices (and a few in-game token prices in $AURUM) as the bot's nickname in every server it's in, refreshed every minute.
- **Countdown bots** count down to the daily reset and to the next tournament.

A small Flask server runs alongside so the host sees a web process and the bots update on a timer.

The repo is no longer maintained. Prices came from the Nomics API, which has shut down, so the price bots won't run as they are. The structure is the useful part.

## How it works

- `main.py` starts the web server, brings every bot in `botList` online, and runs the update loop in a thread.
- `scripts/bot_class_def.py` defines the `Bot` class and the list of bots.
- `scripts/get_token_values.py` fetches prices.
- `scripts/reset_timer_update.py` and `scripts/tournament_timer_update.py` drive the countdowns.
- `scripts/endpoints.py` holds the Flask routes and the update loop.

## Configuration

Each bot's Discord token is an environment variable named after the bot (`raiderBot`, `aurumBot`, `resetTimerBot`, and so on). `nomicsKey` is the price API key. Set `testMode=True` to update only a test server. Locally, put them in a `.env` file, which is loaded at startup and should stay out of git.

```
pip install -r requirements.txt
python main.py
```

The `Procfile` runs it as a worker on Heroku-style hosts.

## Write-ups

- [Price and countdown timer bots that update every minute](https://opsmachine.co/blog/creating-discord-token-price-countdown-timer-bots-that-update-every-minute-with-free-hosting/)
- [Building and hosting multiple Discord bots in one Python script](https://opsmachine.co/blog/discord-bots-v4-building-and-hosting-multiple-discord-bots-in-one-python-script/)
