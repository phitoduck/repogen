# repogen

The goal of this project is to automate the creation and configuration of GitHub repositories.

The idea is that any team working with Python could use this repository as a reference implemetation
and customize their own platform in a way that fits their team's opinions.

There are two components to this platform:

1. [`phitoduck-projen`](https://github.com/phitoduck/phito-projen), a library of Python-based `projen` "Components" (building blocks) for generating scaffolded Python projects
2. `repogen`, a GUI tool (via GitHub actions) for creating configured GitHub repositories with boilerplate projects

