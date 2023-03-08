import requests
print("Dictionary")

def get_word():
    word = input("enter word")
    return word

def get_meaning(word):
    data = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    response = data.json()
    return response

word = get_word()
print(get_meaning(word)[0][''])



  
