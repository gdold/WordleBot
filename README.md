# WordleBot
## A bot that solves Wordles

This python bot automatically solves the word-deduction game **[Wordle](https://www.powerlanguage.co.uk/wordle/)**. Its functionality can be broken down into smaller steps, allowing strategies to be tested and compared. 

The source code contains the full dictionary and list of wordles from the original game - be careful if inspecting to avoid spoilers.

## Usage

Download [WordleBot.py](WordleBot.py)

Basic solve of today's Wordle:

    from WordleBot import WordleBot
    bot = WordleBot()
    bot.set_todays_wordle()
    bot.solve()

    🟨🟩⬛⬛⬛
    ⬛🟩🟨🟩🟩
    ⬛🟩🟩🟩🟩
    🟩🟩🟩🟩🟩

For more detailed usage, see [Usage.ipynb](Usage.ipynb)
