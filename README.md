# python-solidity-parser
An experimental Solidity parser for Python built on top of a robust ANTLR4 grammar.


## Generate the parser

Update the grammar in `./solidity-antlr4/Solidity.g4` and run the antlr generator script to create the parser classes in `solidity_parser/solidity_antlr4`.
```
#> bash script/antlr4.sh


## Update the Core Library

Download the Solidity.g4 file:
https://github.com/antlr/grammars-v4/tree/master/solidity
This file defines the latest Solidity syntax.

Install antlr4:
https://github.com/antlr/antlr4/blob/master/doc/getting-started.md

Generate Python targets:

Run the following command in the specified directory of the Solidity.g4 file:

Requires java11

```python -D
antlr4 -Dlanguage=Python3 -visitor Solidity.g4
venv/bin/antlr4 -Dlanguage=Python3 -visitor solidity-antlr4/Solidity.g4 -o solidity_parser/solidity_antlr4/
```

This will generate the relevant target files. Replace all files in `src/solidity_parser/solidity_antlr4/` with the generated files.
