#!D:\WebWAPM\XAMPP\perl\bin\perl.exe

use strict;

my %env_info = (
	SERVER_SOFTWARE		=> "the server software",
	SERVER_NAME		=> "the server hostname or IP address",
	GATEWAY_INTERFACE	=> "the CGI specification revision",
	SERVER_PROTOCOL		=> "the server protocol name",
	SERVER_PORT		=> "the port number for the server",
	request_method		=> "the HTTP request method",
	PATH_INFO		=> "the extro path info",
	PATH_TRANSLATED		=> "the extra path info translated",
	DOCUMENT_ROOT 		=> "the server document root directory",
	SCRIPT_NAME		=> "the script name",
	QUERY_STRING		=> "the query string",
	REMOTE_HOST		=> "the hostname of the client",
	REMOTE_ADDR		=> "the IP address of the client",
	AUTH_TYPE		=> "the authentication method",
	REMOTE_USER		=> "the authenticated username",
	REMOTE_IDENT		=> "the remote user is (RFC 931): ",
	CONTENT_TYPE		=> "the media type of the data",
	CONTENT_LENGTH		=> "the length of the request body",
	HTTP_ACCEPT		=> "the media types the client accepts",
	HTTP_USER_AGERT		=> "the browser the client is using",
	HTTP_REFERER		=> "the URL of the referring page",
	HTTP_COOKIE		=> "the cookie(s) the client sent"
);

print "Content-type: text/html\n\n";

print <<ND_OF_HEADING;

<html>
	<head>
		<title>A List of Environment Variables</title>
	</head>

	<body>
		<h1>CGI Environment Variables</h1>

		<table border=1>
			<tr>
				<th>Variable Name</th>
				<th>Description</th>
				<th>Value</th>
			</tr>
	ND_OF_HEADING

	my $name;

	# Add additional variables defined by web server or browser
	foreach $name ( keys %ENV) {
		$env_info{$name} = "an extra variable provided by this server"
			unless exists $env_info{$name};
	}

	foreach $name ( sort keys %env_info ) {
		my $info = $env_info{$name};
		my $value = $ENV{$name} || "<I>Not Defined</I>";
		print "<tr><td><b>$name</b></td><td>$info</td><td>$value</td></tr>\n";
	}

	print "</table>\n";
	print "</body></html>\n";
