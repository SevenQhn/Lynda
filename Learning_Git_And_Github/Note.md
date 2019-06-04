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
- Creater branch from specific commit point
`git branch newBranchName CommitHashCode`
`git brawnch newBranchName defaultIsCurrentBranch`
- Create branch from where your pwd are and switch to that branh right now
`git checkout -b NewBranchName `
- git checkout is quite flexible command
- merge current branch into current branch
`git checkout master`+`git merge branchName`
- change your branch name
`git branch -m oldName newName`
- delete a branch
`git branch -D branchName1 branchName2 branchName3`
- Colone a git repository but only have access to master branch (other branches are hidden)
`pwd`
`cd positionYouWantYourColoneFileIn`
`git colone Url`
`gitignore`
`README`
`package.json`
---
`git branch -a` see the hidden branches
---
< Recommend course Ray Villalobos-Angular.js>
- Coloning individual branches
`pwd`
`cd positionYouWantYourColoneFileIn`
`git colone Url`
`git branch -a`
`git checkout -b branch`
----
`git colone -b BranchName Url`
- Coloning all branches
`pwd`
`cd positionYouWantYourColoneFileIn`
`git clone --mirror Url .git`
> then no actual fiels show in working directory
`git config --bool core.bare false`
> above command will turn a bare repo folder into a real one
`git reset --hard`
- HARD HEAD VS SOFT 
- Use exist branch as your template
`rm -dfr .git`