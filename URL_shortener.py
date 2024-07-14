# url_shortener.py

import pyshorteners

class URLShortener:
    def __init__(self):
        self.shortener = pyshorteners.Shortener()

    def shorten_url(self, url):
        try:
            if not url:
                return {"error": "Empty URL. Please enter a valid URL."}

            shortened_url = self.shortener.tinyurl.short(url)
            return {"shortened_url": shortened_url}

        except pyshorteners.exceptions.NoURLException:
            return {"error": "Invalid URL. Please enter a valid URL."}

        except pyshorteners.exceptions.ShorteningErrorException:
            return {"error": "Unable to shorten the URL. Please try again later."}

        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}
