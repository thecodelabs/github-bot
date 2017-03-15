## Github follow bot

### Disclaimer

	* Depending on internet connection, script will run for morethan 36 hours.
	* It is considered spammy so use at your own risk

### Script setup

clone this repository

	$ git clone https://github.com/thecodelabs/github-bot.git
	$ cd github-bot

create a python 2.7 environment

	$ virtualenv <your_preffered_env_name>
	$ source <your_preffered_env_name>/bin/activate

Install dependancies

	$ pip install -r requirements.txt

Download and extract the latest geckodriver executable found [here](https://github.com/mozilla/geckodriver/releases)
make it executable.
move to /usr/bin

```bash
$ chmod a+x geckodriver
$ sudo mv geckodriver /usr/bin
$ export PATH=$PATH:/usr/bin/geckodriver
```

Replace all the required variables check [follow-bot.py](https://github.com/the codelabs/github-bot/blob/master/follow_bot.py)

```js
username.send_keys("your_user_name_goes_here")
password.send_keys("your_password_goes_here")
```

Run file
```bash
$ python follow_bot.py
```

### License
---
The MIT License (MIT)

Copyright (c)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
