# Scraplex

Scraplex is a Python software for scraping company's from google maps. 

## Information

Since the latest update, you don't need to install an external chromedriver. We are using the package "webdriver-manager"
to install and manage the webdriver. 

If you are running into errors, e.g. a wrong xpath please create a issue. It is possible that Google  is changing the 
classes, paths and id's from elements Scraplex is using.

## Package-Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libs.

```bash
pip install -r requirements.txt
```


## Usage

```python
# start the software
python scraper.py
```

## Output
Scraplex creates 3 files while running: links.txt which is used to save the links from scraped companys and 
export.json which is used to save information about the scraped companys. Both files will be deleted after Scraplex
is finished. The only relevant file will be *output.json* - it's created with right syntax and every
neccessary information about the scraped companys.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)