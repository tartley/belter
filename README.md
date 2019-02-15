# Belter

A videogame with 2D vector graphics, reminiscent of Asteroids.

## Instructions

F10 to toggle windowed/fullscreen, and cycle through available monitors.

## TODO

* `pip install -U pip` should be separate step, to make sure it gets done before all else.
* A ship has a body which describes a triangle
* travis builds
* readme build badge
* When added to the world, the ship's body is converted into a Glyph,
  which is sent to gfx card (vbo? vao?) and id is added to the render
  collection.
* In on_draw, we draw all the glyphs
* draw glyphs in correct position
* draw glyphs in correct orientation
* bodies may consist of polygons, which are tessellated into triangles
* produce an linux executable
* make a github release
* ask someone to download and double click
* e2e test which builds the executable, runs with --selftest|exitafter,
  asserts exitval.
* bodies are also added to pymunk
* world.update calls pymunk.step
* results of pymunk.step are used for render positions and orientations
* bodies are rendered as an outline, with a black interior
* keys to control ship
* starfield
* pip-tools to pin subdeps
* monitor my Py2D PR https://github.com/sseemayer/Py2D/pull/12

