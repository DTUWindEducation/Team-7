1	What is the difference between git and GitLab?
	⁃	Git is a version control system while, GitLab is a platform that uses Git and adds tools for collaboration and DevOps.
	2	What is the difference between GitLab, GitHub, and BitBucket?
	⁃	GitLab is a comprehensive DevOps platform, GitHub is more popular for open-source projects and BitBucket integrates well with Atlassian tools.
	3	Why would I ever want to use git, but not GitLab?
	⁃	if you only need version control and don't require the additional features because Git is lightweight and can be used locally or with other platforms like GitHub or BitBucket.
	4	What are the steps to update the GitLab server with some changes I made on my computer?
	⁃	Stage Your Changes: git add .
	⁃	Commit Your Changes: git commit -m "Describe your changes"
	⁃	Push to GitLab: git push origin <your-branch-name>
	5	What is a branch and why would I use one?
	⁃	A branch in Git is a separate line of development. It allows you to work on different features or fixes independently from the main codebase. You might use it to keep your work separate from the main project until it's ready or, so multiple developers can work on different branches without conflicts, or even, to test new ideas without affecting the stable code.
	6	How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
	⁃	Commit 4 (branch2), Commit 3 (branch1), Commit 2, Commit 1
	⁃	Commit 1: Initial commit.
	⁃	Commit 2: Second commit.
	⁃	Commit 3: Third commit on branch1.
	⁃	Commit 4: Commit on branch2, which branches off after Commit 2.
	7	Give an example of a set of git commands that would result in a merge conflict.
	⁃	Here's an example of a set of Git commands that could result in a merge conflict:
	⁃	Initialize a Repository: git init
	⁃	Create a File and Commit: echo "Line 1" > file.txt, git add file.txt, git commit -m "Initial commit"
	⁃	Create and Switch to a New Branch: git checkout -b branch1
	⁃	Make Changes in branch1 and Commit: echo "Line 2 from branch1" >> file.txt, git add file.txt, git commit -m "Add line in branch1"
	⁃	Switch Back to main Branch: git checkout main
	⁃	Create and Switch to Another Branch: git checkout -b branch2
	⁃	Make Different Changes in branch2 and Commit: echo "Line 2 from branch2" >> file.txt, git add file.txt, git commit -m "Add line in branch2"
	⁃	Merge branch1 into main: git checkout main, git merge branch1
	⁃	Attempt to Merge branch2 into main: git merge branch2
	8	Is Git suitable for latex documents?
	⁃	Yes, Git is suitable for LaTeX documents.
	9	Should I from now on version my word and powerpoint slides using git? Why/why not?
	⁃	If you frequently collaborate on slides or need to maintain a detailed history of changes, using Git can be helpful. However, for simpler projects or if you find managing binary files cumbersome, you might prefer other version control methods like cloud storage with version history.
	10	What could happen when I push my latest commit to the remote repository without pulling first?
	⁃	Several issues could arise:
	⁃	Rejection: Git will reject your push if there are changes on the remote that you don't have locally. You'll see an error message indicating that you need to pull first.
	⁃	Merge Conflicts: If there are changes on the remote that conflict with your local changes, you'll need to resolve these conflicts after pulling.
	⁃	Out-of-Sync History: Your local repository's history will be out of sync with the remote, which can cause confusion and make
	11	What happens when I pull without commiting my local changes first?
	⁃	Git will attempt to merge the remote changes with your local changes. Automatic merge, merge conflicts, stashing changes.
	12	What is the difference between branching and forking?
	⁃	Branching and forking are both ways to create separate lines of development in Git, but they serve different purposes. Branching creates a new branch within the same repository to work on features, fixes, or experiments, used for short-term development and collaboration within the same project. Forking creates a personal copy of someone else's repository, allowing you to make changes without affecting the original project which is commonly used for contributing to open-source projects or when you want to develop independently.
