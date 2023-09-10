# Google Noto Animation Scraper

Per the [the FAQ section](https://googlefonts.github.io/noto-emoji-animation/documentation) of [Google Noto's Animated Emojis](https://googlefonts.github.io/noto-emoji-animation/), 
  > How do I download everything?
  >  
  > Currently, there is no way to download the whole set — the world is not ready for that many simultaneously dancing emoji.  

We challenge that statement as the harbingers of a new world order. So we made a script to generate a CSV to the file names and download links.

[Just want the CSV?](emoji-lotties.csv)

## Run

### Requirements

- ChromeDriver/Gecko. (Chrome) Instructions can be found [here](https://pypi.org/project/chromedriver-autoinstaller/).
- Python packages
  ```shell
  pip install selenium
  pip install BeautifulSoup4
  pip install requests
  ```

### Execute

```shell
python3 emojidownload.py
```
