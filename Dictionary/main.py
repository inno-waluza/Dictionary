import tkinter as tk
import requests
import json
import tkinter.messagebox as mbox

class DictionaryGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dictionary")

        # Create a label and a text input for the word to search
        self.welcome_label = tk.Label(master, font=("Arial", 16), text="English Dictionary")
        self.welcome_label.pack()
        self.word_label = tk.Label(master, font=("Arial", 16), text="Enter a word to search:")
        self.word_label.pack()
        self.word_entry = tk.Entry(master, width=30, font=("Arial", 16,))
        self.word_entry.pack()

        # Create a button to trigger the search
        self.search_button = tk.Button(master, text="Search", font=("Arial", 16), command=self.search_word)
        self.search_button.pack()

        # Create a label to display the search result
        self.result_label = tk.Label(master, text="", font=("Arial", 13))
        self.result_label.pack()
        
        # Create a label to display by innowaluza
        self.myname_label = tk.Label(master, text="by innowaluza", font=("Arial, 16"))
        self.myname_label.pack()

    def get_meaning(self, word):
        try:
            data = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
            response = data.text
            return response
        except:
            mbox.showerror("Error", "An error occurred while retrieving the word meaning.")
            return ""

    def search_word(self):
        # Retrieve the search term from the input box
        search_term = self.word_entry.get()

        # Clear the previous search result
        self.result_label.config(text='')

        # Use the dictionary API to get the meaning of the word
        json_data = self.get_meaning(search_term)

        if json_data == "":
            # An error occurred, do not continue
            return

        data = json.loads(json_data)

        # Display the meaning of the word if it is found
        if len(data) > 0:
            word = data[0]["word"]
            definitions = []
            for meaning in data[0]["meanings"]:
                part_of_speech = meaning["partOfSpeech"]
                for definition in meaning["definitions"]:
                    definition_text = definition["definition"]
                    definitions.append({"part_of_speech": part_of_speech, "definition_text": definition_text})

            result_text = f"Word: {word}\nDefinitions:\n"
            for definition in definitions:
                result_text += f"{definition['part_of_speech']}: {definition['definition_text']}\n"
            self.result_label.config(text=result_text)
        else:
            # Display an error message if the word is not found
            self.result_label.config(text='Word not found')

if __name__ == '__main__':
    root = tk.Tk()
    dictionary_gui = DictionaryGUI(root)
    root.geometry("900x500+300+200")
    window_icon = tk.PhotoImage(file="Dictionary.png")
    window_icon = window_icon.subsample(16)

    root.iconphoto(True, window_icon)
    root.mainloop()
