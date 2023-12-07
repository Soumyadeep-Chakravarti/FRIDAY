import webbrowser
import urllib.parse

def browse(url):
    try:
        webbrowser.open(url)
        print(f"Opening {url} in the default web browser.")
    except Exception as e:
        print(f"Error: {e}")

def open_mail():
    try:
        # Open the default mail client
        webbrowser.open("mailto:")
        print("Opening default mail client.")
    except Exception as e:
        print(f"Error: {e}")

def search(query):
    search_url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    try:
        webbrowser.open(search_url)
        print(f"Searching for '{query}' on Google.")
    except Exception as e:
        print(f"Error: {e}")