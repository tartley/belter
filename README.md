# Belter

A videogame with 2D vector graphics, reminiscent of Asteroids.

## Instructions

F10 to toggle windowed/fullscreen, and cycle through available monitors.

## TODO

* A ship has a body which describes a triangle
  Use py2d!

* When added to the world, the ship's body is converted into a Glyph,
  which is sent to gfx card (vbo? vao?) and id is added to the render
  collection.
* In on_draw, we draw all the glyphs
* draw glyphs in correct position
* draw glyphs in correct orientation
* bodies may consist of polygons, which are tessellated into triangles
* bodies are also added to pymunk
* world.update calls pymunk.step
* results of pymunk.step are used for render positions and orientations
* bodies are rendered as an outline, with a black interior
* run currently doesn't work if the virtualenv isn't active.
  If it were a bash script again, it could invoke the ve's python.
  It ought to allow the passing of -O.
* pip-tools to pin subdeps

