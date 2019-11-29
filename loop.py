"""Play videos in a slide show manner."""

import logging
import subprocess
import sys
import time

# pylint: disable=invalid-name

logger = logging.getLogger(__name__)


def main():
    """Entry point for our simple vlc player
    """

    args = ["python3", "start_app.py", "movie.mp4", "--set_time", "600000"]
    process = subprocess.Popen(args, stdout=sys.stdout, stderr=subprocess.STDOUT)

    logger.info("Letting it run for a bit")
    time.sleep(5)
    process.terminate()
    logger.info("Done")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
