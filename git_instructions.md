## 1. Set Up Credentials for Git

Configure your Git credentials by setting your username and email:

```bash
git config --global user.name "Your Username"
git config --global user.email "your.email@example.com"
```

## 2. Initialize a New Git Repository

Create a new directory for your project and initialize a Git repository:

```bash
mkdir myproject
cd myproject
git init
```

## 3. Stage File

After creating or modifying files in the repository folder. Stage the needed files before commiting

```bash
git add file_name.py

#or

git add .
```
## 4. Commit the changes

After staging files Create commit with the staged files and commit message

```bash
git commit - m "Enter you message here"
```

## 5. Create GitHub Repository and push code

Create GitHub Repository and push the code to repository

```bash
git remote add upstream https://github.com/ORIGINAL-OWNER/ORIGINAL-REPOSITORY.git
git branch -m main
git push -u origin main
```
