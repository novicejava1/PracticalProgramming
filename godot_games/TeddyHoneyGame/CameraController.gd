extends Camera2D

onready var player = get_node("/root/MainScene/Teddy")

func _process(delta):
	position.x = player.position.x
