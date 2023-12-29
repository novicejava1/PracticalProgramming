extends Node2D

var movement = 5

func _process(delta):
	#$Ball.position = Vector2(250, 0)
	$Ball.position.x = 450
	if Input.is_action_pressed("ui_left"):
		$Platform.position.x = $Platform.position.x - movement
		print($Platform.position.x)
	if Input.is_action_pressed("ui_right"):
		$Platform.position.x = $Platform.position.x + movement
		print($Platform.position.x)
