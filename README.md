# Flashcards app

A very simple learning application that runs in the browser.

It receives either a `xlsx` or `csv` file, using the first two columns to populate a series of flashcards for you to practice anything you want to learn. I have decided I will commit my french-learning files to this repository as samples.

# Setup

Best experience using online version at [pabsan-0.github.io/flashcards-app](https://pabsan-0.github.io/flashcards-app). On android, I suggest you "install" it from your web browser (like a mere shortcut, but more convenient view).

To deploy and run locally:

```
git clone https://github.com/pabsan-0/flashcards-app
cd flashcards-app
python3 -m http.server 8000
xdg-open localhost:8000
```

# Using your own flashcards

## Using custom files

- Create a `xlsx` or `csv` file with whatever you want to learn. Google Sheets is free and available at the browser
- Save that file to a location in your phone or PC
- Open the application and select Custom File
- Select your file
- Start learning!

## Adding presets

- Create a `xlsx` or `csv` file with whatever you want to learn. Google Sheets is free and available at the browser
- Clone or fork the repo
- Add the `xlsx` or `csv` file in the `presets/` dir
- Run `presets.py` to auto-update the filelist `presets.json` (or edit by hand)
- Open the application and select Presets
- Start learning!


# Motivation

This is a very simple app, and there are many available which achieve the same purpose. However, the ones I liked had ads, hence I chose to build my own.
