# Git Manager

The Application will show you results of exponentiation your args, settled in the file in the remote repository based on git-url ang commit reference you provide.
'https://github.com/yangemba/test-git-manager' - required example.

## Installation
Python 3.7.4

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install git manager.

```bash
pip install - r requirements.txt
```

## Usage

```bash
python main.py -u https://github.com/yangemba/test-git-manager -c e2cd1778c4ff947b0047ef32e74c9df20cf88190 -x 2

```

Arguments:

    -u (--Url) - Url to remote git repository of your current project 
    
    -c (--commit) - Chosen commit reference (hash)
    
    -x (--x_arg) - Settled argument

Result:

    WARNING:root: X^2 = 4!


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Free