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

Learning: Always handle missing file when working with file systems

**Empty title accepted**
This issue can be solved by validation and rules



## Improvement / Future Enhancement
## Key Learnings
create a new repository on git.com
keep it public
do not add repository
once the repository is created, copy the command that git provided and paste in the vs code terminal

Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 2.16 KiB | 2.16 MiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/HudaPatel45/cloud-study-notes.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'. means your code is being pushed
## Screenshots
