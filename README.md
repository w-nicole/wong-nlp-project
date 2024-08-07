# Added text pt. 2

Below is work done towards replicating the Wu & Dredze 2019 paper referenced later on in this text, which was done during a UROP under Dr. Yoon Kim investigating semisupervised methods of learning better (i.e. SOTA) POS accuracy leveraging techniques that spanned different languages.

Due to ease of usage and strict time constraints, to be able to complete the project with limited resources and guidance, it was necessary to use work from a previous iteration. Furthermore, that the replication numbers could be re-confirmed with past research records could not be done, due to time constraints and bandwidth constraints.

Every effort, however, was made to assure with reasonable confidence that this would reasonably replicate an acceptable reproduction of the Wu/Dredze numbers (note that after significant effort, the method to get the extremely exact numbers either on our end or theirs was lost, but the replication was deemed reasonable and safe, in the past UROP that this code is from).

# Added text

Relative to the commit ```fae1df0```, these are the changes made to Shijie Wu's repository.

Here is the original repository: https://github.com/shijie-wu/crosslingual-nlp

### A copy of the crosslingual-nlp repository, with the following general edits:

- Changes to minor hyperparameters to the corresponding paper at https://arxiv.org/abs/1904.09077l.
    - But NOT changes to other processing or details described in the paper that differ from the original code.
- A different environment was used, so the .yml was deleted.
- Simplified `example/surprising-mbert/evaluate.sh` script due to no need for non-POS evaluation.
- A few scripts and files added for convenience of analyzing and executing various runs (`run_multiple_check_variation.sh`, anything with `download` in its name in `src`, `src/scratchwork`)
- Change to `constant.py` to get labels to run with older UD.
- Changes to the way that types are represented in `util.py` to resolve compile errors/possible library inconsistencies.
- Of course, README changes.

Changes are not always marked in individual files, but the above was generated by going through the complete diff as of 3/28/22.

Commit hashes are in the private repository, but this is a non-run confirmed copy of a reasonable replication.

# License

Note that the LICENSE file corresponds to Shijie Wu's MIT License, in order to reproduce their original license. However, the codebase will be significantly altered, such that the license will not be strictly reflective of only Wu's original repoistory -- however, this repository can be considered to be under a general MIT license.

