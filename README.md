# obp-extract-cit
Wrapper to extract citations from XML editions of OBP books.

## How to run this tool
### Setup
This wrapper requires `saxonb-xslt` to be installed on your system. On Debian (or Debian-based distributions) this package can be installed via

`apt-get install libsaxonb-java`

To perform the setup, run:

`bash setup`

The setup contains the necessary instruction to initialise the submodule.

### Run
To run the process, place a copy of the **XML edition of the book** and the **DOI deposit** in the _obp-gen-xml_ folder. Finally, run:

`bash run`

### Clean-up

`bash clean [-y]`

would remove temporary files (untracked files and folders stored in the _obp-gen-xml_ folder). The script asks for the user's confirmation before removing the files, but if you are running this as part of a script you might want to use the`-y` flag to bypass the confirmation. 

## DEV
The way the _run_ script picks up files to process is not very precise (currently, via wildcards/asterisks). We might want to improve this in the future; solutions include (a) defining naming conventions for input files across all our scripts and (b) make bash to accept filenames as input arguments.
