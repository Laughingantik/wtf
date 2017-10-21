# Contributing

Instructions for contributing to War Torn Faith.

## issue tracker

We use our [GitHub issue tracker](https://github.com/mrpudn/wtf/issues) for tracking bugs, new features, enhancements, and discussions. If you discover a bug or would like to participate in the development of this project, please use our issue tracker.

## kanban board

We have a special GitHub project set up as our [Kanban Board](https://github.com/mrpudn/wtf/projects/1). It shows the status of all in-flight tasks that we're working on. There are three columns: **Backlog**, **In Progress**, and **Done**. **Backlog** contains tasks that we plan to start working on in the near future. New items are regularly added to **Backlog** after they have been groomed and prioritized and as bandwidth becomes available. **In Progress** contains tasks that we are currently working on. **Done** contains finished tasks. Old items in the **Done** column are regularly cleared out in order to avoid clutter.

## pull requests

Pull requests to this repo are more than welcome!

We ask that you participate in the [issue tracker](#issue-tracker) so that you can collect feedback on what you're wishing to contribute and whether it aligns with the project's vision and roadmap. Doing so will improve the odds of your contribution being accepted.

We ask that you include a meaningful description in your pull request, tag any issues that are closed by or related to the pull request, and squash your commits for clarity and legibility. Logistically challenging pull requests may be rejected.

## architecture

This project has a simple architecture: a **relational database**, sitting behind a **RESTful API**, which is consumed by a **web application**.

The **RESTful API** is the only component that performs direct operations (`SELECT`, `CREATE`, `INSERT`, `UPDATE`, and `DELETE` queries) against the **relational database**. Clients (chiefly the **web application**) connect to the **RESTful API** using HTTP (`GET`, `POST`, `PUT`, `PATCH`, and `DELETE` methods) in order to indirectly manipulate the data in the **relational database** and carry out the business logic of the application. Additional layers of authentication, authorization, security, validation, caching, etc. that are beyond the scope of the **relational database** are built into the **RESTful API**.

Separating this functionality within the **RESTful API** component, instead of intermingling it with the **web application** has a few important benefits, including:
  1. *reusability* - thanks to the ubiquity of the HTTP protocol, the **RESTful API** can be reused by a wide variety of clients, including Android apps, iPhone apps, third party systems, etc. Additionally, the internal workings of the **RESTful API** and the components behind it (i.e. the **relational database**) can be changed with minimal or no impact to the clients using the **RESTful API** (ex. swapping the database from one vendor to another or completely rewriting the **RESTful API** in a different programming language) - so long as the request/response contracts remain the same, these details are of no concern to clients
  2. *scalability* - the **RESTful API** component can scale independently of the **web application**. In the future, each resource in the **RESTful API** could be split into it's own microservice and scaled independently from the rest of the microservices for potentially greater scalability.
  3. *deployment* - the **RESTful API** can be deployed independently of the **web application** and the **relational database**

For more information about this architectural pattern, please see:
  - [Wikipedia: Representational state transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)

## directory structure

```
.
├── CONTRIBUTING.md   # contributing documentation
│
├── Pipfile           # project environment requirements
├── Pipfile.lock      # project environment details
│
├── README.md         # high-level project documentation
│
├── api               # RESTful API
│   ├── accounts      #   accounts resource
│   ├── characters    #   characters resource
│   ├── fights        #   fights resource
│   └── run.py        #   script to start the API Flask web server
│
├── app               # web app
│   ├── static        #   static assets
│   ├── templates     #   Jinja2 templates
│   ├── views         #   Flask view routes
│   └── run.py        #   script to start the web app Flask web server
│
├── db                # database
│   └── migrations    #   schema/data migration scripts
│
└── run.py            # script to start both the RESTful API and the web app
                      #   mounted in the same Flask web server
```

## environment setup

It should go without saying that you will need [git](https://git-scm.com/) and a [GitHub](https://github.com/) account in order to checkout and make contributions to this project's codebase. If these tools are new to you or you're uncomfortable using them, please refer to our [git and github primer](#git-and-github-primer).

This project requires [Python 3.6](https://www.python.org/) and [pipenv](https://github.com/kennethreitz/pipenv).

We use pipenv to install and manage this project's dependencies and environment. The `Pipfile` and `Pipfile.lock` files are both used by pipenv to define and freeze the project's package and environment dependencies.

To install the project's dependencies (including dev dependencies):
```bash
$ pipenv install --dev
```

For more help with pipenv:
```bash
$ pipenv --help
```

## developing

To run only the API:
```bash
$ FLASK_APP=api/run.py pipenv run flask run
```

To run only the web app:
```bash
$ FLASK_APP=app/run.py pipenv run flask run
```

## continuous integration

...

## git and github primer

Git is the most important tool in your developer arsenal. It will enable you to work swiftly and collaborate seamlessly with others. Mastery of this tool is essential for a productive, frictionless development experience.

This primer should hopefully be enough to get you started, but we recommend spending some time in deeper study of the tool. The free, online book, [Pro Git](https://git-scm.com/book), is a great choice!

### installation

We'll assume that you've already installed git and have created a GitHub account.

### git config

The first thing you'll want to do is set up your git `user.name` and `user.email`, which is how you'll identify yourself to others:
```bash
# set you user.name and user.email globally
# (be sure to use your GitHub username and email)
$ git config --global user.name "<username>"
$ git config --global user.email "<email>"
```

You can verify these configurations like so:
```bash
# print your user.name and user.email
$ git config --global user.name
$ git config --global user.email
```

### forking

Now we're ready to clone this project, but before we do, let's explain forking.

This project follows the "Fork and Pull Request" workflow, which is the standard workflow for open-source projects. Contributors make changes to a *fork* (basically a copy) of the main repository (called the "*upstream*" repository) and propose those changes to the upstream repository in the form of a *Pull Request* (abbreviated as *PR*). The PR is reviewed by the project's maintainers and either accepted or rejected. This is the frictionless and safe way that projects are able to incorporate contributions from well intentioned strangers while keeping their users protected from malicious or otherwise harmful code.

You can read more about this workflow here: [Atlassian: Git Workflows and Tutorials - Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows#forking-workflow)

In order to make contributions to this repo, you too will need a fork.

This repository (the "upstream" repository, remember) is located here: [mrpudn/wtf](https://github.com/mrpudn/wtf). Simply click the "Fork" button at the top right of the page in order to create your own fork of this project under your username. You're free to modify this fork to your hearts content.

### cloning

You can clone any repo with the following command:
```bash
# (replacing <repo-url> with the repo's url, of course)
$ git clone <repo-url>
```

This will clone the repo down from it's remote location to your computer in your current directory. What you end up cloning is a full git repository that looks just like the one at the remote location (i.e. it will have a `.git` directory with a ton of stuff in it).

Just to clarify: when we say "remote location", for this project that usually means somewhere on GitHub, but it could be anywhere there's a git server or even just a `.git` directory. We'll talk more about this later.

Go ahead and clone your fork down to your computer and `cd` into it:
```bash
$ git clone <fork-url>
$ cd wtf
```

### remotes

Remember when we said "remote location"? Git has this concept of *remotes*, which are just paths to git repositories that you might want to pull changes from or push changes to.

Let's take a look at our current remotes:
```bash
$ git remote -v
```

You'll see a single remote called "origin" that points to your fork. Traditionally, we set up at least two remotes: *origin* which points to your fork, and *upstream* which points to the main/upstream repository.

Let's set up the *upstream* remote:
```bash
$ git remote add upstream http://github.com/mrpudn/wtf.git
$ git remote -v
```

Now we'll be able to push our local changes to the *origin* remote (our fork) and pull in new changes made to the upstream repository from our *upstream* remote to keep up-to-date.

You can think of remotes as "aliases". You don't have to think of the URL or path that points to a repository (or type it out every time, for that matter), just associate it with a quick keyword, like *origin*, *upstream*, *john*, or *jane*.

### branches

Branches allow you to multitask and keep your changes separate from the volatility of the main (or `master`) branch that's changing all the time. It's good practice to always develop your changes on their own branches, and we highly recommend that you do.

You can list all of your local branches like so:
```bash
$ git branch -a
```

You should be on the `master` branch.

To create a new branch, execute the following command:
```bash
$ git checkout -b my-branch
$ git branch -a
```

This will create a new branch, called `my-branch`, and switch your active branch to it. You're now free to develop and make changes to this branch, independently of `master`.

It's important to note that we've branched off of `master` in this case, since we were on the `master` branch before checking out our new branch, `my-branch`. That means your new branch will have all of the same commits that you had in `master` at the time. Had we been on a different branch, the new branch would have all of the commits from that branch instead.

When you're ready to commit your changes, first check the status of your branch:
```bash
$ git status
```

Next, you'll want to add these changes to git's "staging area":
```bash
# (imagine we've modified the CONTRIBUTING.md document)
$ git add CONTRIBUTING.md
$ git status
```

You can also add all changes made to all files, like so:
```bash
$ git add --all
```

Changes in the staging area are the only ones that will be committed when we issue our commit command. This is useful if you have changes that are not ready yet and do not wish to commit them with the others.

You can now commit these changes to your `my-branch` branch and provide a quick message about the changes, like so:
```bash
$ git commit -m "Added branches section to CONTRIBUTING.md document"
```

Finally, we can push our changes up to our fork:
```bash
$ git push origin my-branch
```

If you'd like to switch to another branch, simply check it out:
```bash
$ git checkout master
```

### syncing with `upstream/master`

To get your local's `master` branch synced up with the latest changes in the `upstream` repo, make sure you have your `master` branch checked out, and then pull the `master` branch of your `upstream` repo:
```bash
$ git checkout master
$ git pull upstream master
```

Now, you can push these changes up to your fork, to keep it in sync as well:
```bash
$ git push origin master
```

You can sync your branches up with these new changes, too:
```bash
$ git checkout my-branch
$ git rebase master
$ git push -f origin my-branch
```

The `git rebase master` command will add all of the commits that your `my-branch` branch does not already have from master, and then play all of the changes you've made to `my-branch` on top of those changes. The newly updated `master` branch will effectively become the new "base" for your `my-branch` branch, instead of the old `master` that you originally branched off of.

Note that if you've changed a file that has also been changed by the incoming changes from the `upstream` repo's `master` branch, then you may experience a merge conflict if it's not clear to git how they should be merged together. In this case, you'll have to resolve the conflict before it can complete the rebase. Run a `git status`, and it will help guide you through this process - as a general rule: when in doubt, run `git status`.

Notice that we've added the `-f` (force) flag to our `git push` command. When you perform a rebase, you effectively rewrite your commit history, which will confuse your remote repos. You have to use a force push to force your remote to accept the new commit history.

### rebasing

Rebasing is an intermediate concept, so don't worry if you don't get the hang of it immediately. If you can at least rebase your branches with new changes coming in from the `upstream` repo's `master` branch, that'll get you pretty far.

Interactive rebasing is a very powerful feature of git, but it can get you in trouble if you're not careful. Interactive rebasing allows you to perform several handy operations: re-word commit messages, edit a commit, drop a commit, or even "squash" two or more commits into a single commit. It's a great way to prepare your changes to be more easily reviewed by others, and is a step most commonly performed prior to issuing a Pull Request (PR).

When initiating an interactive rebase, you need to tell git how far back in your commit history you want to go back to. You can give it a commit hash explicitly or compute it in a variety of ways. Here are a few common examples:
```bash
# rebase all commits since commit a350e2:
$ git rebase -i a350e2
# rebase the last 1 commit:
$ git rebase -i HEAD~1
# rebase the last 3 commits:
$ git rebase -i HEAD~3
# rebase all commits since master and my-branch diverged:
# (this one is particularly useful)
$ git rebase -i $(git merge-base master my-branch)
```

You will be presented with a list of commits and a menu of commands that you can execute against each commit. Each commit will have the `pick` command, by default. To switch the command, simply delete `pick` and replace it with one of the other commands (or their one-letter shortcut).

Note that you'll be editing the rebase menu in `vi`. If you're not familiar with `vi`, here are a few quick tips to get by:
  - Enter "insert" mode by pressing `i`
    - (You can edit the text in this mode)
  - Enter "command" mode by pressing the `ESC` key
    - (You can issue commands in this mode)
  - You should be able to navigate with your directional keys
  - "Write" and "Quit" from "command" mode by typing `:wq` and pressing the `ENTER` key

You can also change the editor to something other than `vi`, but that's beyond this primer. Google is your friend :)

When you're done rebasing, you can issue a force push to update your remote:
```bash
git push -f origin my-branch
```

Try experimenting with smaller rebases until you get the hang of it, then you can tackle more complicated rebasing.

### pull requests

When you're ready to have your changes merged into the `upstream` repository, you'll need to create a Pull Request (PR). To create one, go to your fork in GitHub, select your branch, and click the "New pull request" button.

Make sure you add a good description to your pull request to help reviewers understand your changes. Be sure to note any open issues that are related to your PR are resolved by your PR. If changes are requested to your PR, you can simply make changes to your branch and push them to your fork, and they will be incorporated into the PR.

After your PR has been accepted, you can sync your `master` branch with the `upstream` repo.

To delete your branch after you're completely done with it:
```bash
$ git branch -D my-branch
```

To delete the branch from your fork:
```bash
$ git push --delete origin my-branch
```

Now, you can repeat the whole process for your next contribution :)

### ssh keys

You'll probably want to set up SSH keys with GitHub so that you don't have to authenticate every time you have to interact with GitHub from the command line. This isn't essential when you're first starting out, but constantly authenticating yourself will start to get annoying, so be sure to come back and complete these steps: [Connecting to GitHub with SSH](https://help.github.com/articles/connecting-to-github-with-ssh/).

### useful git commands

Sync your local and *origin* `master` branches with the latest changes from the *upstream* `master` branch:
```bash
$ git checkout master && git pull upstream master && git push origin master
```

Pop the last commit back into the commit staging area, as if you haven't committed it yet:
```bash
$ git reset --soft HEAD~1
```

Wipe out changes in your local repository:
```bash
$ git reset --hard HEAD && git clean -f
```

Perform an interactive rebase of all changes you've made after branching off of master:
```bash
$ git rebase -i $(git merge-base master <branch>)
```

Delete and create a pristine `master` branch:
```bash
# (make sure you aren't on master)
# quick way to get off of master:
$ git checkout master && git checkout -b temp
# recreate master
$ git branch -D master && git checkout -b master upstream/master
```

Fetch all of your remotes (become aware of any changes made to them), and prune out any branches that have been deleted in your remotes:
```bash
$ git fetch --all --prune
```
