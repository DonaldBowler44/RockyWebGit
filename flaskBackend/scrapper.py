import requests
import re
from bs4 import BeautifulSoup
from models.characters import db, Character

def convert_kg_to_pounds(weight):
    kg_pattern = re.compile(r'(\d+)\s*kg')
    match = kg_pattern.search(weight)
    if match:
        kg_value = float(match.group(1))
        pounds_value = round(kg_value * 2.20462, 2)
        weight = kg_pattern.sub(f'{pounds_value} pounds', weight)
    return weight

def scrape_and_save_chracters():
    # List of URLs to scrape from
    urls = [
        "https://rocky.fandom.com/wiki/Rocky_Balboa",
        "https://rocky.fandom.com/wiki/Apollo_Creed",
        "https://rocky.fandom.com/wiki/Ivan_Drago",
        "https://rocky.fandom.com/wiki/James_%22Clubber%22_Lang",
        "https://rocky.fandom.com/wiki/Tommy_Gunn",
        "https://rocky.fandom.com/wiki/Mason_Dixon",
        "https://rocky.fandom.com/wiki/Adonis_Johnson_Creed",
        "https://rocky.fandom.com/wiki/Danny_Wheeler",
        "https://rocky.fandom.com/wiki/Ricky_Conlan",
        "https://rocky.fandom.com/wiki/Viktor_Drago",
        "https://rocky.fandom.com/wiki/Damian_Anderson"
    ]

    for url in urls:
        # Scrape character data from the URL
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        name = soup.find("h1", class_="page-header__title").find("span", class_="mw-page-title-main").text.strip()

         #check if heights field is present
        heights_elem = soup.find("div", {"data-source": "height"})
        if heights_elem:
             height = heights_elem.find("div", class_="pi-data-value").text.strip().replace("\xa0", " ")

            # Remove parentheses information using regex
             height = re.sub(r'\([^)]*\)', '', height) 

            # Convert height from cm to ft and inches
             if height.endswith("cm"):
              cm_value = float(re.findall(r'\d+\.\d+', height)[0])
              total_inches = cm_value * 39.3701
              feet = int(total_inches // 12)
              inches = round(total_inches % 12)
              height = f"{feet} ft {inches} in"
             else:
              #height = "unknown"
              height = re.sub(r'\([^)]*\)', '', height)

        #check if weight field is present
        weight_elem = soup.find("div", {"data-source": "weight"})
        if weight_elem:
            weight = weight_elem.find("div", class_="pi-data-value").text.strip().replace("\xa0", " ")
            weight = convert_kg_to_pounds(weight)  # Convert kg to pounds if necessary
            
        # Remove parentheses information using regex
            weight = re.sub(r'\([^)]*\)', '', weight)
        else:
            weight = "218 pounds"

        total_fights = soup.find("div", {"data-source": "total_fights"}).find("div", class_="pi-data-value").text.strip()
        wins = soup.find("div", {"data-source": "wins"}).find("div", class_="pi-data-value").text.strip()

        # check if the ko field is present
        ko_elem = soup.find("div", {"data-source": "wins_by_ko"})
        if ko_elem:
            wins_by_ko = ko_elem.find("div", class_="pi-data-value").text.strip()
        else:
            wins_by_ko = "0"

        # Check if the "draws" field is present
        draws_elem = soup.find("div", {"data-source": "draws"})
        if draws_elem:
            draws = draws_elem.find("div", class_="pi-data-value").text.strip()
        else:
            draws = "0"

        losses = soup.find("div", {"data-source": "losses"}).find("div", class_="pi-data-value").text.strip()

        # Check if the stance field is present
        stance_elem = soup.find("div", {"data-source": "stance"})
        if stance_elem:
            stance = stance_elem.find("div", class_="pi-data-value").text.strip()
        else:
            stance = "Orthodox"

        save_character(name, height, weight, total_fights, wins, wins_by_ko, draws, losses, stance)

def save_character(name, height, weight, total_fights, wins, wins_by_ko, draws, losses, stance):
    character = Character(
        name=name,
        height=height,
        weight=weight,
        total_fights=total_fights,
        wins=wins,
        wins_by_ko=wins_by_ko,
        draws=draws,
        losses=losses,
        stance=stance
    )
    try:
        db.session.add(character)
        db.session.commit()
        print(f"Character '{name}' saved successfully.")
    except Exception as e:
        db.session.rollback()
        print(f"Failed to save character '{name}'. Error: {str(e)}")

    

    # Print the extracted information
    # print("URL:", url)
    # print("Name:", name)
    # print("Height:", height)
    # print("Weight:", weight)
    # print("Total Fights:", total_fights)
    # print("Wins:", wins)
    # print("Wins by KO:", wins_by_ko)
    # print("Draws:", draws)
    # print("Losses:", losses)
    # print("Stance:", stance)
    # print("--------------------------------")
