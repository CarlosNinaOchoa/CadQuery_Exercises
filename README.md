# CadQuery Exercises

## Goal
This is a compilation of CadQuery exercises created with learning purposes only. This serves like a documentation of my progression in use of CadQuery tools.

## Benefit for others
I have been a hard user of CAD software for almost 20 years and a mechanical design engineer for industrial machines. So you could find this examples interesting for your learning process too.

## Start with CadQuery

### Install
> For a complete installation guide, please visit the [official documentation](https://cadquery.readthedocs.io/en/latest/index.html)


To install in Ubuntu (WSL2 in my case):

#### Install Miniforge (recommended)
    curl -L -o miniforge.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash miniforge.sh -b -p $HOME/miniforge

#### Activate Miniforge
    source $HOME/miniforge/bin/activate

#### Create a new enviroment and activate it
This code create an eviroment called "cq"

    conda create -n cq
    conda activate cq
#### Install with Mamba
Install the latest CADQuery version:

    mamba install cadquery

### Test installation
To test if all has gone just fine, open a Terminal and type:

    $ python
    >>> import cadquery
    >>> cadquery.Workplane('XY').box(1,2,3).toSvg()

If the results is a SVG output like this:

    '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<svg ...
    ... 
    \n</svg>\n'

You just installed CadQuery correctly. Congrats!

### Start a new session

To start a new session, you have to activate Miniforge again:

    source $HOME/miniforge/bin/activate

Then, activate your "cq" enviroment:

    conda activate cq

Finally - if your want - you can clone this repo and try this exercises freely.


