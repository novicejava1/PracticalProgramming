extends Sprite

var movement = 5
var direction = 0

func _process(delta):
	if Input.is_action_pressed("ui_left"):
		direction = -1
		position = position + [movement, 0]
	if Input.is_action_pressed("ui_right"):
		direction = +1
		position = position + [movement, 0]

func _on_Timer_timeout():
	self.visible = not self.visible
