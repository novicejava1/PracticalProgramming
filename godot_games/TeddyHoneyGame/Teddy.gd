extends KinematicBody2D

var score = 0

const speed = 200
const jumpForce = 600
const gravity = 800
var screen_size

var vel = Vector2()
var grounded = false

onready var ui = get_node("/root/MainScene/UI")


func _ready():
	screen_size = get_viewport_rect().size
	#scoreText.text = "0"

# physics loop - same as Unity's "FixedUpdate" function
func _physics_process(delta):
	
	vel.x = 0
	var direction = 0

	# movement inputs
	if Input.is_action_pressed("move_left"):
		vel.x -= speed
		
	if Input.is_action_pressed("move_right"):
		vel.x += speed
	
	# applying the velocity
	vel = move_and_slide(vel, Vector2.UP)
	
	# gravity
	vel.y += gravity * delta
		
	# jump inputs
	if Input.is_action_pressed("jump") and is_on_floor():
		vel.y -= jumpForce
	
	# sprite direction
	if vel.x < 0:
		$AnimatedSprite.animation = "walk"
		$AnimatedSprite.flip_h = true
	elif vel.x > 0:	
		$AnimatedSprite.animation = "walk"
		$AnimatedSprite.flip_h = false
	else:
		$AnimatedSprite.animation = "stand"
	
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)
	
	$AnimatedSprite.play()

func collect_berry(value):
	score += value
	ui.set_score_text(score)
	
