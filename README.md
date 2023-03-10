# pytao_LCLS
This repository has...

$\rightarrow$ Instructions to setup and run basic Tao and Pytao commands.

$\rightarrow$ Basic Tao optimization and beam tracking examples using a simple Bmad lattice.

$\rightarrow$ Example to run pytao on a LCLS2 lattice.

$\rightarrow$ Example of bmad-live-model which interfaces with the LCLS2 machine via datamaps.

$\rightarrow$ Optics compensation example for LCLS2.

====================================================

The user must know basic Python and bash commands.

All example notebooks are run on jupyter with a kernel called `lcls-live`.

To setup, clone this repository first, then:

(A) Install `conda` from 

https://conda.io/projects/conda/en/latest/user-guide/install/index.html

(B) Open a new terminal. Then create a new conda environment by typing: 

`conda env create -f environment.yml`

This step can take time to install pytao, bmad, and other packages.

The new environment is called "lcls-live". 

(C) Activate the environment by typing `source activate lcls-live`.

To check that this has worked, type `conda env list`.

(D) Install a new kernel to use Jupyter notebooks by typing:
`python -m ipykernel install --user --name lcls-live --display-name Lcls-live`

(E) Open jupyter lab by typing `jupyter lab`.

This will open a browser tab which runs jupyter. 

Now you can open and run the example notebooks using the lcls-live kernel!
( Additional instructions are included for each notebook. )

Only step (C) and (E) need to be repeated for future runs.

