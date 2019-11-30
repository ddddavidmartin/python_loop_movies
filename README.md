Play movies from a given directory in a loop.


## The use case is as follows

- have a party
- play movies on a projector without sound just for the athmosphere
- instead of playing every movie continuously, switch to a different one for example every 5 minutes
- basically it is like a slide-show, except with movies

## Example

Have a directory `movies` with `A.mp4` and `B.mp4`

```
$ python loop_movies.py movies --loop_time 300

-> A.mp4 plays for 5 minutes (300 seconds)
-> B.mp4 starts and plays for 5 minutes; A.mp4 is stopped
-> A.mp4 continues from where it stopped and plays for 5 minutes; B.mp4 is stopped
-> B.mp4 continues from where it stopped before; A.mp4 is stopped
-> ...
```

## Requirements

- Python 3
- `pip3 install python-vlc python-cocoa`
- vlc


## Notes

This is a super hacky put-together-in-one-night kind of program. It seems to work okay on my end on MacOS though.
