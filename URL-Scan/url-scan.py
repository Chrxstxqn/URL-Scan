import requests
import urllib
import json
import time
import os

def print_fire_text(text):
    fire_colors = ['\033[38;5;202m', '\033[38;5;208m', '\033[38;5;214m', '\033[38;5;220m', '\033[38;5;226m', '\033[38;5;202m']
    for i, char in enumerate(text):
        print(f"{fire_colors[i % len(fire_colors)]}{char}", end='')
    print('\033[0m')

def print_fire_title():
    title = [
        "         (   (      (                   )    ",
        "         )\ ))\ )   )\ )  (    (     ( /(    ",
        "      ( (()/(()/(  (()/(  )\   )\    )\())   ",
        "      )\ /(_))(_))  /(_)|((_|(((_)( ((_)\    ",
        "   _ ((_|_))(_))   (_)) )\___)\ _ )\ _((_)   ",
        "  | | | | _ \ |    / __((/ __(_)_\(_) \| |   ",
        "  | |_| |   / |__  \__ \| (__ / _ \ | .` |   ",
        "   \___/|_|_\____| |___/ \___/_/ \_\|_|\_|   ",  
        "                ig: i.chrxstxqn              ",
        "            beta 2.0  by Chrxstxqn           ",                                           
        "   ~https://github.com/Chrxstxqn/URL-Scan~   ",
        "                                             ",
    ]

    for line in title:
        print_fire_text(line)

def print_fire_json(data):
    formatted_data = json.dumps(data, indent=4)
    print_fire_text(formatted_data)

def print_fire_menu():
    menu = "    [0] Exit     [1] Scan again    "
    print_fire_text(menu)

def print_footer():
    print(" ")
    print_fire_text("Thanks for using! <3")
        print_fire_text("Support me on Instagram: 'i.chrxstxqn'")

def main():
    while True:
        print_fire_title()

        url = input("Insert URL to scan: ")
        encoded_url = urllib.parse.quote(url, safe='')
        api_url = "https://ipqualityscore.com/api/json/url/6iP3Ci09b83suqDijoQ4pHSD9uayadBp/"
        response = requests.get(api_url + encoded_url)

        try:
            data = response.json()
            print_fire_json(data)
        except json.decoder.JSONDecodeError:
            print_fire_text("Error: Invalid JSON response from the API.")

        print_footer()
        
        print("  ")
        print("  ")

        print_fire_menu()
        choice = input("Select an option: ")
        if choice == "0":
            break
        elif choice != "1":
            print_fire_text("Invalid choice. Exiting...")
            break

if __name__ == "__main__":
    main()
