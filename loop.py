"""Play videos in a slide show manner."""

import argparse
import logging
import os
import subprocess
import sys
import time

import vlc

# pylint: disable=invalid-name, too-few-public-methods

logger = logging.getLogger(__name__)


class Movie():
    """Container class for movie information"""
    def __init__(self, path, length):
        self.path = path
        self.length = length
        self.time_played = 0

def _parse_movie_infos(directory):
    """Parse all necessary information about the movies in the given directory."""
    instance = vlc.Instance()
    movies = {}
    for root, _, files in os.walk(directory):
        for f in files:
            logger.info("Parsing '%s'", os.path.join(root, f))
            file_path = os.path.join(root, f)
            media = instance.media_new(file_path)
            media.parse()
            length = media.get_duration()
            movies[f] = Movie(file_path, length)
    return movies


def main():
    """Entry point for our simple vlc player
    """
    parser = argparse.ArgumentParser(description="Loop through movies in a directory")
    parser.add_argument('directory', type=str, help="The directory containing the movie files.")
    parser.add_argument('--loop_time', type=int, default=180,
                        help="Time in seconds that each movie is shown for at a time.")
    options = parser.parse_args()

    movies = _parse_movie_infos(options.directory)
    while True:
        for movie in movies.values():
            args = ["python3", "start_app.py", movie.path, "--set_time", str(movie.time_played)]
            process = subprocess.Popen(args, stdout=sys.stdout, stderr=subprocess.STDOUT)
            logger.info("Letting '%s' run for %s second(s)", movie.path, options.loop_time)
            time.sleep(options.loop_time)
            process.terminate()
            movie.time_played += options.loop_time * 1000  # play time in VLC is in ms
            logger.info("Done")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
