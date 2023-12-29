extends Node

#export var direction = "UP"
var direction = "DOWN"

func _ready():
	
	if direction == "UP" or direction == "DOWN":		
		get_tree().change_scene("res://VerticalSlider.tscn")
		
	else:
		get_tree().change_scene("res://HorizontalSlider.tscn")
