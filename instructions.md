# Selenium

Selenium is a simple yet powerful tool used to create bots, web automation, & more using Python.

## 0. Project Setup

Download a text editor, such as VSCode or Sublime Text. (I prefer VSCode)

[Link to Download VSCode](https://code.visualstudio.com/download)

[Link to Download Sublime Text](https://www.sublimetext.com/)

In the VSCode Terminal/Command Prompt, setup the local project directory:

```sh
mkdir selenium
cd selenium
```

Head to [Github](https://github.com/) and create a new remote repository named `selenium`.

Following the creation of your new remote repository, create a new local repository on the command line:

```sh
echo "# selenium" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MylesThomas/selenium.git
git push -u origin main
```

Save this file as a markdown file `/selenium/instructions.md`, then open up a new VSCode instance and Open folder > `selenium`.

Next, setup a virtual Python environment:

```sh
cd selenium
py -m venv env
```

You should now see a folder 'env' with a python.exe program in the /Scripts directory.

Create a .gitignore file for the Python project and save it in the root directory `selenium`:

```sh
cd selenium
echo > .gitignore
```

Code for .gitignore: [Link to file](https://github.com/github/gitignore/blob/main/Python.gitignore)

Activate the virtual environment in the terminal, and update pip while you're at it:

```sh
where python
.\env\Scripts\activate

python.exe -m pip install --upgrade pip
pip list
```

Note: You can leave the virtual environment with this call:

```sh
deactivate
```

Install the necessary packages into your virtual environment:

```sh
pip install selenium
```

Create a requirements.txt file to ensure that you have the necessary dependencies to run this code:

```sh
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

Note:
- 1st line of code: Creates a requirements.txt file
- 2nd line of code: Download the necessary libraries again (Optional)

Create a main Python file, which we will be working from:

```sh
echo > main.py
```

Begin with the necessary imports:

```py
# main.py
import selenium
```

Ensure this runs by heading into the terminal with the virtual environment running:

```sh
python main.py
```

Note: In Sublime, you can run the code with the following command: Ctrl-B

Save these files and update git before beginning the project:

```sh
cd selenium

git status
git add .
git commit -m "Completed project setup"
git push -u origin main
git status
git log --oneline
q
```



---

### References

References:
- 