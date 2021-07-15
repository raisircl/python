# python
python programs
1. Sum of 4 Digits of a  Number
2. Reverse of digits of 4 digit number
Git Setup
Microsoft Windows [Version 10.0.19043.1083]
(c) Microsoft Corporation. All rights reserved.

C:\Users\raive>git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone             Clone a repository into a new directory
   init              Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add               Add file contents to the index
   mv                Move or rename a file, a directory, or a symlink
   restore           Restore working tree files
   rm                Remove files from the working tree and from the index
   sparse-checkout   Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)
   bisect            Use binary search to find the commit that introduced a bug
   diff              Show changes between commits, commit and working tree, etc
   grep              Print lines matching a pattern
   log               Show commit logs
   show              Show various types of objects
   status            Show the working tree status

grow, mark and tweak your common history
   branch            List, create, or delete branches
   commit            Record changes to the repository
   merge             Join two or more development histories together
   rebase            Reapply commits on top of another base tip
   reset             Reset current HEAD to the specified state
   switch            Switch branches
   tag               Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch             Download objects and refs from another repository
   pull              Fetch from and integrate with another repository or a local branch
   push              Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

C:\Users\raive>d:

D:\>cd rai

D:\rai>cd code

D:\rai\code>cd pyth*

D:\rai\code\python>cd suraj

D:\rai\code\python\suraj>md git

D:\rai\code\python\suraj>dir
 Volume in drive D is New Volume
 Volume Serial Number is 8422-2065

 Directory of D:\rai\code\python\suraj

07/15/2021  06:38 AM    <DIR>          .
07/15/2021  06:38 AM    <DIR>          ..
07/15/2021  06:38 AM    <DIR>          git
07/15/2021  06:23 AM    <DIR>          programs
07/13/2021  06:57 AM           316,149 Python-day-1.pdf
07/14/2021  06:54 AM           202,553 Python-day-2.pdf
               2 File(s)        518,702 bytes
               4 Dir(s)  30,416,379,904 bytes free

D:\rai\code\python\suraj>cd git

D:\rai\code\python\suraj\git>git clone https://github.com/raisircl/python.git
Cloning into 'python'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.

D:\rai\code\python\suraj\git>dir
 Volume in drive D is New Volume
 Volume Serial Number is 8422-2065

 Directory of D:\rai\code\python\suraj\git

07/15/2021  06:42 AM    <DIR>          .
07/15/2021  06:42 AM    <DIR>          ..
07/15/2021  06:42 AM    <DIR>          python
               0 File(s)              0 bytes
               3 Dir(s)  30,416,322,560 bytes free

D:\rai\code\python\suraj\git>cd python

D:\rai\code\python\suraj\git\python>git checkout
Your branch is up to date with 'origin/master'.

D:\rai\code\python\suraj\git\python>git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        digitastotal.py
        reverseofnum.py
        sum.py

nothing added to commit but untracked files present (use "git add" to track)

D:\rai\code\python\suraj\git\python>git add  digitastotal.py reverseofnum.py sum.py

D:\rai\code\python\suraj\git\python>git commit -m " sum of digits , reverse  , sum of 2 nos "
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'raive@DESKTOP-HT3VRU3.(none)')

D:\rai\code\python\suraj\git\python>git config --global user.email "rai.verma@live.com"

D:\rai\code\python\suraj\git\python>git config --global user.name "raisircl"

D:\rai\code\python\suraj\git\python>git commit -m " sum of digits , reverse  , sum of 2 nos "
[master 8f96d1f]  sum of digits , reverse  , sum of 2 nos
 3 files changed, 28 insertions(+)
 create mode 100644 digitastotal.py
 create mode 100644 reverseofnum.py
 create mode 100644 sum.py

D:\rai\code\python\suraj\git\python>git push
Select an authentication method for 'https://github.com/':
  1. Web browser (default)
  2. Personal access token
option (enter for default):
info: please complete authentication in your browser...
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 654 bytes | 654.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/raisircl/python.git
   98f0760..8f96d1f  master -> master

D:\rai\code\python\suraj\git\python>git push
Everything up-to-date

D:\rai\code\python\suraj\git\python>
