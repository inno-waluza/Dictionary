import requests
import json
print("Dictionary")

input = input("enter word")
def get_meaning(input):
    data = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{input}")
    response = data.text
    return response

# Load the JSON data from a file or a string
json_data = get_meaning(input) ##'[{"word": "hello", "phonetic": "həˈləʊ", "phonetics": [{"text": "həˈləʊ", "audio": "//ssl.gstatic.com/dictionary/static/sounds/20200429/hello--_gb_1.mp3"}, {"text": "hɛˈləʊ"}], "origin": "early 19th century: variant of earlier hollo ; related to holla.", "meanings": [{"partOfSpeech": "exclamation", "definitions": [{"definition": "used as a greeting or to begin a phone conversation.", "example": "hello there, Katie!", "synonyms": [], "antonyms": []}]}, {"partOfSpeech": "noun", "definitions": [{"definition": "an utterance of ‘hello’; a greeting.", "example": "she was getting polite nods and hellos from people", "synonyms": [], "antonyms": []}]}, {"partOfSpeech": "verb", "definitions": [{"definition": "say or shout ‘hello’.", "example": "I pressed the phone button and helloed", "synonyms": [], "antonyms": []}]}]}]'

# Load the JSON data as a Python object
data = json.loads(json_data)

# Extract the word and phonetic
word = data[0]["word"]
#phonetic = data[0]["phonetic"]

# Extract the definitions
definitions = []
for meaning in data[0]["meanings"]:
    part_of_speech = meaning["partOfSpeech"]
    for definition in meaning["definitions"]:
        definition_text = definition["definition"]
        definitions.append({"part_of_speech": part_of_speech, "definition_text": definition_text})

# Print the extracted data
print(f"Word: {word}")
##print(f"Phonetic: {phonetic}")
print("Definitions:")
for definition in definitions:
    print(f"{definition['part_of_speech']}: {definition['definition_text']}")


  
