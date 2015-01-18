# videopizza

video delivered just the way you like it

# Integration Project req's

- Flask
- livereload
- Python 2.7

## Wireframe

- Link TODO

## Use cases

- Link TODO

## Logo and Branding

- Link TODO

## Player tool

User: typical Facebook / Twitter internet user

From a long video, VideoPizza repackages slices that are short clips, are each
tweetable and shareable. The Player Tool is embeddable on publisher websites (a
la Storify embeds) or can self-host the videos plus the interesting slices.

Posts on Twitter and Facebook that include VideoPizza slices create better
social engagement over smaller portions of the full video.

- Bootstrap / HTML / LESS
- [Video.js](http://www.videojs.com/)

## Autoclip tool

User: journalist / editor / video producer

If you have a video online that contains text transcripts (e.g. C-SPAN, YouTube
closed captioning), the Autoclip Tool will analyze the text, score the
sentences, and identify the most "interesting" parts of the video. An editor
can then choose which clips are actually interesting and tweet/share those.

- Python
- Hand-crafted natural language processing using POS tagging and stop words
- [VideoGrep](https://github.com/antiboredom/videogrep)
- [MoviePy](http://zulko.github.io/moviepy/)

## Annotation tool

User: journalist / editor / video producer

OR: hyper-engaged Internet user viewing a video

Some videos can't be automatically sliced via VideoPizza, or editors won't
agree with the chosen slices. The Annotation Tool provides an interactive
interface so that you can manually annotate different parts of a video and
then treat those as slices.

- [Video.js](http://www.videojs.com/)
- [Elasticsearch](http://www.elasticsearch.com/)
- [Open Video Annotation project](http://www.openvideoannotation.org/)
