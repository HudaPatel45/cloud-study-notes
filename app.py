import json
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
   
        

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, topic):
    title = title.strip('!') # the strip() function removes all type of white spaces or special characters in the brackets, the ! in the bracket was removed when data was entered with ! 
    topic = topic.strip()

    if not title or not topic:
        print("Title and Topic cannot be empty.")
        return
    
    if len(title)<3:
        print("Title must be atleast 3 characters.")
        return
    
    if len(topic)<3:
        print("Topic cannot be less than 3 characters")
        return
    
    if len(title)>80 or len(topic)>80:
        print("Please keep the title and topic under 80 characters.")
        return

    notes = load_notes()

    note = {
        "title": title,
        "topic": topic,
        "created_at": datetime.now().isoformat()
    }

    notes.append(note)
    save_notes(notes)
    print(" Note added successfully")

def view_notes():
    notes = load_notes()
    for idx, note in enumerate(notes, start=1):
        print(f"{idx}. {note['title']} - {note['topic']}")

if __name__ == "__main__":
    print("1. Add Note")
    print("2. View Notes")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter note title: ")
        topic = input("Enter topic: ")
        add_note(title, topic)
    elif choice == "2":
        view_notes()
    else:
        print("Invalid option")

