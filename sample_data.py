import csv
import pandas as pd
from utils.options import args

original_file = '%s/NOTEEVENTS.csv' % args.MIMIC_3_DIR
sample_file = '%s/NOTEEVENTS_SAMPLED.csv' % args.MIMIC_3_DIR

ratio = args.ratio # defaukt: 0.1

# TODO - Sample ratio% (default 10%) of notes from NOTEEVENTS.csv and save to NOTEEVENTS_SAMPLED.csv