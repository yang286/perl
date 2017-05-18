#!D:\WebWAPM\XAMPP\perl\bin\perl.exe
#Print a formatted list of all the environment variables

use strict;

print "Content-type: text/html\n\n";


my $var_name;
foreach $var_name ( sort keys %ENV ) {
	print "<P><B>$var_name</b><br>";
	print "$ENV{$var_name}</p>";
}
