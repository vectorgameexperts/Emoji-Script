# Google Noto Animation Scraper

Per the the FAQ section of [Google Noto's Animated Emojis](https://googlefonts.github.io/noto-emoji-animation/), 
  > How do I download everything?
  >  
  > Currently, there is no way to download the whole set — the world is not ready for that many simultaneously dancing emoji.  

We challenge that statement as the harbingers of a new world order. So we made a script to generate a CSV to the file names and download links.

[Just want the CSV?](emoji-lotties.csv)

## Run

### Requirements

- ChromeDriver/Gecko. Download a compatible version of chromedriver from [here](https://googlechromelabs.github.io/chrome-for-testing/) and replace the `chromedriver.exe` with your version. 
  
- Python packages
  ```shell
  pip install selenium
  pip install BeautifulSoup4
  pip install lxml
  pip install requests
  ```

### Execute

```shell
python3 emojidownload.py
```
