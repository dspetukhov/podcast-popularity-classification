The aim of this project is to predict whether an episode of the **[Super Data Science podcast](https://www.superdatascience.com)** will be popular or not, considering it as a binary classification problem.

Popularity is measured by the number of listens on SoundCloud. The podcast episode is considered popular (target label is one) if the number of listens of the episode is more than the third quartile of all episodes in the quarter, otherwise target label is zero. More details about labeling can be found in [01_exploratory_data_analysis.ipynb](01_exploratory_data_analysis.ipynb).

There are two stages in this project. First one is the data collection for the modelling:

- [crawling.py](crawling.py) - collecting information about each episode at `https://www.superdatascience.com/` using `selenium`.

- [downloading.py](downloading.py) - downloading each episode as mp3 file using `youtube-dl` and `ffmpeg` libraries.

The second stage is the data analysis, preprocessing, and modelling to identify the most popular podcast episodes using the spectrograms of audio signal:

- [01_exploratory_data_analysis.ipynb](01_exploratory_data_analysis.ipynb) - analyzing the number of listenings and labeling episodes by quarters.

- [02_augmentations.ipynb](02_augmentations.ipynb) - exploring basic augmentation techniques for audio data to implement them in [utils/augmentations.py](utils/augmentations.py).

- [03_preprocessing_spectrogram.ipynb](03_preprocessing_spectrogram.ipynb) - example of audio signal transformation using `Spectrogram` method.

- [04_modelling_spectrogram.ipynb](04_modelling_spectrogram.ipynb) - modelling with audio data transformed by `Spectrogram` as images and raw audio signal preprocessed in `Dataset` class with augmentation.

- [05_preprocessing_melspectrogram.ipynb](05_preprocessing_melspectrogram.ipynb) - example of audio signal transformation using `MelSpectrogram` method.

- [06_modelling_melspectrogram.ipynb](06_modelling_melspectrogram.ipynb) - modelling with audio data transformed by `MelSpectrogram` as images and raw audio signal preprocessed in `Dataset` class with augmentation.

- [07_preprocessing_mfcc.ipynb](07_preprocessing_mfcc.ipynb) - example of audio signal transformation using `MFCC` method.

- [08_modelling_mfcc.ipynb](08_modelling_mfcc.ipynb) - modelling with audio data transformed by `MFCC` as images and raw audio signal preprocessed in `Dataset` class with augmentation.

- [09_preprocessing_lfcc.ipynb](09_preprocessing_lfcc.ipynb) - example of audio signal transformation using `LFCC` method.

- [10_modelling_lfcc.ipynb](10_modelling_lfcc.ipynb) - modelling with audio data transformed by `LFCC` as images and raw audio signal preprocessed in `Dataset` class with augmentation.


