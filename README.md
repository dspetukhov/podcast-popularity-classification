The aim of this project is to predict whether an episode of the [Super Data Science podcast](https://www.superdatascience.com) will be popular. This problem is considered as a binary classification problem and based on the number of listens on SoundCloud.

There are two stages in this project. First one is the data collection for the modelling:

- [crawling.py](crawling.py) - collecting information about each episode at `https://www.superdatascience.com/` using `selenium`.

- [downloading.py](downloading.py) - function for downloading podcast episode as mp3 file using `youtube-dl` and `ffmpeg` libraries.

The second stage is the data analysis, preprocessing, and modelling to identify the most popular podcast episodes based on the spectrograms of audio signal:

- [01_exploratory_data_analysis.ipynb](01_exploratory_data_analysis.ipynb) - 

- [02_augmentations.ipynb](02_augmentations.ipynb) - 

- [03_preprocessing_spectrogram.ipynb](03_preprocessing_spectrogram.ipynb) - 

- [04_modelling_spectrogram.ipynb](04_modelling_spectrogram.ipynb) - 

- [05_preprocessing_melspectrogram.ipynb](05_preprocessing_melspectrogram.ipynb) - 

- [06_modelling_melspectrogram.ipynb](06_modelling_melspectrogram.ipynb) - 

- [07_preprocessing_mfcc.ipynb](07_preprocessing_mfcc.ipynb) - 

- [08_modelling_mfcc.ipynb](08_modelling_mfcc.ipynb) - 

- [09_preprocessing_lfcc.ipynb](09_preprocessing_lfcc.ipynb) - 

- [10_modelling_lfcc.ipynb](10_modelling_lfcc.ipynb) - 


