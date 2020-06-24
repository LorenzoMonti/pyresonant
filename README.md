# Pyresonant

Pyresonant allows the user to use any stringed instrument as a pc keyboard. This is possible thanks to the mapping of the notes with the keys.

## Download and install

This project is written in Python3, so make sure you have it installed in your machine.
After that you can download this repository, open terminal and type:
```bash
git clone https://github.com/LorenzoMonti/pyresonant.git
```

## Project's dependecies

```bash
cd pyresonant/
pip3 install -r requirements.txt
```
## Launch the main script

Now you can run the project:

```bash
python3 pyresonant.py --input 1 --mappingcsv ./example_mapping.csv
```
change (or create a new one) csv file according to your needs.


## CLI (command line interface)

| Flag | Description |
| --- | --- |
| `--input` | select your audio input device  |
| `--volthresh` | select volume threshold |
| `--mapping` | map notes with keys with this pattern: note-key,note-key |
| `--mappingcsv` | add the path of the csv with this pattern: note,key. You can find an example in *example_mapping.csv* |

## License

[MIT](https://choosealicense.com/licenses/mit/)
