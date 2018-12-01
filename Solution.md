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
