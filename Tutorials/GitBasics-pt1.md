# Git Basics

## What is Git and why should you use it?

Quite simply, git is distributed version control.  It allows files to be stored, organized,  versioned, and shared using a well-defined framework.  When used effectively, the system will free folders of messy and inconsistent version names and will provide context to all changes that have been made.  It has the most utility with flat files (essentially anything you could edit with a text editor), but can also be used with binary files such as powerpoint, word, excel, or pdf.  

Each git repository is a complete copy of all changes that have every been made to the code that is within the repository.  This means that when you copy a repository from github or from a friend, you have the complete history of the project at your fingertips without needing a network connection.  This may sound like it would take a substantial amount of space, but git uses snapshots to keep sizes small.

Git manages changes through what are called commits and branches.  The commits represent a state of the files that should be saved for future reference.  The branches represent different directions the work may take.  

As an example, if you are working on a project and are at a point where a small but tangible amount of work is completed, perhaps adding a new function, this could be commited.  This commit can then be referenced in the future and the clock can be turned back to this specific state if something is broken in the future.

A branch is used for developing new feature sets without inturrupting the main portion of the project.  This would be useful if part of the team is refactoring a set of functions to increase speed.  The team wouldn't want to break the functions for everyone else but needs their own place to work.  By using a branch they can perform all of their work and testing without impacting others.  Once completed with the refactoring the work can be "merged" back with the original branch to give everyone the benefits of the refactoring.  

Branches and commits can be selectively merged at any point.  This is a powerful concept that is central to git.  If a team member makes a commit that is useful in a different branch, it can be independently merged.  If it is determined that an old commit breaks part of the code base, that specific commit can be reversed without affecting any of the future commits.  

There are lots of other great features of git that we will cover in the future after committing and branching is more understood.  


Git is most useful if you already have an account with a remote repository.  We therefore begin our tutorial by recommending you visit one of the many web hosted git repos.  These include the following

### github.com
#### Pros: 
- Well known gold standard for open source repositories
- Many users with a strong community
- Flat fee of using a private repository

#### Cons:
- If you have something that you need to be private, github will charge you to make the repository private.
- Requires a new login account (can't use google, twitter, facebook, etc.)

#### Storage limits:
- Soft limit at 1GB.  Over 1GB they will politely send you a message asking you to reduce the size.

### bitbucket.com

#### Pros:

- Private repositories are free, just select private
- Arguably the second largest code repository location
- Can use login credentials from Twitter, Facebook, OpenID, or Google
- Inline commenting.  If you see a line of code that seems fishy, make a comment to find out more information.
	
#### Cons:

- Fewer users
- Privite repositories are chaged by the user and still maintain the same storage limits

#### Storage limits:

- Soft limit at 1GB.  Hard limit at 2GB that will prevent future push's to the repository

### Both services

Both bitbucket and github offer excellent web integrations that can make collaboration and review much easier.  Some of our favorite shared features include:

- Web-based edits:
	Review code online and make modifications and commit them through the website.  This can be very helpful if you are performing quick code reviews online or if you are working on markdown files.
	
- Commit notifications:
	Keeping current on work from a team becomes challenging as commits pile up.  Both services offer a robust number of features to notifiy you of new commits.  As your team becomes more clear with commit messages these can help quickly flag commits that warrent extra attention.

- Bug tracking:
	When bugs are found, both tools allow you to quickly mark them to make sure they are resolved in the future.  

## Conclusion:

Bitbucket is a better solution when you need a minimum number of private repositories to share between a team.  The integrated issue tracker and the inline comments allow for fast and flexible reviews.

## Endorsements and credits

Writen by: Dan Skorski

This introduction has been read and edited by:
Angela Waterworth
