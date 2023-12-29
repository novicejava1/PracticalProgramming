extends Node2D

#export var direction = "LEFT"
var direction = MainScene.direction
#var direction = "LEFT"
var speed = 400
var angular_speed = PI
var screen_size
var slab_size
var nodes

#func _ready():
#	if direction == "UP" or direction == "DOWN":
#		#get_tree().change_scene("res://VerticalSlider.tscn")
#		load("res://VerticalSlider.tscn")
#	else:
#		#get_tree().change_scene("res://HorizontalSlider.tscn")
#		load("res://HorizontalSlider.tscn")

#func _ready():
#	#direction = get_tree().get_root().get_node("MainScene").direction
#	#direction = get_tree().root.get_node("/root/MainScene").direction
	
func _process(delta):
	#rotation += angular_speed * delta
	#direction = get_tree().get_root().get_node("MainScene").direction
	#direction = get_tree().get_script().get(direction)
	#direction = get_tree().get("direction")
	#direction = 
	print("direction")
	print(direction)
	screen_size = get_viewport_rect().size
	slab_size = $Sprite.texture.get_size()
	print(screen_size)
	print(slab_size)
	print(rotation)
	if  direction == "UP":
		var velocity = Vector2.UP * speed
		move(direction, velocity, delta)
	elif direction == "RIGHT":
		var velocity = Vector2.RIGHT * speed
		move(direction, velocity, delta)
	elif direction == "LEFT":
		var velocity = Vector2.LEFT * speed
		move(direction, velocity, delta)
	else:
		var velocity = Vector2.DOWN * speed
		move(direction, velocity, delta)


func move(direction, velocity, delta):
	#pass
	print(velocity)
	print(position)
	position = position + velocity * delta
	print(position)
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)
	
	if direction == "UP":
		if position.y == 0:
			position.y = screen_size.y
	elif direction == "RIGHT":
		if position.x == screen_size.x:
			position.x = 0
	elif direction == "LEFT":
		if position.x == 0:
			position.x = screen_size.x
	else:
		if position.y == screen_size.y:
			position.y = 0
