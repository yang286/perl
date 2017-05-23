#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my $a = <STDIN>;
chomp $a;
my $true = (1 == 1);
if ($a) {
	print "Yes, this is true";
}
