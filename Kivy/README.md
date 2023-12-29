# Install Kivy pre-requisite tools
$ python -m pip install --upgrade pip setuptools virtualenv

# Create a virtual environment
$ python -m venv kivy_venv

# Activate virtual environment
$ source kivy_venv/bin/activate

# Install kivy with base dependencies and examples
$ python -m pip install "kivy[base]" kivy_examples

# Check the installed packages in virtual environment
(venv) [admin@fedser Kivy]$ pip freeze
certifi==2022.6.15
charset-normalizer==2.1.0
docutils==0.19
idna==3.3
Kivy==2.1.0
Kivy-examples==2.1.0
Kivy-Garden==0.1.5
Pillow==9.2.0
Pygments==2.12.0
requests==2.28.1
urllib3==1.26.11
