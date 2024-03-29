"""Play the given video."""

import argparse
import logging

from cocoavlc import AppVLC

# pylint: disable=invalid-name

logger = logging.getLogger(__name__)


def run_video(video, set_time):
    """Run the given video file in a new thread."""
    app = AppVLC(video=video, set_time=set_time)
    app.run(timeout=None)  # never returns


def main():
    """Entry point for our simple vlc player
    """
    parser = argparse.ArgumentParser(description="Play a movie")
    parser.add_argument('movie', type=str, help="The movie to play.")
    parser.add_argument('--set_time', type=int, default=0,
                        help="Time to start the movie at in milliseconds.")
    args = parser.parse_args()

    run_video(args.movie, args.set_time)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
