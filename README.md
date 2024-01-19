# Google Noto Animation Scraper

Per the the FAQ section of [Google Noto's Animated Emojis](https://googlefonts.github.io/noto-emoji-animation/),
  > How do I download everything?
  >
  > Currently, there is no way to download the whole set — the world is not ready for that many simultaneously dancing emoji.

This is a script to make the world ready.

[Just want the CSV?](emoji-lotties.csv)

## Run

### Requirements

- ChromeDriver/Gecko. Download a compatible version of chromedriver from [here](https://googlechromelabs.github.io/chrome-for-testing/) and make the driver available in your `$PATH`.

- Scrape

  If you want a fresh list, and not [the one we already compiled for you](emoji-lotties.csv):

  ```shell
  pip install -r requirements.txt
  python3 scrape.py
  ```

- Download only

  ```shell
  pip install -r requirements.txt
  python3 download.py
  ```
