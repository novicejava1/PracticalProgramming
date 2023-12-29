extends KinematicBody2D

var speed = 400

func _physics_process(delta):
	var velocity = Vector2.ZERO
	var direction = 0
	
	if Input.is_action_pressed("ui_left"):
		direction = -1
		velocity = Vector2(speed * direction, 0)
		#position -= velocity * speed * delta
		#$AnimatedSprite.animation = "walk"
	if Input.is_action_pressed("ui_right"):
		direction = +1
		velocity = Vector2(speed * direction, 0)
		#position += velocity * speed * delta
		#$AnimatedSprite.animation = "walk"
	
	#print(velocity)
	if velocity.x < 0:
		$AnimatedSprite.animation = "walk"
		$AnimatedSprite.flip_h = true
		# See the note below about boolean assignment.
		#$AnimatedSprite.flip_h = velocity.x < 0
	elif velocity.x > 0:
		$AnimatedSprite.animation = "walk"
		$AnimatedSprite.flip_h = false
	else:
		$AnimatedSprite.animation = "stand"
	
	move_and_slide(velocity)
	$AnimatedSprite.play()
