"""Play the given video."""

import logging

from cocoavlc import AppVLC

logger = logging.getLogger(__name__)


def run_video(video):
    """Run the given video file in a new thread."""
    app = AppVLC(video=video)
    logger.info("Starting the video from the run script")
    app.run(timeout=None)
    logger.info("Time at the end: %s", app.player.get_time())


def main():
    """Entry point for our simple vlc player
    """
    run_video("movie.mp4")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
