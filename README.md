# BookBot

A small command-line tool that reads a plain-text book and prints a report with its word count and how many times each letter appears.

My first Python project, built while learning the language with boot.dev.

## Usage

Requires Python 3.

```bash
git clone https://github.com/zellorz/bookbot.git
cd bookbot
python main.py path/to/book.txt
```

You can use any plain-text book, for example one from [Project Gutenberg](https://www.gutenberg.org/) such as *Frankenstein*. Put it in a `books/` folder (ignored by Git) or pass any path.

On Linux/macOS, use `python3` instead of `python`.

## Example output

```
--- Begin report of books/frankenstein.txt ---
<N> words found in the document
The a character was found <N> times
The b character was found <N> times
...
--- End report ---
```

(The counts depend on the text you use.)

## What it does

- Counts words by splitting on whitespace
- Counts letters case-insensitively, ignoring digits and punctuation
- Prints the letters in alphabetical order

## Ideas for next steps

- Sort the letters by frequency
- Add tests
- Accept several files at once