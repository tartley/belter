# Belter

A videogame with 2D vector graphics, reminiscent of Asteroids.

## Status

Just started. A blank window.

## Prerequisites

For now, prerequisites must be manually installed.

Debian/Ubuntu:

    sudo apt-get install -y freeglut3-dev

Fedora/CentOS/RedHat:

    sudo yum install freeglut-devel

## To run

For now, is only runnable from source.

Create and populate virtualenv:

    make setup

Then run with:

    ./run

## Instructions

F10 to toggle windowed/fullscreen, and cycle through available monitors.

That's all that works right now.

## TODO

* perhaps order should be: virtualenv, download, install, freeze ?
* A ship has a body which describes a triangle
* When added to the world, the ship's body is converted into a Glyph, which is
  sent to gfx card (vbo? vao?) and id is added to the render collection.
* In on_draw, we draw all the glyphs
* draw glyphs in correct position
* draw glyphs in correct orientation
* bodies may consist of polygons, which are tessellated into triangles
* screenshot in readme
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
* executable
* github release
* e2e test of building executable and running it in self-test mode

## Gameplay

Main engine reverse direction after landing on an asteroid, so you can moved it
around:

    ____A____

No: Simpler, land on (or dock with) things nose-first.

    ____V____


The visual could be improved by unfolding landing gear, which is cool:

    ____X____

This is worse than a thrust-style tether, in that wiggling through gaps
isn't as hair-raising. But it is better in that the asteroid moves in freefall,
as opposed to a tethered spiral, and hence it's path can be more
precisely and meaningfully predicted, both by the player, and by the game's
HUD, for example in plotting orbits or estimated path to point of impact.

