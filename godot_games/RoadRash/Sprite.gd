extends Sprite

var speed = Vector2(100.0, 0)
var angular_speed = PI

func _process(delta):
	#rotation += angular_speed * delta
	position += speed * delta
	
	
