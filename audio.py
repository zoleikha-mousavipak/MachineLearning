import pyglet

file = pyglet.resource.media('audio/when.mp3')
file.play()

pyglet.app.run()