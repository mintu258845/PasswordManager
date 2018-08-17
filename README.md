# Introduction
Welcome to the technical test. Thank you for your interest in being part of our team. This will be divided into 2 parts:

1. A recorded video from you talking about your experience
2. A practical Python test

# About you
We want to know more about you. So we created some questions and we would like you to record yourself answering those questions and send us back either the video file or video URL. For recording, we recommend this website: https://webcamera.io/. With it, you will be able to record yourself and save the video into a file. This will video file should be sent together with your code (described in the sections below). Instead of sending us the video file you can also upload it into Google Drive (preferred) or YouTube and just send us the URL. We **will not**, ever, publish or share your video with anyone. This will only be seen by the technical reviewer assigned to your application.

If you *refuse* to record yourself but still want to participate in our process you may only record an audio of you answering the questions below. For audio recording, you may find a lot of options on the web. You can send us the audio file via Google Drive as well by providing the URL.

**If you opt to upload your video or audio file into Google Drive (instead of sharing the raw file), just add the public URL into your `solution.md` (details below). Do not share it with any Nexus Edge email.**

## Questions
The questions we would like you to answer while recording yourself are (please answer in the same order):

1. Briefly describe your experience with Software development
2. What is your experience specifically with Python version 3?
3. Do you have any experience with async programming in Python?
4. Do you have any experience with threads or multiprocessing in Python?
5. What is your familiarity with DevOps tools? Have you had the chance to know or work with any of them?
6. What is your experience with REST APIs (integration, development, testing etc)? Do you know any frameworks?
7. How do you debug and test your code? Which tools or strategies do you use?
8. Do you think you have other pertinent skills relevant to this position?
9. What is your experience with remote teams?

After recording yourself and downloading the video file, please, watch it and ensure everything is ok. We will declassify you if the video is inaudible or corrupted.

# Python Test
This essential Python test is designed to assess your familiarity with the basic concepts of Python, how organized you are and your overall coding skills. You will be evaluated based on this criterions:

1. Formatting: basically PEP8
2. Structure: how modular is your code and do you organize it
3. Familiarity: how much you know standard libraries and syntax

## Getting started
Before you start working on the code:

1. Log in into your Bitbucket account or create a new one
2. Fork this repository into a **private repository** (to protect your privacy) [How to fork](https://confluence.atlassian.com/bitbucket/forking-a-repository-221449527.html)
3. Clone your forked version of this repository [How to clone](https://confluence.atlassian.com/bitbucket/clone-a-repository-223217891.html)
4. Be sure that you are using Python version >= 3.6

## Challenge
In the `reference.py` file you will find references about the functions you will need to create, don't forget to take a look at it. **Do not use it into your final code nor change the file** (you may copy & paste its contents into your script, and create other functions if necessary), this file should be read-only.
If you use any third-party library you must provide a requirements.txt file.

1. Create a Python module
2. Define a function that creates random passwords with a given length and complexity. See the function `generate_password` in the `reference.py` file.
3. Define a function that asserts that the complexity levels. See the function `check_password_level` in the `reference.py` file.
4. Create a script that generates passwords (with multiple scenarios) and tests them using the assertion function you created in step 3. Them output the result (success or fail).
5. Define a function that retrieves a random user and persist the user into an SQLite database (full name and email). This SQLite database must be persistent (not in memory). See the function `create_user` in the `reference.py` file.
6. At last, create a script that retrieves 10 users using the function you created on the last step and for each one: create a new password using the password generator function with random length (between 6 and 12) and random complexity level; persist this password into the SQLite database associated with the correspondent user.

## Wrapping up
1. Create a Markdown file called "solution" explaining your solution and why did you code it the way you coded.
2. Commit your changes. [How to commit](https://confluence.atlassian.com/get-started-with-bitbucket/push-code-to-bitbucket-861185309.html)
3. Don't forget to add either your video file or URL (in YouTube or Google Drive)!
4. Push your changes. [How to push](https://confluence.atlassian.com/get-started-with-bitbucket/push-code-to-bitbucket-861185309.html)
5. **If you completed all tasks**: at your repository's page: go to _Settings_, then _User and group access_ and add a new user `marcellus777` with _read_ permission. **Do this step only if you are done**.

**Do not give me access to your repository if you are not done.**

Thank you and good luck!