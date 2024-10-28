# will-it-run
A CLI scraper app for getting minimal or recommended requirements of a video game without using any browser or stupid GUI.
The app operates by looking through the games with a SteamPowered API and finding the closest match to the name put in by the user.

## Setting up the CLI
After downloading the repository, you need to run the command

``` 
pip3 install --editable .
```

Now the command `$ will-it-run` should work. If it doesn't, you probably need to add it to your PATH.

## Alternative usage
If you don't want to setup the CLI, you can use the script just by running 

```
python3 main.py [game_name] --[options]
```

in the correct folder, you just need to make sure to have all the dependencies installed.

## Dependencies
You can find all the dependencies in the `setup.py` file, it is encouraged to use venv or e.g. conda