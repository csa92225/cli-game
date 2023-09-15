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
cd src
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

4. Enter a word that matches the chosen topic (ex. If "fruit" is selected as the topic, enter "kiwi" accordingly)

** Important Rules:
- A word must be space sensitive and spelled correctly (ex.New Jersey)
- Only enter a word that was never used before

5. Wait for Dr. Brain to enter a word.
6. Repeat steps 3 and 4 until Dr. Brain can't think of the next word!



https://github.com/csa92225/cli-game/assets/46687564/88d139c3-2c52-40e1-8814-2e1bf490c85e




