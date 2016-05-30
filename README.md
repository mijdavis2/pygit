[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9f2c98df839545c385231b43fd1e7509)](https://www.codacy.com/app/mijdavis2/pygit?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mijdavis2/pygit&amp;utm_campaign=Badge_Grade)

# pygit

Easy to use git utility for python.

Just instantiate a pygit object with ```git = PyGit("/path/to/repo/")``` and use git as you would normally.

Returns stdout from git as a list.

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

## Install

```bash
pip install git+git://github.com/mijdavis2/pygit.git
```

## Require

In requirements.txt file:

```
git+git://github.com/mijdavis2/pygit.git@0.1.1#egg=pygit
```

## License

MIT © [mijdavis2](http://mdavisinsc.com)
