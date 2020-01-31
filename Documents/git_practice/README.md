## Unix Commands
- `mkdir <dir name>` : make a new directory called `dir name`
- `ls` : list all files/directories in the current directory
    - `-a`: all (including hidden .files/directories)
- `touch <file name>` : create a new file called `file name`
- `cd <dir name>` : change directory to `dir name`
- `clear` : clear your screen
- `cat <file name>` : display the content of `file name`

## Git Commands
### Local (Machine)
- `git init` : initialiaze the current dir as git repository
    - creates `.git/`
- `git status` : displays the current status of git repository
- `git add <file name>` : add `file name` to the staging(index) area
- `git commit -m` `<message>` : commit the current change in the staging(index) area.
- `git log` : log all commits history.

### Remote (Github)
- `git remote add <origin>` <https://github.com/user_name/repository.git>
	- Set the remote repository as origin with URL.
- `git push` -u `<origin> <master>`
	- Push the local git repositry to remote master branch (github).








