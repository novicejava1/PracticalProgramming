extends Node2D

func _on_Button_mouse_entered():
	$Sprite.texture = load('res://penguin.png')
	#$Sprite.texture = null

func _on_Button_mouse_exited():
	$Sprite.texture = load('res://penguin_gray.png')
