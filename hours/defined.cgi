#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my ($a, $b);
$b = 10;
if (defined $a) {
	print "\$a has a value.\n";
} else {
	print "\$b has a value.\n";
}
