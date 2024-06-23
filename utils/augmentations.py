import random
from torchaudio import transforms as T
from torchaudio import functional as F
from torchaudio import sox_effects


def augment(waveform, sample_rate, clipping, clipping_length=5_000_000):
    """Basic audio augmentations."""
    if random.choice([True, False]):
        waveform = _time_shift(waveform)
    #
    if random.choice([True, False]):
        waveform = _speed_shift(waveform, sample_rate)
    #
    # print(waveform.shape)
    # if random.choice([True, False]):
    #     waveform = _pitch_shift(waveform, sample_rate)
    #
    if clipping:
        return _clipping(waveform, clipping_length)
    return waveform


def _time_shift(waveform):
    """Shift the waveform by a random value from 5 to 25%."""
    multiplier = random.choice([-1, 1])
    shift = random.randint(
        int(0.05 * waveform.shape[0]),
        int(0.25 * waveform.shape[0])
    )
    return waveform.roll(multiplier * shift)


def _speed_shift(waveform, sample_rate):
    """Change the playback speed according to documentation
    https://pytorch.org/audio/main/generated/torchaudio.transforms.Speed.html.
    """
    speed = T.Speed(
        orig_freq=sample_rate,
        factor=random.choice([0.9, 1.1])
    )
    _waveform, _ = speed(waveform)
    return _waveform


def _pitch_shift(waveform, sample_rate):
    """Shift the pitch of a waveform."""
    factor = random.randint(3, 7)
    return F.pitch_shift(
        waveform,
        sample_rate,
        n_steps=random.randint(1, 4),
        n_fft=sample_rate // (2**factor),
        hop_length=sample_rate // (4*2**factor)
    )


def _clipping(waveform, clipping_length):
    """Taking a random fixed length segment of the waveform."""
    offset = random.randint(0, waveform.shape[0] - clipping_length)
    return waveform[offset:(offset+clipping_length)]


def masking(spectrogram):
    """Add frequency or time masking or both."""
    fm = T.FrequencyMasking(freq_mask_param=(spectrogram.shape[0] // random.randint(10, 40)))
    for _ in range(random.randint(0, 5)):
        spectrogram = fm(spectrogram)
    #
    tm = T.TimeMasking(time_mask_param=(spectrogram.shape[1] // random.randint(10, 40)))
    for _ in range(random.randint(0, 5)):
        spectrogram = tm(spectrogram)
    #
    return spectrogram