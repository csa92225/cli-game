# Wordmaster Challenge game

Challenge your word knowledge against Dr. Brain, the city's most knowledgeable individual, in this CLI game. Select a topic and compete to see who can come up with the most words!

### To get started

```sh
python3 -m venv venv
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

To see details of the command:

```sh
python3 main.py --help
```

### How to play:

1. Run below command to begin:

```sh
cd src
python3 main.py
```

2. Choose the game topic.
3. Choose your difficulty level, which determines how much time you have to answer. If you can't answer before the timer runs out, you'll lose:

- Easy: 10 seconds
- Medium: 6 seconds
- Hard: 3 seconds

4. Enter a word that matches the chosen topic. \*Please note that it is case and space sensitive.
   ex. if "fruit" is selected as the topic, enter "kiwi" accordingly.

5. Wait for Dr. Brain to enter a word.
6. Repeat steps 3 and 4 until Dr. Brain can't think of the next word!
