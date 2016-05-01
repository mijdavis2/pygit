# pygit
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/439a70b92c114241a7c118020cb229e7)](https://www.codacy.com/app/mdavis/PyGit?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mijdavis2/PyGit&amp;utm_campaign=Badge_Grade)

Easy to use git utility for python.

Just instantiate a pygit object with ```git = PyGit("/path/to/repo/")``` and use git as you would normally.

Returns stdout from git as a list.

Modify to suite your needs.

## Usage

```python
>>> from pygit import PyGit
>>> git = PyGit("/path/to/repo/")
>>> git("checkout master")
[ "Switched to branch 'master'", "Your branch is up-to-date with 'origin/master'."]

>>> git("describe --tags")
['1.4.0-rev23']

>>> git("tag --contains ex4m9le*c00m1t*h4Sh")
['1.4.0-rev23', 'MY-SECOND-TAG-rev1']
```

## License

MIT © [mijdavis2](http://mdavisinsc.com)