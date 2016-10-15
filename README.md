### github follow bot

#### Setup

clone this repository
	$ git clone https://github.com/mussaimo/github-bot.git
	$ cd github-bot

create a python 2.7 environment
	$ virtualenv <replace_with_your_preffered_env_name>
	$ source <replace_with_your_preffered_env_name>/bin/activate

Install dependancies
	$ pip install -r requirements.txt

Download and unpack/etract geckodriver
make it executable.
move to /usr/bin
	$ chmod a+x geckodriver
	$ sudo mv geckodriver /usr/bin
	$ export PATH=$PATH:/usr/bin/geckodriver


You can find the latest geckodriver executable on the [GitHub release page.](https://github.com/mozilla/geckodriver/releases)


Replace all the required variables
	username.send_keys("your_user_name_goes_here")
	
	password.send_keys("your_password_goes_here")
	

Run file
	$ python follow_bot.py

