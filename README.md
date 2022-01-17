# WordleBot
## A bot that solves Wordles

This python bot automatically solves the word-deduction game **[Wordle](https://www.powerlanguage.co.uk/wordle/)**. Its functionality can be broken down into smaller steps, allowing strategies to be tested and compared. 

The source code contains the full dictionary and list of wordles from the original game - be careful if inspecting to avoid spoilers.

## Usage

Download [WordleBot](WordleBot)

Basic solve of today's Wordle:

    from WordleBot import WordleBot
    bot = WordleBot()
    bot.solve()


    WordleBot 🤖 212 4/6

    🟩⬛⬛🟩🟩
    🟩⬛🟩🟩🟩
    🟩⬛🟩🟩🟩
    🟩🟩🟩🟩🟩


For more detailed usage, see [Usage.ipynb](Usage.ipynb).

The bot can employ any of three strategies, a comparison of which can be seen in [StrategyBenchmarks.ipynb](StrategyBenchmarks.ipynb):
- "entropy" which guesses the word that most reduces the entropy in a list of possible words at each stage
- "scored" which chooses the highest-scored word from a pre-sorted list of words, ranked according to the occurrence of unique common letters
- "random" which picks a random possible word  
For "entropy" and "scored" solvers, if all else is equal, the bot chooses the word that is more frequently used.

The bot uses a dictionary of word frequencies, scraped from Google Ngrams, as well as a list of words scored by the occurrence of unique common letters. See [scrape_word_popularities.py](utils/scrape_word_popularities.py) and [CreateScoredDictionary.ipynb](utils/CreateScoredDictionary.ipynb) for details. 
