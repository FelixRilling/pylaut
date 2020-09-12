# PyLaut

Simple Python script allowing for key sequence input triggered text replacement.

## Dependencies

Requires Python 3.x and pip.
 
 ```shell script
pip install -r requirements.txt
```
 
## Usage

Configure the sequence bindings in `config.yaml` to fit your needs, then start `main.py`.

Now, typing any of the defined sequences will trigger them to be replaced.

The default key sequence bindings are:

- Acronyms
    - `asap;` -> `as soon as possible`
- German umlauts
    - `ss;` -> `ß`
    - `ae;` -> `ä`
    - `Ae;` -> `Ä`
    - etc.

## Notes

- Should work in every environment where pynput works, namely Linux (Under an X server), Windows and macOS.
    - See <https://pynput.readthedocs.io/en/latest/limitations.html> for details.
- Be careful not to register bindings which may trigger themselves or others upon replacement.
- Due to the design of this script, removing characters (e.g. typos) from the sequence and continuing typing it will prevent the script from registering the sequence. The sequence has to be written without any other key inputs in between.