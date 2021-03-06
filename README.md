# videopizza

Video delivered just the way you like it.

VideoPizza sifts through an entire video to find its richest portions and delivers them in easily-consumable, shareable "slices."

It does this using fancy natural language processing against the transcript of the video, along with some server-side magic. A rich timeline annotation UI allows for manual editing of those slices, which we call "toppings". And a player allows those slices and toppings to be consumed in a tasty package, either in standalone mode or as an embed on a publisher website.

NOTE: this is just a proof-of-concept.

![videopizza](https://raw.githubusercontent.com/amontalenti/videopizza/master/assets/videopizza-logo.png)

![videopizzagif](https://raw.githubusercontent.com/amontalenti/videopizza/master/assets/SMALL.gif)

[http://videopizza.org](http://videopizza.org)

## Integration Project req's

- Flask
- Python 2.7

## Wireframe

[InVision Clickable Wireframe](http://invis.io/G42110QRX)

## Use cases

[Use Cases GDoc](http://goo.gl/QpM4Lk)

## Logo and Branding

in `assets/`

## Player tool

User: typical Facebook / Twitter internet user

From a long video, VideoPizza repackages slices that are short clips, are each
tweetable and shareable. The Player Tool is embeddable on publisher websites (a
la Storify embeds) or can self-host the videos plus the interesting slices.

Posts on Twitter and Facebook that include VideoPizza slices create better
social engagement over smaller portions of the full video.

- Bootstrap / HTML / LESS
- [Video.js](http://www.videojs.com/)

## Autoclipper tool

Code: `submodules/autoclipper`

User: journalist / editor / video producer

If you have a video online that contains text transcripts (e.g. C-SPAN, YouTube
closed captioning), the Autoclip Tool will analyze the text, score the
sentences, and identify the most "interesting" parts of the video. An editor
can then choose which clips are actually interesting and tweet/share those.

- Python
- Hand-crafted natural language processing using POS tagging and stop words
- [VideoGrep](https://github.com/antiboredom/videogrep)
- [MoviePy](http://zulko.github.io/moviepy/)

## Annotator tool

Code: `submodules/annotator`

User: journalist / editor / video producer

OR: hyper-engaged Internet user viewing a video

Some videos can't be automatically sliced via VideoPizza, or editors won't
agree with the chosen slices. The Annotation Tool provides an interactive
interface so that you can manually annotate different parts of a video and
then treat those as slices.

- [Video.js](http://www.videojs.com/)
- [Elasticsearch](http://www.elasticsearch.com/)
- [Open Video Annotation project](http://www.openvideoannotation.org/)

## Team Members

- Andrew Montalenti
- Amelia Winger-Bearskin
- Alessandra Villaamil
- Daniel Mclaughlin
- Elizabeth Kilroy
- Fred Ritchin
- Jasmine Henderson
- Kristina Budelis
- Liam Andrew
- Meredith Derby Berg
- Ross Goodwin
- Sharon Chen
- Sky Dylan-Robbins
- Steph Rymer
- Tobias Wright
