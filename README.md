markdown
1234567891011121314
1.2 First git status
text
12345678
1.3 After the first commit
text
123
1.4 git log
text
123
1.5 git diff
text
12345678
text
1234567891011121314151617181920212223
How does this git status differ from the one in 1.2?
In 1.2, the file was untracked or newly created. In 1.5, Git recognizes it as a modified tracked file because we already committed it once.
1.6 Git command reflections
In one or two sentences each, what does each command do?
git init: Initializes a new Git repository in the current directory.
git status: Shows the state of the working directory and staging area.
git add: Stages changes to be included in the next commit.
git commit: Records staged changes to the repository history.
git log: Displays the commit history of the repository.
git diff: Shows unstaged changes between commits or the working tree.
1.7 Repository link
1.8 Comparing approaches
In your own words:
How does the nested-loop approach check for a duplicate?
How does the set-based approach check for a duplicate?
What is the runtime and memory trade-off of each?
1.9 Pull request merge options
In your own words, what does each GitHub merge option do?
Create a merge commit
Squash and merge
Rebase and merge
