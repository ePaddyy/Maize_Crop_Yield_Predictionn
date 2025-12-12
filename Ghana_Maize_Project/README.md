# Ghana Maize Yield Prediction

Predicting maize yield using Machine Learning, Satellite Weather Data, and Soil Analysis.

# Ghana Maize Project - Quick Run

Quick steps (safe, minimal actions):

1. Open notebooks/pipeline.ipynb.
2. Run the "IMPORTANT - run "Install libraries" cell 
   - Run ONLY Cell 1 to install packages. Do NOT run the rest of the notebook unless you intend to re-run the full pipeline.
3. After installation and restarting the kernel, run ONLY the MODEL TRAINING cell (Cell 12).
   - Model cell trains the ensemble and saves the model to `../models/maize_model.pkl`.
   - Precondition: the master dataset must exist at `../data/final/Ghana_Maize_Master_Dataset.csv`. If missing, run preprocessing/data-ingestion cells deliberately (they perform downloads and/or long processing).

Why this order:

<<<<<<< HEAD
- The install cell safely installs missing packages without executing data downloads or pipeline steps.
- Running only the model.ipynb in the notebook folder is the fastest way to train the model if you already have the processed master dataset.
=======
- Running only the MODEL TRAINING cell is the fastest way to train the model if you already have the processed master dataset.
>>>>>>> 4faa1992fcd106503dbad22805c69a683e7a6538

If you need to rebuild the dataset or regenerate reports, run the earlier notebook cells in order  but be aware of long API calls and processing time.

# Report
- Read the documentaion in the report folder to get the steps used to get the data
