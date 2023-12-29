extends Node2D



func _on_Button_mouse_entered():
	$Sprite.texture = load('penguin.png')




func _on_Button_mouse_exited():
	$Sprite.texture = load('penguin_gray.png')
