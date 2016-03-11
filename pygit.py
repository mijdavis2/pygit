"""
.. module:: pygit
   :platform: Unix, Windows
   :synopsis: Utility for using git naturally in python scripts.

.. moduleauthors:: mijdavis2

.. versionadd:: 1.0.0
"""
import subprocess


class InvalidRepoDirectory(Exception):
    pass


class PyGit(object):
    def __init__(self, repo_directory):
        """
        :param repo_directory: "/path/to/repo"
        :type repo_directory: str
        """
        self.repo_directory = repo_directory
        git_check = subprocess.check_output(['git', 'rev-parse', '--git-dir'], cwd=self.repo_directory).split("\n")[0]
        if git_check != '.git':
            raise InvalidRepoDirectory("Invalid git repo directory: '{}'.\n"
                                       "repo_directory must be a root repo directory "
                                       "of git project.".format(self.repo_directory))

    def git(self, arg_string):
        """
        Makes using git in python nearly seamless.

        .. example::

            git = PyGit("/path/to/repo").git
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

        :param arg_string: Arguments you'd normally pass in as arguments to git
        :type arg_string: str
        :returns: The stdout of the requested git command split by '\n' in the form of a list
        """
        arguments = ["git"] + arg_string.split(" ")
        return subprocess.check_output(arguments, cwd=self.repo_directory).split("\n")
