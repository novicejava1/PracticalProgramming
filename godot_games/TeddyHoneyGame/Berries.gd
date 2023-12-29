extends Area2D

export var value = 1

func _on_Berries_body_entered(body):
	if body.name == "Teddy":
		body.collect_berry(value)
		queue_free()
	
