# Varnan

[![Python package](https://github.com/AmitGupta7580/Varnan/actions/workflows/python-package.yml/badge.svg)](https://github.com/AmitGupta7580/Varnan/actions/workflows/python-package.yml)
[![Latest Version][mdversion-button]][md-pypi]
[![Python Versions][pyversion-button]][md-pypi]
[![MIT License][mitlicense-button]][mitlicense]

[build-button]: https://github.com/Python-Markdown/markdown/workflows/CI/badge.svg?event=push
[build]: https://github.com/Python-Markdown/markdown/actions?query=workflow%3ACI+event%3Apush
[codecov-button]: https://codecov.io/gh/Python-Markdown/markdown/branch/master/graph/badge.svg
[mdversion-button]: https://img.shields.io/badge/pypi-v3.3.6-orange
[md-pypi]: https://pypi.org/project/Markdown/
[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
[mitlicense-button]: https://img.shields.io/badge/license-MIT-yellow
[mitlicense]: https://opensource.org/licenses/MIT

A CTF-writeup tool

## Documentation

### <b>Commands</b>

1. ### Initilaize CTF Workspace <br>
    Initialize Standard Workspace
    ```
    varnan init
    ```
    Initialize Customized Workspace according to the CTF
    ```
    varnan init --name CTF_NAME --ctf CTF_LINK --creds USERNAME:PASSWORD
    ```
2. ### Link CTF
    Update the workspace according to the linked CTF Challanges and fetch realtime stats of CTF
    ```
    varnan link --ctf CTF_LINK --creds USERNAME:PASSWORD
    ```
3. ### Show Statistics
    Show Total Points and total solved challanges in the CTF. If it was linked with a real online hosted CTF then it will also display overall rank of yours
    ```
    varnan stats
    ```
4. ### List Categories
    List all the present CTF Catagories in the workspace
    ```
    varnan category list
    ```
5. ### Add Category
    Add CTF Category in the workspace
    ```
    varnan category add -c category_NAME
    ```
6. ### Remove Category
    Remove CTF Category in the workspace
    ```
    varnan category remove -c category_NAME
    ```
7. ### List Tasks (Solved / unsolved)
    List all the present CTF Tasks in the workspace
    ```
    varnan task list
    ```
8. ### Add Task
    Add CTF Task in the workspace
    ```
    varnan task add -tn TASK_NAME --desc DESCRIPTION -c category_NAME --points POINTS --attatchments ATTATCHMENT_LINK
    ```
9. ### Remove Task
    Remove CTF Task in the workspace
    ```
    varnan task remove -tn TASK_NAME -c category_NAME
    ```
10. ### Solve Task
    Mark CTF Task as solved
    ```
    varnan task solve -c category_NAME -tn TASK_NAME --flag FLAG
    ```
11. ### Generate complete CTF README
    Parse over all catagories and task to generate a final README file for whole CTF with proper formatting of solution and challange description.
    ```
    varnan generate
    ```
12. ### Push Writeup to Github
    Push the complete Workspace to Github.
13. ### Push Writeup README to Github
    Push Final README of CTF to Github.
