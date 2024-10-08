# Simple guess the number game build using [Nada by Nillion](https://docs.nillion.com/nada-lang)
## Description
Simple game to guess the number, party1 stores number onchain and then party2 tries to guess it.
Idea is that party1 can store secret number and give store id to party2, and party2 using just its is can try to guess number many times, while he didnt guess (or tired:))
## How to run
> [!IMPORTANT]
>You'll need python3 version 3.11 or higher with a working pip installed to import the nada_dsl dependency. Before setting up your Python virtual environment, confirm that you have python3 (version >=3.11) and pip installed!
```
python3 --version
python3 -m pip --version
```
_____________________
1. Install Nillion sdk using [official guide](https://docs.nillion.com/quickstart-install)
2. Clone this repo
```
git clone https://github.com/JeTr1x/guess_num_nada_game/
```
3. Create venv, activate it and install nada-dsl
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade nada-dsl
```
4. Run the nada build command to compile programs.

```
nada build
```
5. Run the program with test values

```
nada run guess_num_test
```
6. Test the program
```
nada test guess_num_test
```
