"""Play videos in a slide show manner."""

import argparse
import logging
import subprocess
import sys
import time

# pylint: disable=invalid-name

logger = logging.getLogger(__name__)


def main():
    """Entry point for our simple vlc player
    """
    parser = argparse.ArgumentParser(description="Loop through movies in a directory")
    parser.add_argument('directory', type=str, help="The directory containing the movie files.")
    parser.add_argument('--loop_time', type=int, default=180,
                        help="Time in seconds that each movie is shown for at a time.")
    options = parser.parse_args()

    args = ["python3", "start_app.py", "movies/movie.mp4", "--set_time", "600000"]
    process = subprocess.Popen(args, stdout=sys.stdout, stderr=subprocess.STDOUT)

    logger.info("Letting it run for %s second(s)", options.loop_time)
    time.sleep(options.loop_time)
    process.terminate()
    logger.info("Done")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
