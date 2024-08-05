# Preparing Satori with Anaconda

The location of all of your code and where all experiments should go is: `/nobackup/users/KERB`. It is reachable via `cd ~; cd /nobackup/users/KERB`.

Install Anaconda 2022 in your main folder.

Now, your `source ~/.bashrc` currently contains the following (only thing changed is the name of the environment):

```
# 4/28/23: https://huggingface.co/docs/datasets/cache
# no modifications except to path name
export HF_DATASETS_CACHE="/nobackup/users/wongn/huggingface_cache"
# end cite

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/nobackup/users/wongn/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/nobackup/users/wongn/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/nobackup/users/wongn/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/nobackup/users/wongn/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

cd /nobackup/users/wongn
conda init bash
conda activate wong-nlp-ox
```

This means you also need to run `mkdir /nobackup/users/wongn/huggingface_cache`. Note that the lower-level (2022) Anaconda is the one being accessed.

Notice the "conda init bash" and the "conda activate wong-nlp-ox".

# Running your first models

First, we're going to ensure that Satori is ready for running, especially due to past problems with installation of pytorch, confusion with pip and conda, etc.

When activating the environment, make sure that you are activating it within in the ```true root directory```, which in your case, confusingly, is the subdirectory with Anaconda 2022 installed. Only there, activate the following:

```source ~/.bashrc```

This is to get your environment setup properly, in a fast way. Now, the right environment is activated.

Then, you want to do the following:

11/17/23: https://mit-satori.github.io/satori-ai-frameworks.html
```
conda config --prepend channels \
https://opence.mit.edu
```
end cite

8/2/24: https://mit-satori.github.io/satori-ai-frameworks.html
```
conda config --prepend channels \
https://public.dhe.ibm.com/ibmdl/export/pub/software/server/ibm-ai/conda/
```
```
conda install pytorch
```
8/2/24: https://anaconda.org/conda-forge/transformers
```
conda install conda-forge::transformers
```
8/2/24: https://mit-satori.github.io/satori-ai-frameworks.html
```
export IBM_POWERAI_LICENSE_ACCEPT=yes
```

Then, do this:

Notice that this won't run until you run the following (make sure the conda is not initalized):

```conda create --name wong-nlp-ox```



