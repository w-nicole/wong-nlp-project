TODO: insert the stuff here pertaining to the env setup, how to set up on Satori, etc.

TODO: update this consistently with what is needed to do to set up, exactly once after each phase of setting up/installation etc.

Note you can just environment.yml at the end if needed -- but don't worry too much about the details.

Download the dataset: 

`wget https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-1827/ud-treebanks-v1.4.tgz?sequence=4&isAllowed=y`

Note that you want the .tgz for UD v1.4, to match the Wu & Dredze ('19) paper.

Then, extract the data:

`tar -xvzf ud-treebanks-v1.4.tgz\?sequence\=4`

Make the experiments folder

`mkdir /nobackup/users/wongn/nlp-ox/wong-nlp-project/experiments`

things that are were installed in trying to get the reproduction to work (i.e. initial_run.sh)

the call is chmod u+x ./initial_run.sh and to run, it's ./initial_run.sh (note this resolves weird things with the symlinking)

`conda pytorch-lightning conda install lightning -c conda-forge`

Above fails, so use:

`pip install pytorch-lightning==1.4.4 torchmetrics==0.5.0`

However, that results in another failure (Numpy requires GCC >= 8.4).

`gcc --version` (SO post)

gcc (GCC) 8.3. (Red Hat 8.3.1-5)

So this means the following 

