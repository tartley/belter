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
* self documenting makefile
* copy stuff back into project template
* executable
* github release
* e2e test of building executable and running it in self-test mode

## Gameplay

### Goals

Put high value asteroids into the fab intake?
* how to discern high value?
  * color?
  * reuse "Asteroids" background tones as proximity guage?
* why?
  * provided with raw material, the fab makes things?
    * fuel?
    * extra life?
  * unlocks progress to next level?
    * need to fill the fab?
      Implies same amount for each level.
      So maybe harder levels make high value asteroids harder to come by?
    * need to find all high value asteroids?
      Levels could have varying amounts of high value asteroids.

  * filling it, or collecting all high value asteroids, unlocks next level?

### Landing / Docking

Conventional landing on the tail-fins:

    ____A____

But this means we can't use main engine for thrusting against the thing
we've landed on / docked with.

One solution is, after landing, the whole ship (or just its engines?)
gimbal around 180 degrees on the landing gear after. Then the main engines are
pointing at the sky.

But it seems simpler, both gamedev wise and in real life, in a low grav
environment, to land on (or dock with) things nose-first:

    ____V____

This looks a bit top-heavy, and weak at the point of contact. So thicken it
up at the bottom by unfolding landing gear. Which is cool anyhow:

    ____X____

This is worse than a thrust-style tether, in that wiggling through gaps
isn't as hair-raising. But it is better in that the asteroid moves in freefall,
as opposed to a tethered spiral, and hence it's path can be more
precisely and meaningfully predicted, both by the player, and by the game's
HUD, for example in plotting orbits or estimated path to point of impact.

