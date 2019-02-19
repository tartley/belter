# Belter

A videogame with 2D vector graphics, reminiscent of Asteroids.

## To run

For now, is only runnable from source (see TODO item to create executable).

To create and populate virtualenv:

    make setup

Run 'belter' using the 'python' in our virtualenv:

    ~/.virtualenvs/belter/bin/python run

## Instructions

F10 to toggle windowed/fullscreen, and cycle through available monitors.

That's all that works right now.

## TODO

* install colout from origin using pip's git syntax
* install py2d from origin now that my PR is merged
* 'run' should be a bash script again, and should work regardless of whether
  virtualenv is active or not. Fix "to run" docs above. Should it create
  virtualenv automatically?
* Travis. put badge in readme.
* screenshot in readme
* `pip install -U pip` should be separate step, to make sure it gets done
  before all else.
* pip-tools or manual steps to pin subdeps
* A ship has a body which describes a triangle
* travis builds
* readme build badge
* When added to the world, the ship's body is converted into a Glyph, which is
  sent to gfx card (vbo? vao?) and id is added to the render collection.
* In on_draw, we draw all the glyphs
* draw glyphs in correct position
* draw glyphs in correct orientation
* bodies may consist of polygons, which are tessellated into triangles
* produce an linux executable
* make a github release
* ask someone to download and double click
* e2e test which builds the executable, runs with --selftest|exitafter, asserts
  exitval.
* bodies are also added to pymunk
* world.update calls pymunk.step
* results of pymunk.step are used for render positions and orientations
* starfield v1
* bodies are rendered as an outline, with a black interior
* keys to control ship
* copy stuff back into project template

## gameplay

main engine reverse direction after landing on an asteroid, so you can moved it around.

No: Simpler, land on (or dock with) things nose-first.

