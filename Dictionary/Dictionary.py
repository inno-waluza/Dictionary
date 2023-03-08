import requests
import json
print("Dictionary")

input = input("enter word")
def get_meaning(input):
    data = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{input}")
    response = data.text
    return response

# Load the JSON data from a file or a string
json_data = get_meaning(input) 

# Load the JSON data as a Python object
data = json.loads(json_data)

# Extract the word 
word = data[0]["word"]

definitions = []
for meaning in data[0]["meanings"]:
    part_of_speech = meaning["partOfSpeech"]
    for definition in meaning["definitions"]:
        definition_text = definition["definition"]
        definitions.append({"part_of_speech": part_of_speech, "definition_text": definition_text})

# Print the extracted data
print(f"Word: {word}")
print("Definitions:")
for definition in definitions:
    print(f"{definition['part_of_speech']}: {definition['definition_text']}")


  
