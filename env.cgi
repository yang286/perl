#!D:\WebWAPM\XAMPP\perl\bin\perl.exe
print <<END_OF_HTML;
Content-type: text/html

<html>
<head>
	<title>About this Server</title>
	</head>

	<body>
		<h1>About this Server</h1>

		<hr>
		<pre>
			server Name:	$ENV{server_NAME}
			Listening on Port: $ENV{SERVER_PORT}
			Server Softerware: $ENV{SERVER_SOFTWARE}
			Server Protocol:   $ENV{SERVER_PROTOCOL}
			CGI Version:	   $ENV{GATEWAY_INTERFACE}
		</pre>
		<hr>
	

	</body>
</html>
END_OF_HTML
