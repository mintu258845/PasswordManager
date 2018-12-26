PROBLEM 
1. Create a Python module
2. Define a function that creates random passwords with a given length and complexity. See the function `generate_password` in the `reference.py` file.
3. Define a function that asserts that the complexity levels. 
4. Create a script that generates passwords (with multiple scenarios) and tests them using the assertion function you created in step 3. Them output the result (success or fail).
5. Define a function that retrieves a random user and persist the user into an SQLite database (full name and email). This SQLite database must be persistent (not in memory).
6. At last, create a script that retrieves 10 users using the function you created on the last step and for each one: create a new password using the password generator function with random length (between 6 and 12) and random complexity level; persist this password into the SQLite database associated with the correspondent user.

SOLUTION 
In generate_password()
  Initially assigned a few lowercase letter for all given complexity
  later added exactly one Uppercase, one digit and  one special characters based on requirement.
  Added only one of each because it is easy track the length and make sure all requirement is covered.

In check_password_level()
Here I am using nested if loops.
outermost loop checks for complexity 1 and assigns the complexity to 1,
complexity will be overridden if it matches higher complexity requirements.
I used this method because, complexity 4 should meet the requiremnt of complexity 3,2 and 1.
I found this as simple solution compared complex logical operator involved conditions.

In create_user()
I am reading the API through urllib.request(), other option was to use requests module.
request module need to downloaded, where as urllib.request() is a python inbuilt module.
After fetching the user name and email, loaded the user details with null password into sqlite3

'__main__'
Involves

1. Scripts for validating generate_password function.
  Sometimes the scripts print Fail messages, which is due to the complexity_level
  exception which is implemented in the check_password_level

2. Scripts for creating 10 users, updating random passwords and loading them into sqlite 
