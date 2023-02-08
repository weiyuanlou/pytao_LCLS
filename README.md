# pytao_LCLS
This repository has...

$\rightarrow$ Instructions to setup and run basic Tao and Pytao commands  

---> Run Tao optimization and beam tracking using a simple Bmad lattice 

---> Run pytao on a LCLS2 lattice and apply bmad-live-model to interface with the LCLS2 machine 

---> Datamap example for data conversion between LCLS2 and bmad-live-model

---> Optics matching example for LCLS2

The user must know basic Python and bash commands.
All example notebooks are run on jupyter.

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

