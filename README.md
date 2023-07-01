# MoveRCCar API using FastAPI for ChatGPT4

This project demonstrates how to create a simple MoveRCCar API using FastAPI, allowing you to control an RC car using text commands from ChatGPT4.

The API was mainly written by using chatGPT itself

## Prerequisites

- Python 3.7 or higher
- FastAPI framework
- PySerial library (for controlling the RC car)

## Installation
NOTE: These steps assume the use of Windows CLI or Git CLI on Windows
1. Open the CLI and locate in the appropriate directory for work on this project
1. Create a directory called "RC_car_api"
1. Move to that directory
1. Create a virtual environment for the example
   ```shell
   python -m venv chatgpt_rccar_api_venv
   ```
1. Activate the environment, using one of the following commands
   ```shell
   source chatgpt_rccar_api_venv/bin/activate  # for Unix/Linux
   chatgpt_rccar_api_venv\Scripts\activate  # for Windows
   source chatgpt_rccar_api_venv/Scripts/activate # for git CLI on windows
   ```
1. Clone the repository within "RC_car_api" directory with the following command:
   ```shell
   git clone https://github.com/Karosuo/chatgpt_rccar_api.git
   ```
1. Install the requirements
   ```shell
   pip install -r chatgpt_rccar_api/requirements.txt # Remember the correct use of forward/backward slashes when using widnows CLI or git CLI
   ```
1. Move into the cloned directory
1. Run the server by using the following command:
   ```shell
   uvicorn main:app --reload
   ```

## Examples
In order to make the car move, we can request it directly, or make it a bit more interesting, like
"Your goal is to get to the apple, which is 2 blocks ahead an 1 to the right, move the car accordingly to make it to the apple"
