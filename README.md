# Varnan

> A CTF-writeup tool

## Features

1. ### Initilaize CTF Workspace <br>
    Initialize Standard Workspace
    ```
    varnan init
    ```
    Initialize Customized Workspace according to the CTF
    ```
    varnan init --ctf CTF_LINK --creds USERNAME:PASSWORD
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
    varnan category add category_NAME
    ```
6. ### List Tasks (Solved / unsolved)
    List all the present CTF Tasks in the workspace
    ```
    varnan task list
    ```
7. ### Add Task
    Add CTF Task in the workspace
    ```
    varnan task add --name TASK_NAME --desc DESCRIPTION --points POINTS --author AUTHOR --attatchments ATTATCHMENT_LINK
    ```
8. ### Solve Task
    Mark CTF Task as solved
    ```
    varnan task solve --category CATEGORY --name TASK_NAME --flag FLAG
    ```
9. ### Generate complete CTF README
    Parse over all catagories and task to generate a final README file for whole CTF with proper formatting of solution and challange description.
    ```
    varnan generate
    ```
10. ### Push Writeup to Github
    Push the complete Workspace to Github.
11. ### Push Writeup README to Github
    Push Final README of CTF to Github.