from typing import Dict, Tuple

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import mediapipe as mp

from ..data_curation.pose_estimation import LIMB_PAIRS, LIMB_PAIRS_DESCRIPTIONS


angle_net = dict[tuple[tuple[str, str], tuple[str, str]], list[float]]


def evaluate_single_joint(name: tuple[tuple[str, str], tuple[str, str]], baseline: list[float], to_evaluate: list[float]) -> float:
    desired_length = len(baseline)

    common_time = np.linspace(0, 1, desired_length)

    to_evaluate_interpolator = interp1d(np.arange(len(to_evaluate)) / (len(to_evaluate) - 1), to_evaluate)

    interpolated_to_evaluate = to_evaluate_interpolator(common_time)

    correlation = (1 + np.corrcoef(baseline, interpolated_to_evaluate)[0, 1]) / 2.

    plt.plot(np.arange(len(baseline)), baseline)
    plt.plot(np.arange(len(interpolated_to_evaluate)), interpolated_to_evaluate)
    plt.title(LIMB_PAIRS_DESCRIPTIONS[LIMB_PAIRS.index(name)])
    plt.savefig(LIMB_PAIRS_DESCRIPTIONS[LIMB_PAIRS.index(name)], bbox_inches='tight')
    plt.figure()

    return correlation


def evaluate_sequence(baseline: angle_net, to_evaluate: angle_net) -> dict[str, float]:
    scores = {}

    print(to_evaluate)
    print(baseline)

    for key, value in baseline.items():
        scores[LIMB_PAIRS_DESCRIPTIONS[LIMB_PAIRS.index(key)]] = evaluate_single_joint(key, value, to_evaluate[key])

    return scores
