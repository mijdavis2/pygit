import subprocess

class PyGit:
    def __init__(self, repo_directory):
        self.repo_directory = repo_directory

    def git(self, *args):
        arguments = ["git"] + [arg for arg in args]
        return subprocess.check_output(arguments, cwd=self.repo_directory).split("\n")
