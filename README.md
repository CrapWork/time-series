CrapWork's Mystery Fitbit Data Analysis

To open online version of repository:

https://mybinder.org/v2/gh/CrapWork/time-series/7136b96d220e303a270de9cb9e306a9fe5cadc63

    *No requirements are needed to use this link*

---

Included in this repository are:
    
    Conda Environment List
        environment.yml

    Jupyter Notebook, detailing the data analysis process
        analysis.ipynb

    Python Modules, .py files containing the functions that are used in the Notebook
        Acquire
        Explore
    
    Data Dictionary,
        data_dictionary.md

    Directory of raw csvs, (will be created if does not exist)
        /fitbit
            2018-04-26_through_2018-05-26.csv  2018-06-27_through_2018-07-27.csv  2018-08-27_through_2018-09-26.csv  2018-10-28_through-2018-11-27.csv
            2018-05-27_through_2018-06-26.csv  2018-07-28_through_2018-08-26.csv  2018-09-27_through_2018-10-27.csv  2018-11-28_through_2018-12-28.csv

    Dataset, (will be created if does not exist)
        data.csv
    
    Predictions,
        prediction_data.csv

    Presentation, 
        https://docs.google.com/presentation/d/1RxO_sOnriGU-3vKv1hp_h_nWzhkg7CJQyvwmUSX9MM0/edit?usp=sharing

---    

Requirements:
    Python 3 or higher,

    Jupyter Notebook

    Notebook must be executed in same directory as repository

    Explicit package requirements are found in environment.yml. The default Anaconda environment has all the 
    necessary packages.

---

A summarization of the data.

- There was a clear change in trends after July 1st. 
- Trends adhered to a new mean on most columns, and with less variance
- Future predictions were decided to use only the post-change data

