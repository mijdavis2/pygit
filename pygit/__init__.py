"""
.. module:: pygit
   :platform: Unix, Windows
   :synopsis: Utility for using git naturally in python scripts.

.. moduleauthors:: mijdavis2, pmaguire

.. versionadd:: 0.1.3
"""
import subprocess
import os


class InvalidRepoDirectory(Exception):
    pass


class PyGit(object):
    def __init__(self, repo_directory, new_repo=False):
        """
        :param repo_directory: "/path/to/repo"
        :type repo_directory: str
        :param new_repo: Set to true if you want PyGit to run a git init.
        """
        self.repo_directory = repo_directory
        if new_repo:
            self._git("init")
        if not os.path.isdir(self.repo_directory) or \
                not os.access(self.repo_directory, os.R_OK) or \
                not os.access(self.repo_directory, os.W_OK) or \
                not subprocess.check_output(['git', 'rev-parse', '--git-dir'],
                                            cwd=self.repo_directory).decode('ascii').split("\n")[0]:
            raise InvalidRepoDirectory("Invalid git repo directory: '{}'.\n"
                                       "repo_directory must be a root repo directory "
                                       "of git project and you must have r/w permissions.".format(self.repo_directory))

    def __call__(self, *args, **kwargs):
        return self._git(args[0])

    def _git(self, arg_string_or_list):
        """
        Makes using git in python nearly seamless.

        .. example::

            git = PyGit("/path/to/repo")
            git("status")

            [
                'On branch develop',
                'Your branch is up-to-date with "origin/develop".',
                'nothing to commit, working directory clean'
            ]

            git("tag")

            [
                '1.4.0-rev20',
                '1.4.0-rev21',
                '1.4.0-rev22',
                '1.4.0-rev23',
                ...
            ]

        :param arg_string_or_list: Arguments you'd normally pass in as arguments to git.  
        :type arg_string_or_list: str or list
        :returns: The stdout of the requested git command split by '\n' in the form of a list
        """
        if type(arg_string_or_list) is list:
            arguments = ["git"] + arg_string_or_list
        else:
            arguments = ["git"] + arg_string_or_list.split()

        return subprocess.check_output(arguments, cwd=self.repo_directory).decode('ascii').split("\n")

    def checkout_tag(self, tag_name):
        self._git('fetch -p')
        git_output = subprocess.check_output(["git", "ls-remote", "--tags"],
                                             cwd=self.repo_directory).decode('ascii').split()
        remote_tags = [x.replace('refs/tags/', '') for x in git_output if 'refs/tags/' in x]
        if tag_name not in remote_tags:
            raise Exception("No version tag exists in the current repo named: '{}'. ".format(tag_name))
        print ("Confirmed that version tag: {} exists in the repo. "
               "Checking out this version.".format(tag_name))
        self._git("checkout " + tag_name)
