# ‼💻 explaincmd

A CLI helper that succintly explains commands to help with memorization.

## Installation

You can install `explaincmd` directly from PyPI:

```
pip install explaincmd
```

## Setup

After installation, you need to configure your Anthropic API key. You can do this by running:

```
explaincmd setup YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual Anthropic API key. This will save your API key securely in a configuration file, so you don't need to set it as an environment variable each time.

## Usage

Once you've set up your API key, you can use the tool like this:

```
explaincmd your command description
```

For example:

```bash
$ explaincmd lsof -i :9002 | awk 'NR>1 {print $2}' | xargs kill -9
lsof -i :9002 | awk 'NR>1 {print $2}' | xargs kill -9
│    │         │     │                │       │
│    │         │     │                │       └─ signal 9 (SIGKILL - no mercy)
│    │         │     │                └─ x = execute, args = arguments
│    │         │     └─ NR = Number of Records (skip header)
│    │         └─ awk = "Aho, Weinberger, Kernighan" (text processing)
│    └─ -i = internet connections
└─ ls + of = "list open files"
```


## Development

If you want to contribute or modify the tool:

1. Clone this repository:
   ```
   git clone https://github.com/alramalho/explaincmd.git
   cd explaincmd
   ```

2. Install the package in editable mode:
   ```
   pip install -e .
   ```

3. Make your changes and test them locally.

## Publishing to PyPI

To publish updates to PyPI:

1. Update the version in `pyproject.toml`
2. Build the package: `python -m build`
3. Upload to PyPI: `python -m twine upload dist/*`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## Author

Alex Ramalho ([@alramalho](https://github.com/alramalho))
