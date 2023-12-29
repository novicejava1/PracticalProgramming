extends Node2D


func _on_Button_pressed():
	#$Sprite.visible = not $Sprite.visible
	if $Sprite.visible == true:
		$Sprite.visible = false
	else:
		$Sprite.visible = true
