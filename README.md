# PyLaut

Simple Python script allowing for key sequence input triggered text replacement.

## Dependencies

Requires Python 3.x and pip.
 
 ```shell script
pip install -r requirements.txt
```
 
## Usage

Start `main.py`. Now, typing any of the defined sequences will trigger them to be replaced.

The default key sequence bindings can be found in the [default config](./config.yaml).

Using the config flag (`-c` or `--config`) a custom configuration file with different bindings can
be set.

## Notes

- Should work in every environment
  where [pynput](https://pynput.readthedocs.io/en/latest/index.html) works.
    - See <https://pynput.readthedocs.io/en/latest/limitations.html> for details.
- Be careful not to register bindings which may trigger themselves or others upon replacement.
- Due to the design of this script, removing characters (e.g. typos) from the sequence and continuing typing it will prevent the script from registering the sequence. The sequence has to be written without any other key inputs in between.
