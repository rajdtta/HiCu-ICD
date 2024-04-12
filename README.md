# CS598 Project: HiCu-ICD

This repository is a modified version of the [original HiCu-ICD repository](https://github.com/wren93/HiCu-ICD) for the
purposes of our course project. The original repository contains code for the
paper [HiCu: Leveraging Hierarchy for Curriculum Learning in Automated ICD Coding](https://arxiv.org/abs/2208.02301).

Our modified code adds support for the latest packages and libraries, as well as reduces
the number of models to be trained for the purposes of our project.

1. Clone the repository to a local directory

2. Once you have gained access to the [MIMIC-III v1.4 dataset](https://physionet.org/content/mimiciii/1.4/) (see link for requirements),
   download the required files and move them into a `/data` folder within the root of the repository. Use the following directory structure:

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

3. Install the required packages using the following command:

    ```bash
    # Python v3.11.7 is recommended
    pip install -r requirements.txt
    ```

4. Run the pre-processing script to generate the necessary sampled data files. The `--ratio` flag can be used to specify
   the ratio of the dataset to be used. For example, to use 5% of the dataset, run the following command:

    ```bash
    python preprocess_mimic3.py --ratio 0.05
    ```

5. Use the training scripts in the `./runs` directory to train each of the models. For example, to train the base
   MultiResCNN model, run the following command:

    ```bash
    ./runs/run_multirescnn.sh
    ```

   The evaluation metrics will be saved in the `./models` directory in a timestamped folder.