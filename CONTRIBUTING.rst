Filing Bugs or Feature Requests
-------------------------------

Please **always** create an issue when you encounter any bugs, problems or
need a new feature. Emails and private messages are not meant to communicate
such things!

Use the appropriate template and file a new issue here:
https://git.ecap.work/tgal/hesspix/issues

You can browse all the issues here: https://git.ecap.work/tgal/hesspix/issues

Please follow the instructions in the templates to provide all the
necessary information which will help other people to understand the
situation.

Improve
-------

Check out our KanBan board https://git.ecap.work/tgal/hesspix/boards,
which shows all the open issues in three columns:

- *discussion*: The issues which are yet to be discussed (e.g. not clear how to proceed)
- *todo*: Issues tagged with this label are ready to be tackled
- *doing*: These issues are currently "work in progress". They can however be
  put tossed back to *todo* column at any time if the development is suspended.

Here is the recommended workflow if you want to improve this project. This is a
standard procedure for collaborative software development, nothing exotic!

Feel free to contribute ;)

Make a Fork
~~~~~~~~~~~

You create a fork (your full own copy of the
repository), change the code and when you are happy with the changes, you create
a merge request, so we can review, discuss and add your contribution.
Merge requests are automatically tested on our GitLab CI server and you
don't have to do anything special.

Go to https://git.ecap.work/tgal/hesspix and click on "Fork".

After that, you will have a full copy of the code with write access under an URL
like this: ``https://git.km3net.de/YOUR_USERNAME/hesspix``

Clone your Fork to your PC
~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a local copy to work on (use the SSH address `git@git...`, not the HTTP one)::

    git clone git@git.km3net.de:YOUR_USERNAME/hesspix

Now you need to add a reference to the original repository, so you can sync your
own fork with the original repository::

    cd hesspix
    git remote add upstream https://git.ecap.work/tgal/hesspix


Keep your Fork Up to Date
~~~~~~~~~~~~~~~~~~~~~~~~~

To get the most recent commits (including all branches), run::

    git fetch upstream

This will download all the missing commits and branches which are now accessible
using the ``upstream/...`` prefix::

    $ git fetch upstream
    From hesspix
     * [new branch]        gitlab_jenkins_ci_test -> upstream/gitlab_jenkins_ci_test
     * [new branch]        legacy                 -> upstream/legacy
     * [new branch]        master                 -> upstream/master


If you want to update for example your **own** ``master`` branch
to contain all the changes on the official ``master`` branch of the original repository,
switch to it first with::

    git checkout master

and then merge the ``upstream/master`` into it::

    git merge upstream/master

Make sure to regularly ``git fetch upstream`` and merge changes to your own branches.

Push your changes to Gitlab regularly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure to keep your fork up to date on the GitLab server by pushing
all your commits regularly using::

    git push


Install in Developer Mode
~~~~~~~~~~~~~~~~~~~~~~~~~

This project can be installed in ``dev-mode``, which means, it links itself to
your site-packages and you can edit the sources and test them without the need
to reinstall it all the time. Although you will need to restart any
``python``, ``ipython`` or ``jupyter``-notebook (only the kernel!) if you
imported this python package before you made the changes.

Go to your own fork folder (as described above) and check out the branch you
want to work on::

    git checkout master  # the main development branch (should always be stable)
    make install-dev


Running the Test Suite
~~~~~~~~~~~~~~~~~~~~~~

Make sure to run the test suite first to see if everything is working
correctly::

    $ make test

This should give you a green bar!

Run the tests every time you make changes to see if you broke anything! It usually
takes just a few seconds and ensures that you don't break existing code. It's
also an easy way to spot syntax errors ;)

You can also start a script which will watch for file changes and retrigger
a test suite run every time for you. It's a nice practice to have a terminal
open running this script to check your test results continuously::

    make test-loop

Time to Code
~~~~~~~~~~~~

We develop new features and fix bugs on separate branches and merge them
back to ``master`` when they are stable. Merge requests (see below) are also
pointing towards this branch.

If you are working on your own fork, you can stay on your own ``master`` branch
and create merge requests from that.

Code Style
~~~~~~~~~~

Make sure to run ``black`` over the code, which ensures that the code style
matches the one we love and respect. We have a tool which makes it easy::

    make black

Create a Merge Request (aka Pull Request)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to https://git.ecap.work/tgal/hesspix/merge_requests/new and select your
source branch, which contains the changes you want to be added to this project
and select the ``master`` branch as target branch.

That's it, the merge will be accepted if everything is OK ;)

If you want to join the dev-team, let us know! Once you are a member of the
project, you can work on branches in this repository, without the need to
use your own fork :)
