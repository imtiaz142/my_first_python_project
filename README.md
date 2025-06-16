# My First Python Project

This is a beginner-level Python project with multiple files to practice using Git and GitHub.

✅ 1. Go to Desktop and create a project folder
cd ~/Desktop
mkdir my_first_python_project
cd my_first_python_project

✅ 2. Create Python files
touch main.py helper.py README.md

✅ 3. Initialize Git & make first commit

git init
git add .
git commit -m "Initial commit - basic Python project"

✅ 4. Create a GitHub repo (do this from the website manually):
Go to: https://github.com

Click New

Repo name: my_first_python_project

Leave README unchecked (you already have one)

Click Create repository

✅ 5.Connect your local folder to GitHub
git remote add origin https://github.com/YOUR_USERNAME/my_first_python_project.git
git branch -M main
git push -u origin main


🔁 Future Updates (whenever you change code)

git add .
git commit -m "Your update message"
git push

🧹 Optional: Create .gitignore file

touch .gitignore