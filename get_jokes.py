import requests
from pyfiglet import figlet_format
from termcolor import colored
import random
import emoji 

f_format = figlet_format("DAD JOKES 2.0", font = "slant")
f_c_format = colored(f_format, 'cyan')
print(f_c_format)

url = "https://icanhazdadjoke.com/search"


flag = True
while flag == True:
    topic = input("Let me tell you a joke! Give me a topic: ")
    response = requests.get(url, 
        headers = {'Accept': 'application/json'},
        params = {'term': topic.lower()}
        ).json()
    total_jokes = response['total_jokes']

    if total_jokes:
        if total_jokes > 1:
            rnd = random.randint(0,total_jokes)
            print(f"I've got {total_jokes} jokes on {topic}. Here's one {emoji.emojize(':grinning_face_with_smiling_eyes:')}")
            print(response['results'][rnd]['joke'])
        else:
            print(f"I've gor only {total_jokes} jokes on {topic}. Here it is {emoji.emojize(':grinning_face_with_smiling_eyes:')}")
            print(response['results'][0]['joke'])
    else:
        print(f"There're not jokes on {topic} {emoji.emojize(':unamused_face:')}. Please try another topic ")

    to_continue = input(f"\nDo you want to continue with another topic {emoji.emojize(':winking_face:')}: (y/n) ")
    
    if to_continue[0].lower() == 'y':
        continue
    else:
        print('See you!')
        flag = False
    
# print(response.json())


# Query String
