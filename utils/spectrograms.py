from torchaudio import transforms as T


def get_spectrogram(waveform, sample_rate, spectrogram_type='spectrogram'):
    """Get spectrogram of specified type transformed to DB scale."""
    if spectrogram_type == 'spectrogram':
        spectrogram = _spectrogram(sample_rate)
    elif spectrogram_type == 'melspectrogram':
        spectrogram = _melspectrogram(sample_rate)
    elif spectrogram_type == 'mfcc':
        spectrogram = _mfcc(sample_rate)
    elif spectrogram_type == 'lfcc':
        spectrogram = _lfcc(sample_rate)
    a2db = T.AmplitudeToDB(top_db=80)
    return a2db(
        spectrogram(waveform)
    )


def _spectrogram(sample_rate):
    return T.Spectrogram(
        n_fft=sample_rate,
        hop_length=sample_rate // 2,
    )


def _melspectrogram(sample_rate):
    return T.MelSpectrogram(
        sample_rate=sample_rate,
        n_fft=sample_rate,
        hop_length=sample_rate // 2,
        n_mels=128
    )


def _mfcc(sample_rate):
    return T.MFCC(
        sample_rate=sample_rate, n_mfcc=40,
        melkwargs={
                'n_fft': sample_rate,
                'hop_length': sample_rate // 2,
                'n_mels': 128
            }
    )


def _lfcc(sample_rate):
    return T.LFCC(
        sample_rate=sample_rate, n_filter=128, n_lfcc=40,
        speckwargs={
                'n_fft': sample_rate,
                'hop_length': sample_rate // 2
            }
    )
