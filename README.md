# Lab 03: Git and GitHub
This repository documents my practice with local Git, GitHub, branches, and pull requests.

## README Responses

### 1.1 After initialization

```text
ls -la
total 0
drwxr-xr-x   4 wruzindana  staff  128 Sep  3 14:51 .
drwxr-xr-x   5 wruzindana  staff  160 Sep  3 10:40 ..
drwxr-xr-x  12 wruzindana  staff  384 Sep  3 15:54 .git
-rw-r--r--@  1 wruzindana  staff    0 Sep  3 14:51 README.md
text
1
1.2 First git status
text
123456
git statusOn branch mainChanges not staged for commit:  (use "git add <file>..." to update what will be committed)  (use "git restore <file>..." to discard changes in working directory)  mod
1.3 After the first commit
text
123
git statusOn branch mainnothing to commit, working tree clean
1.4 git log
text
123
git log --oneline9d172ba (HEAD -> main) Create alb READMEf2eaada Create lab README
1.5 git diff
text
12345678
git statusOn branch mainChanges not staged for commit:  (use "git add <file>..." to update what will be committed)  (use "git restore <file>..." to discard changes in working directory)  modified:   README.mdno changes added to commit (use "git add" and/or "git commit -a")
text
1234567891011121314151617181920212223
git diffdiff --git a/README.md b/README.mdindex 29dc1c4..f3e125b 100644--- a/README.md+++ b/README.md@@ -1,4 +1,5 @@-+# Lab 03: Git and GitHub+This repository documents my practice with local Git, GitHub, branches, and pull requests.  ## README Responses @@ -11,11 +12,3 @@ drwxr-xr-x   4 wruzindana  staff  128 Sep  3 14:51 . drwxr-xr-x   5 wruzindana  staff  160 Sep  3 10:40 .. drwxr-xr-x  12 wruzindana  staff  384 Sep  3 15:54 .git -rw-r--r--@  1 wruzindana  staff    0 Sep  3 14:51 README.md-git status-On branch main-Changes not staged for commit:-  (use "git add <file>..." to update what will be committed)-  (use "git restore <file>..." to discard changes in working directory)-       modified:   README.md-
How does this git status differ from the one in 1.2?
In 1.2, the file was untracked or newly created. In 1.5, Git recognizes it as a modified tracked file because we already committed it once.
1.6 Git command reflections
git init: Creates a new Git repository in the current directory.
git status: Shows which files are modified, staged, or untracked.
git add: Moves changes from working directory to staging area.
git commit: Saves staged changes to repository history with a message.
git log: Displays the commit history of the repository.
git diff: Shows line-by-line differences between commits or working tree.
1.7 Repository link
https://github.com/rirawill-tech/lab03-exercises
1.8 Comparing approaches
Nested-loop approach: Compares every element with every other element using two loops. If any pair matches, returns true. Time complexity is O(n²), space is O(1).
Set-based approach: Uses a hash set to track seen elements. For each element, checks if it's already in the set. Time complexity is O(n), space is O(n).
Trade-off: Set-based is faster for large lists but uses more memory. Nested loops use less memory but are slower.
1.9 Pull request merge options
Create a merge commit: Combines both branches keeping all individual commits and creates an extra merge commit.
Squash and merge: Combines all commits from the branch into a single commit on main, losing individual commit history.
Rebase and merge: Applies each commit from the branch onto main one by one, creating a linear history without a merge commit.
