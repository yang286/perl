#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my $mday = localtime();
print "$mday";
print "<br />";
print my $gmt = gmtime();
print "<br />";
my ($sec, $min, $hour) = localtime();
printf ("%02d:%02d:%02d", $hour, $min, $sec);
print "<br />";
