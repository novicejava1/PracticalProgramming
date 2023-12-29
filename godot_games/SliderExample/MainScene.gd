extends Node

#export var direction = "UP"
var direction = "LEFT"

func _ready():
	
	if direction == "UP" or direction == "DOWN":
		#get_node("VerticalSlider").get_node("Slider1").direction = direction
		#get_node("VerticalSlider").get_node("Slider2").direction = direction
		#get_node("VerticalSlider").get_node("Slider3").direction = direction
				
		get_tree().change_scene("res://VerticalSlider.tscn")
		
	else:
		get_tree().change_scene("res://HorizontalSlider.tscn")
		#load("res://HorizontalSlider.tscn")
		#get_node("HorizontalSlider").get_node("Slider1").direction = direction
		#get_node("HorizontalSlider").get_node("Slider2").direction = direction
		#get_node("HorizontalSlider").get_node("Slider3").direction = direction
