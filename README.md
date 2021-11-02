# Essgen v2 

A python tool for generating content based on the topic.<br/>
Google custom search engine is used for fetching links for the given topics.<br/>
API Keys are provided by Google and should be stored in a `.env` file along with the project like:<br/>
```
api = "xxxxxxxx<API_KEY>xxxxxxxx"
cse = "xxxxxxx<CSE>xxxxxxx"
```

To clone and run the repository:<br/>

```
git clone https://github.com/AKP2401/essgenv2.git
cd essgenv2
pip install -r requirements.txt
python run.py
```

The final result can be found in `./out/Output.txt` file.

## Tools used:
  * Python
  * Selenium (Chromedrivers for windows is used)
  * nltk

## Contributors:
  * [Harsita R](https://github.com/harsita122)
  * [Pranay Agarwal](https://github.com/Pranay221)
