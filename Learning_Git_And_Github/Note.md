# Learning Git and Github
> Git is the **tool**, GitHub is the **service** for projects that use Git
- [Explainshell.com](https://explainshell.com/explain?cmd=ls+-la)


- initializing
`git init`
- adding
`git add .`
- committing
`git commit -m ""`
- status
`git status`
- withdraw aaa.html from **untracking area**
`git checkout aaa.html`
- withdraw bbb.html from **staging area**
`git reset HEAD bbb.html`
`Get things from staging area and put it in working directory`
- Deleting files also need added to stage and commit
`git rm file.html`
`rm file.html` + `git add file.html`
- each commit can be take out using its hash track code
- add all untrack in staging area
`git add .`
`git add -all`
- check log 
`git log`
- pull commit out to your workingdirectory
`git checkout hashCode.log`
- branch
`git branch`
`git branch -a`
`git checkout master`
`git branch newBranchName CommitHashCode`
- git checkout is quite flexible command