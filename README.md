# Hiring test

This repository contains a skeleton for a small REST API app, that you should build using Falcon (https://falcon.readthedocs.io/en/stable/). Please complete the following tasks, push your code to a new repository and send it to us by mail.

- There is one file in the repo called `run_test.py`. This is the file that you need to be able to run to finish the test. You can use this for testing your intermediate solutions.
- The REST app that you need to build needs to have a route `check`, that takes 3 parameters: `first_name` and `last_name` and `email`.
- The API should do the following
    1. Convert the `first_name`, `last_name` and `email` to all-lowercase, and return those.
    2. Make sure the email is of the form `<[a-z]+>@raymon.ai`, and return the value of this check.
    3. return the list of letters that are in both first name and last name (after converting to lowercase), in alphbetical order.

- The expected result is JSON. All this can be gathered from the assert statements in the `run_test.py` file.
- Please complete the `Dockerfile` and the `code/smallapp/api.py` files. I have indicated where your code should probably go. 
    - The `code/smallapp/api.py` needs to contain the code for the Falcon app. Feel free to add other files to structure your code if you feel the need to.
    - The Dockerfile needs to install the apps requirements, copy the code, install the python package `smallapp` and launch the api. I have already provided the launch command.
- Once you’ve done that, you should be able to run the app using `docker-compose build && docker-compose up`.
- Try to show best practices in your code and in the building of the docker container.

If you have any questions, do not hesitate to contact me. Good luck! 
    

