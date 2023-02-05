# pytao_LCLS
This repository includes jupyter notebooks which show how to..

(1) Set up and apply pytao on a simple Bmad lattice  
(2) Run pytao on a LCLS2 lattice
(3) Use Bmad live-model to interface LCLS2 machine  


To Setup, open a clean bash terminal:

(A) Install `conda` from 

https://conda.io/projects/conda/en/latest/user-guide/install/index.html

After installation, type `conda env list`, which should show that you are in the "base" (deafult) environment.

(B) Create a new conda environment by typing: 

'conda env create -f environment.yml'

This step can take time to install pytao, bmad, and other packages.

The new environment is called 'lcls-live'. 

(C) Activate the environment by typing 'source activate lcls-live'

To check that this has worked, type `conda env list`.

(D) Install a new kernel to use Jupyter notebooks by typing:
'python -m ipykernel install --user --name lcls-live --display-name Lcls-live'

(E) Open jupyter lab by typing 'jupyter lab'.

This will open a browser tab which runs jupyter. 

Now you can open and run the example notebooks using the lcls-live kernel!
( Additional instructions are included for each notebook. )

Only step (C) and (E) need to be repeated for future runs.

