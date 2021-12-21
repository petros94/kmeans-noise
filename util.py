import numpy as np
from pandas import DataFrame


def add_gaussian_noise(df, std):
    noise_df = df.copy()
    noise_df.x += np.random.normal(scale=std, size=len(noise_df))
    noise_df.y += np.random.normal(scale=std, size=len(noise_df))
    return noise_df


def add_uniform_noise_samples(df, n_samples, min_x, max_x, min_y, max_y):
    noise_df = df.copy()
    new_samples = {
        'x': np.random.uniform(min_x, max_x, n_samples),
        'y': np.random.uniform(min_y, max_y, n_samples),
        'label': -1,
        'noise_samples': n_samples
    }
    return noise_df.append(DataFrame(new_samples)).reset_index(drop=True)
