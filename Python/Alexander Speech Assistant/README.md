# Alexander-Speech-Assistant
A python speech assistant using google voice recognition 
  
The follwing packages need to be installed before running the program:  
- speechrecognition  
- pyaudio  
- gtts
- playsound==1.2.2  
- pyobjc  
  
You can use pip install to install the packages needed. For example:  
`pip install speechrecognition`

Then you can run the program using the command:
`python main.py`

## Commands
The program currently understands the following commands:
- What is your name?
  - The program will reply with it's name, Alexander
- What time is it?
  - The program will reply with the current time
- Search
  - The program will ask, what do you want to search for?
  - Then it will wait for you to tell it what to search for
  - It will then reply with the search result
- Find location
  - The program will ask for the location you're looking for
  - It will wait for your answer
  - Then it will open a Google maps resutls
