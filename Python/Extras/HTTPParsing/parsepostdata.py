postdata = {b'--------------------------a7beefa9095fb995\r\nContent-Disposition: form-data': [b''], b' name': [b'"username"\r\n\r\nuser1\r\n--------------------------a7beefa9095fb995\r\nContent-Disposition: form-data', b'"password"\r\n\r\npassuser1\r\n--------------------------a7beefa9095fb995\r\nContent-Disposition: form-data', b'"gender"\r\n\r\n1\r\n--------------------------a7beefa9095fb995--\r\n']}

username = postdata[b' name'][0]
password = postdata[b' name'][1]
gender = postdata[b' name'][2]

print(username.decode().split("\n")[2])
print(password.decode().split("\n")[2])
print(gender.decode().split("\n")[2])