"""Play videos in a slide show manner."""

import argparse
import logging
import os
import subprocess
import sys
import time

import vlc

# pylint: disable=invalid-name, too-few-public-methods, line-too-long

logger = logging.getLogger(__name__)


class Movie():
    """Container class for movie information"""
    def __init__(self, path, length, time_played):
        self.path = path
        self.length = length
        self.time_played = time_played

def _parse_movie_infos(directory, start_time):
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
            logger.info("Length: %s ms, %s minutes", length, length // 1000 // 60)
            movies[file_path] = Movie(file_path, length, start_time * 1000)
    return movies


def main():
    """Entry point for our simple vlc player
    """
    parser = argparse.ArgumentParser(description="Loop through movies in a directory")
    parser.add_argument('directory', type=str, help="The directory containing the movie files.")
    parser.add_argument('--loop_time', type=int, default=180,
                        help="Time in seconds that each movie is shown for at a time.")
    parser.add_argument('--start_time', type=int, default=0,
                        help="Set from when to resume playing in seconds.")
    options = parser.parse_args()

    movies = _parse_movie_infos(options.directory, options.start_time)
    while True:
        movie = None
        previous_process = None
        for movie in list(movies.values()):
            loop_time = options.loop_time
            loop_time_ms = loop_time * 1000  # play time in VLC is in milliseconds

            if movie.time_played >= movie.length:
                logger.info("Finished '%s'.", movie.path)
                del movies[movie.path]
                continue
            elif movie.time_played + loop_time_ms > movie.length:
                logger.info("Less than loop time left. Playing the remainder.")
                loop_time_ms = movie.length - movie.time_played
                loop_time = loop_time_ms // 1000

            args = ["python3", "play_single_movie.py", movie.path, "--set_time", str(movie.time_played)]
            # Start the next movie before terminating the current one to make the
            # transition less jarring.
            logger.info("Starting '%s'.", movie.path)
            process = subprocess.Popen(args, stdout=sys.stdout, stderr=subprocess.STDOUT)
            time.sleep(2)
            if previous_process:
                logger.info("Stopping previous movie.")
                previous_process.terminate()
            previous_process = process
            logger.info("Letting '%s' run for %s second(s)", movie.path, loop_time)
            time.sleep(options.loop_time)
            movie.time_played += loop_time_ms

        if movie:
            elapsed_time = movie.time_played // 1000
            logger.info("Elapsed time: %s second(s), %s minute(s)", elapsed_time, elapsed_time // 60)

        if not movies:
            break
    logger.info("Done")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
