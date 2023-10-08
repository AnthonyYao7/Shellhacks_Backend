import os
import pickle
import configparser
from typing import Any

import shellhacks_algorithm


config = configparser.ConfigParser()
config.read(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "config.cfg"
))

caching_directory = config["DEFAULT"]["caching_directory"]

absolute_caching_directory = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    caching_directory
)


baselines = {
    "Baseball",
    "Basketball",
    "Boxing",
    "Football",
    "Golf Side View",
    "Golf Back View",
    "Running",
    "Push-ups",
    "Snatch",
    "Squat",
    "Clean and Jerk"
}


class VideoProcessor:

    """
    This function processes a video with caching
    """
    @staticmethod
    def process_video(filename: str, compression: int = 1) -> tuple[dict[tuple[tuple[str, str], tuple[str, str]], list[Any]], list[Any]]:
        if filename in baselines:
            print("OWEIFJIOWJFJWFIJ", filename)
            with open(
                os.path.join(
                    absolute_caching_directory,
                    filename + ".pickle"), 'rb') as f:

                obj = pickle.load(f)
                return obj, []

        old_filename = filename
        filename = filename.split('/')[-1]

        res = shellhacks_algorithm.process_video(old_filename, compression)

        with open(
            os.path.join(
                absolute_caching_directory,
                filename + ".pickle"), "wb") as f:
            pickle.dump(res[0], f)

        return res


def process_files(baseline: str, evaluee: str, compression: int = 4) -> tuple[dict[str, float], list]:
    a, _ = VideoProcessor.process_video(baseline, compression)
    b, ret = VideoProcessor.process_video(evaluee, compression)

    return shellhacks_algorithm.evaluate_sequence(a, b), ret

