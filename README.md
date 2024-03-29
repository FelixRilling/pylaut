# PyLaut

Simple Python script allowing for key sequence input triggered text replacement.

## Dependencies

- Requires Python 3.x.
- Install the python modules listed in `requirements.txt` using your package manager or pip.

## Usage

Start `main.py`. Now, typing any of the defined sequences will trigger them to be replaced.

The default key sequence bindings can be found in the [default config](./config.yaml). A custom configuration file with
different bindings can be set using the config flag (`-c` or `--config`).

## Notes

- Should work in every environment where [pynput](https://pynput.readthedocs.io/en/latest/index.html) works.
	- See <https://pynput.readthedocs.io/en/latest/limitations.html> for details.
	- When using wayland, some tweaks may be required. See <https://github.com/moses-palmer/pynput/issues/408> for
	  details.
- Be careful not to register bindings which may trigger themselves or others upon replacement.
- Due to the design of this script, removing characters (e.g. typos) from the sequence and continuing typing it will
  prevent the script from registering the sequence. The sequence has to be written without any other key inputs in
  between.
