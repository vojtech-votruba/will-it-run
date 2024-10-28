# will-it-run
A CLI app for getting minimal or recommended requirements of a video game without using a browser or any stupid GUI.
The app operates by looking through the games with a SteamPowered API and finding the closest match to the name put in by the user.

## Setting up the CLI
After downloading the repository, you need to run the command

``` 
pip3 install --editable .
```

Now the command `$ will-it-run` should work.

## Alternative usage
If you don't want to set up the CLI, you can use the script just by running 

```
python3 main.py [game_name] --[options]
```

in the correct folder, you need to make sure that all the dependencies are installed.

## Dependencies
You can find all the dependencies in the `setup.py` file, it is encouraged to use venv or e.g. conda
