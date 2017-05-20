#!perl

use strict;
use warnings;

print <<ENG_OF;
status: 503 Database Unavailable
content-type: text/html

<html>
	<head><title>503 database unavailable</title></head>
	<body>
		<h1>Error</h1>
		<p>Sorry, the database is currently not available. Please try again later.</p>
	</body>
</html>
ENG_OF
