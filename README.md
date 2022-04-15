# Vrnan

A ctf-writeup tool

## Features

1. ### Initilaize CTF Workspace <br>
    Initialize Standard Workspace
    ```
    vrnan init
    ```
    Initialize Customized Workspace according to the CTF
    ```
    vrnan init --ctf CTF_LINK --creds USERNAME:PASSWORD
    ```
2. ### Link CTF
    Update the workspace according to the linked CTF Challanges and fetch realtime stats of CTF
    ```
    vrnan link --ctf CTF_LINK --creds USERNAME:PASSWORD
    ```
3. ### List Catagories
    List all the present CTF Catagories in the workspace
    ```
    vrnan list catagory
    ```
4. ### List Tasks (Solved / unsolved)
    List all the present CTF Tasks in the workspace
    ```
    vrnan list task
    ```
5. ### Add Catagory
    Add CTF Catagory in the workspace
    ```
    vrnan add catagory CATAGORY_NAME
    ```
6. ### Add Task
    Add CTF Task in the workspace
    ```
    vrnan add task --name TASK_NAME --desc DESCRIPTION --points POINTS --author AUTHOR --attatchments ATTATCHMENT_LINK
    ```
7. ### Generate complete CTF README
    Parse over all catagories and task to generate a final README file for whole CTF with proper formatting of solution and challange description.
8. ### Push Writeup to Github
    Push the complete Workspace to Github.
9. ### Push Writeup README to Github
    Push Final README of CTF to Github.