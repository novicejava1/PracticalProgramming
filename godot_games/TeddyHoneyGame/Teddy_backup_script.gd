extends KinematicBody2D

var speed = 400.0
var gravity = 100.0

func _physics_process(delta):
	var velocity = Vector2.ZERO
	var direction = 0
	
	if Input.is_action_pressed("move_left"):
		direction = -1
		velocity = Vector2(speed * direction, 0)
		#position -= velocity * speed * delta
		#$AnimatedSprite.animation = "walk"
	if Input.is_action_pressed("move_right"):
		direction = +1
		velocity = Vector2(speed * direction, 0)
		#position += velocity * speed * delta
		#$AnimatedSprite.animation = "walk"
	if Input.is_action_pressed("jump"):
		velocity.x += speed * delta
		velocity.y -= gravity
		velocity = Vector2(velocity.x, velocity.y)
	
	print(velocity)
	if velocity.x < 0:
		$AnimatedSprite.animation = "walk"
		$AnimatedSprite.flip_h = true
		# See the note below about boolean assignment.
		#$AnimatedSprite.flip_h = velocity.x < 0
	elif velocity.x > 0:
		$AnimatedSprite.animation = "walk"
		$AnimatedSprite.flip_h = false
	elif velocity.length() > 0:
		$AnimatedSprite.animation = "jump"
		$AnimatedSprite.flip_h = false
	else:
		$AnimatedSprite.animation = "stand"
	
	move_and_slide(velocity)
	$AnimatedSprite.play()

