# Project Title 
Cloud Study Notes App(Python)

## Overview
This is a beginner-friendly Python CLI application that allows users to add and view the notes that are stored in a JSON file and include a title, topic, and timestamp.

## Why This Project
- This project is built incrementally to practice file handling, error handling, and basic Python concepts. The initial phase implements a local Python-based Cloud Notes application, which will later be converted into a serverless Azure application using Azure Functions and Blob Storage.

## Tech Stack 
- Pyhton 3.13.5
- Json
- VS Code


## How to Run
1. make sure that the Python is installed
2. open the terminal create a folder using mkdir name_project
3. Run 
python app.py 

## Project structure

cloud-study-notes/

├── app.py

├── notes.json

└── README.md


## Errors & Issues Faced

##Errors and Issues Faced

### FileNotFoundError when notes.json was missing
Error: Program crashed when notes.json did not exist
Cause: The file was being opened without checking existence
Solution: Added try-except block to handle FileNotFoundError
<pre>except FileNotFoundError:
return [] </pre>  
**If file is missing, assume there are no notes yet**
- apps continues running 
- New file will be created later when saving

<pre>except json.JSONDecodeError:
return []</pre>
- app resets to empty notes
- User can continue


Learning: Always handle missing file whrn working with file systems


## Improvement / Future Enhancement
## Key Learnings
## Screenshots
