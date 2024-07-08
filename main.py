import requests
import json
import time

class nanoTTS:
    def __init__(self):
        self.current_message = ""
        self.filename = "" # Insert your txt file here
        self.last_write_time = 0
        self.channel_ID = "" # Insert your channel ID file here
    
    def write_to_file(self, message):
        current_time = time.time()
        if current_time - self.last_write_time > 1:  # Ensure at least 1 second between writes
            with open(self.filename, "w") as file:
                file.write(message)
            self.last_write_time = current_time
            print(f"New message written: {message.strip()}")
        else:
            print("Write operation skipped (too soon)")
    
    def retrieve_messages(self):
        headers = {
            "authorization": ""  # Insert your authorization token here
        }

        r = requests.get('https://discord.com/api/v9/channels/{channel_ID}/messages', headers=headers) # Change this if not #tts channel

        if r.status_code != 200:
            print(f"Error retrieving messages: {r.status_code}")
            return

        data = json.loads(r.text)

        for value in data:
            user = value["author"]["username"]
            if user == "": # Insert your discord username here
                message = value["content"] + '\n'
                if message != self.current_message:
                    self.current_message = message
                    self.write_to_file(message)
                return  # Exit the method after processing the first new message

        print("No new messages found")

def main():
    test = nanoTTS()
    while True:
        test.retrieve_messages()
        time.sleep(0.5)  # Add a 0.5-second delay between checks

if __name__ == "__main__":
    main()