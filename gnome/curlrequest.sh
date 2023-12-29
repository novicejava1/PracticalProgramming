#!/bin/bash

input=`zenity --forms --add-combo=METHOD --combo-values="GET|POST|HEAD|DELETE|PUT|TRACE" --add-combo=CONTENT --combo-values="application/json|text/html|application/xml" --add-entry="URL" --add-entry="PARMS" --width=500 --height=500`

echo $input

method=`echo $input | awk -F"|" '{print $1}'`
content=`echo $input | awk -F"|" '{print $2}'`
url=`echo $input | awk -F"|" '{print $3}'`
params=`echo $input | awk -F"|" '{print $4}'`

echo $method
echo $content
echo $url
echo $params

response=`curl -X $method -H $content $url?$params`

echo $response
zenity --info --text=$response
