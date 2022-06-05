from bs4 import BeautifulSoup
import requests
import os
from past.builtins import raw_input

while True:
    try:

        # getting response from website main page and parsing html using BeautifulSoup
        # Taking user input for which champion to search for.
        response = requests.get("https://www.metasrc.com/5v5")
        html = BeautifulSoup(response.text, "html.parser")
        name = input("Enter the name of the champion:").title()

        # finding the champion the user is looking for and requesting access to the champion's website then parsing it.
        champion = html.find("a", {"data-search-terms-like": f"{name}|{name}"})
        champion_href = champion.get("href")
        response = requests.get(champion_href)
        html = BeautifulSoup(response.text, "html.parser")

        # finding the specific anchors to scrape the champion information from.
        champion_counters_unformatted = html.findAll(class_="_ate82z")
        champions = champion_counters_unformatted[1]
        champion_counters = champions.find_all("a")

        last_champions = []
        # getting the href from the anchor tags
        for champion in champion_counters:
            last_champions.append(champion.get("href"))

        # splitting the href links in order to find out only the champions names.
        actual_champions = [n.split("/") for n in last_champions]

        # finding the champions names using the index of it and printing it.
        upgraded_champions = [n[5] for n in actual_champions]
        for element in upgraded_champions:
            print(element)
    except AttributeError as e:
        print("Invalid input please enter a valid champion name.")

raw_input()
