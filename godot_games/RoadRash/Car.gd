extends KinematicBody2D

var velocity = Vector2.ZERO
var movement = 100

func _physics_process(delta):
	var direction
	if Input.is_action_pressed("ui_left"):
		direction = -1
		#$Sprite.rotate(-.05)
		velocity = Vector2(movement * direction, 0)
		move_and_slide(velocity)
	if Input.is_action_pressed("ui_right"):
		direction = 1
		$Sprite.rotate(.05)
		velocity = Vector2(movement * direction, 0)
		move_and_slide(velocity)
	if Input.is_action_pressed("ui_up"):
		direction = -1
		velocity = Vector2(0, movement * direction)
		move_and_slide(velocity)
	if Input.is_action_pressed("ui_down"):
		direction = 1
		velocity = Vector2(0, movement * direction)
		move_and_slide(velocity)

