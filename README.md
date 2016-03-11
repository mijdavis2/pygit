# PyGit
Easy to use git utility for python.

Just instantiate a pygit object with ```git = PyGit("/path/to/repo/").git``` and use git as you would normally.

Returns a list.

Modify to suite your needs.

## Usage

```python
>>> git = PyGit("/path/to/repo/").git

>>> git("checkout master")
[ "Switched to branch 'master'", "Your branch is up-to-date with 'origin/master'."]

>>> git("describe --tags")
['1.4.0-rev23']

>>> git("tag --contains ex4m9le*c00m1t*h4Sh")
['1.4.0-rev23', 'MY-SECOND-TAG-rev1']
