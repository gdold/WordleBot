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

    🟨🟩⬛⬛⬛
    ⬛🟩🟨🟩🟩
    ⬛🟩🟩🟩🟩
    🟩🟩🟩🟩🟩

For more detailed usage, see [Usage.ipynb](Usage.ipynb).

The bot can employ any of three strategies, a comparison of which can be seen in [StrategyBenchmarks.ipynb](StrategyBenchmarks.ipynb):
- "entropy" which guesses the word that most reduces the entropy in a list of possible words at each stage
- "scored" which chooses the highest-scored word from a pre-sorted list of words, ranked according to the occurrence of unique common letters
- "random" which picks a random possible word  

The bot includes a dictionary that has been scored by the occurrence of unique common letters, and sorted by that score. See [CreateScoredDictionary.ipynb](CreateScoredDictionary.ipynb) for details. 
