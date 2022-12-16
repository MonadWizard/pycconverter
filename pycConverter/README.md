
## can be imported by

from pycconverter import PycConverter

### or

import pycconverter

## Convert all .py files to .pyc files

#### param Source_path: Path to the source directory
#### param Destination_path: Path to the destination directory where the .pyc files will be stored
#### param DirectoryNamePyc: Name of the directory where the .pyc files will be stored
:return: None

:Example:

```
>>> from pycconverter import PycConverter

>>> PycConverter(Source_path="/home/user/ProjectsDirectory", Destination_path="/home/user/Projects/PycC", DirectoryNamePyc="BUILD").convert_to_pyc()

```
