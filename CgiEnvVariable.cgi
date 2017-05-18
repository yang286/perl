#!D:\WebWAPM\XAMPP\perl\bin\perl.exe
print "Content-type: text/html; charset=utf-8\n\n";
print <<END_OF_HTML;
<html>
		<head>
			<title>CGI Environment Variables</title>
		</head>
		<body>
		<pre>
		AUTH_TYPE
		$ENV{AUTH_TYPE}
		中文豆腐考虑啊几点上课了
		<!-- #The authentication method used to validate a user. This is blank if the request did not require authentication. -->
		
		CONTENT_LENGTH
		$ENV{CONTENT_LENGTH}
		
		<!-- #The length of the data (in bytes) passed to the CGI program via standard input. -->
		
		CONTENT_TYPE
		$ENV{CONTENT_TYPE}
		
		<!-- #The media type of the request body, such as "application/x-www-form-urlencoded ". -->
	
		DOCUMENT_ROOT
		$ENV{DOCUMENT_ROOT}

		<!-- #The directory from which static documents are served. -->
		
		GATEWAY_INTERFACE
		$ENV{GATEWAY_INTERFACE}
		
		<!-- #The revision of the Common Gateway Interface that the server uses. -->
		
		PATH_INFO
		$ENV{PATH_INFO}
		
		<!-- #Extra path information passed to a CGI program. -->
		
		PATH_TRANSLATED
		$ENV{PATH_TRANSLATED}
		
		<!-- #The translated version of the path given by the variable PATH_INFO. -->
		
		QUERY_STRING
		$ENV{QUERY_STRING}
		
		<!-- #The query information from requested URL (i.e., the data following "?"). -->
		
		REMOTE_ADDR
		$ENV{REMOTE_ADDR}
		
		<!-- #The remote IP address of the client making the request; this could be the address of an HTTP proxy between the server and the user. -->
		
		REMOTE_HOST
		$ENV{REMOTE_HOST}
		
		<!-- #The remote hostname of the client making the request; this could also be the name of an HTTP proxy between the server and the user. -->
		
		REMOTE_IDENT
		$ENV{REMOTE_IDENT}
		
		<!-- #The user making the request, as reported by their ident daemon. Only some Unix and IRC users are likely to have this running. -->
		
		REMOTE_USER
		$ENV{REMOTE_USER}
		
		<!-- #The user's login, authenticated by the web server. -->
		
		REQUEST_METHOD
		$ENV{REQUEST_METHOD}
		
		<!-- #The HTTP request method used for this request. -->
		
		SCRIPT_NAME
		$ENV{SCRIPT_NAME}
		
		<!-- #The URL path (e.g., /cgi/program.cgi) of the script being executed. -->
		
		SERVER_NAME
		$ENV{SERVER_NAME}
		
		<!-- #The server's hostname or IP address. -->
		
		SERVER_PORT
		$ENV{SERVER_PORT}
		
		<!-- #The port number of the host on which the server is listening. -->
		
		SERVER_PROTOCOL
		$ENV{SERVER_PROTOCOL}
		
		<!-- #The name and revision of the request protocol, e.g., "HTTP/1.1". -->
		
		SERVER_SOFTWARE
		$ENV{SERVER_SOFTWARE}
		
		<!-- #The name and version of the server software that is answering the client request. -->

		HTTP_ACCEPT
		$ENV{HTTP_ACCEPT}
		
		<!-- A list of the media types the client can accept. -->
		
		HTTP_ACCEPT_CHARSET
		$ENV{HTTP_ACCEPT_CHARSET}
		
		<!-- A{ list of the character sets the client can accept. -->}
		
		HTTP_ACCEPT_ENCODING
		$ENV{HTTP_ACCEPT_ENCODING}
		
		<!-- A list of the encodings the client can accept. -->
		
		HTTP_ACCEPT_LANGUAGE
		$ENV{HTTP_ACCEPT_LANGUAGE}
		
		<!-- A list of the languages the client can accept. -->
		
		HTTP_COOKIE
		$ENV{HTTP_COOKIE}
		
		<!-- A name-value pair previously set by the server. -->
		
		HTTP_FROM
		$ENV{HTTP_FROM}
		
		<!-- The email address of the user making the request; most browsers do not pass this information, since it is considered an invasion of the user's privacy. -->
		
		HTTP_HOST
		$ENV{HTTP_HOST}
		
		<!-- The hostname of the server from the requested URL (this corresponds to the HTTP 1.1 Host field). -->
		
		HTTP_REFERER
		$ENV{HTTP_REFERER}
		
		<!-- The URL of the document that directed the user to this CGI program (e.g., via a hyperlink or via a form). -->
		
		HTTP_USER_AGENT
		$ENV{HTTP_USER_AGENT}
		
		
		HTTPS
		$ENV{HTTPS}

<!-- The name and version of the client's browser. -->
		</pre>
		</body>
		</html>
END_OF_HTML
