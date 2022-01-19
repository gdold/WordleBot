# WordleBot
## A bot that solves Wordles

This python bot automatically solves the word-deduction game **[Wordle](https://www.powerlanguage.co.uk/wordle/)**. Its functionality can be broken down into smaller steps, allowing strategies to be tested and compared. 

The source code contains the full dictionary and list of wordles from the original game - be careful if inspecting to avoid spoilers.

## Installation

`pip install wordlesolver`

Or, download this repo and run `python setup.py install`

## Usage

WordleBot installs as a python library and a console script. You can call it direct from the command line (with the commands `wordlebot` or `wordlesolver`), optionally specifying the wordle number, a 5-letter word, or `random`:

    $ wordlebot
    WordleBot 🤖 210 4/6
    
    ⬛⬛🟨⬛⬛
    ⬛🟩⬛🟩🟨
    ⬛🟩🟩🟩🟩
    🟩🟩🟩🟩🟩

or import is a a python library:

    >>> from WordleBot import WordleBot
    >>> bot = WordleBot()
    >>> bot.solve()
    WordleBot 🤖 210 4/6
    
    ⬛⬛🟨⬛⬛
    ⬛🟩⬛🟩🟨
    ⬛🟩🟩🟩🟩
    🟩🟩🟩🟩🟩

For more detailed usage, run `wordlebot -h` or see [Usage.ipynb](Usage.ipynb).

The bot can employ any of three strategies, a comparison of which can be seen in [StrategyBenchmarks.ipynb](StrategyBenchmarks.ipynb):
- "entropy" which guesses the word that most reduces the entropy in a list of possible words at each stage
- "scored" which chooses the highest-scored word from a pre-sorted list of words, ranked according to the occurrence of unique common letters
- "random" which picks a random possible word  

The bot includes a dictionary that has been scored by the occurrence of unique common letters, and sorted by that score. See [CreateScoredDictionary.ipynb](utils/CreateScoredDictionary.ipynb) for details. 
