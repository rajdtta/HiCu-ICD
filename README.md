# CS598 Project: HiCu-ICD

This repository is a modified version of the [original HiCu-ICD repository](https://github.com/wren93/HiCu-ICD) for the
purposes of our course project. The original repository contains code for the
paper [HiCu: Leveraging Hierarchy for Curriculum Learning in Automated ICD Coding](https://arxiv.org/abs/2208.02301).

Our modified code adds support for the latest packages and libraries, as well as reduces
the number of models to be trained for the purposes of our project.

You can access the CoLab notebook for the project
using [the following link](https://colab.research.google.com/drive/1Qvs9qVqJqd3foCv2zEM-S8XpE1oOX01b?usp=sharing).

Instructions
-----

1. Download the repository and extract the files into a local directory.

2. Once you have been given access to the [MIMIC-III v1.4 dataset](https://physionet.org/content/mimiciii/1.4/),
   download the dataset and extract the files into a `/data` folder within the root of the repository. Update the
   directory structure as follows:

   ```
    HiCu-ICD/ (root)
    |
    ... (other files in the repository)
    └── data/
    |   |   D_ICD_DIAGNOSES.csv
    |   |   D_ICD_PROCEDURES.csv
    |   └───mimic3/
    |   |   |   NOTEEVENTS.csv
    |   |   |   DIAGNOSES_ICD.csv
    |   |   |   PROCEDURES_ICD.csv
    |   |   |   train_full_hadm_ids.csv
    |   |   |   train_50_hadm_ids.csv
    |   |   |   dev_full_hadm_ids.csv
    |   |   |   dev_50_hadm_ids.csv
    |   |   |   test_full_hadm_ids.csv
    |   |   |   test_50_hadm_ids.csv
    ```

   The `*_hadm_ids.csv` files can be
   found [here](https://github.com/jamesmullenbach/caml-mimic/tree/master/mimicdata/mimic3).

3. Create a folder named `HiCu-ICD` in the root folder of your Google Drive. Copy the contents of the repository into
   this folder.

    1. When running the CoLab notebook, make sure that you connect the same Google Drive account that contains
       the `HiCu-ICD` folder.

4. Run the notebook to train the models and/or view the results (from the already trained models).

    1. If using the CoLab environment, make sure to use a GPU runtime (e.g. T4 or a NVIDIA GPU).