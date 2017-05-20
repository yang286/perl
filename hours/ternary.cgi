#!perl
print "content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my $gain = 1;
print "You gained ", $gain, " ", ($gain == 1 ? "experience point<br />" : "experience points<br />"), "!";


my $eggs =5;
print "you have ", $eggs == 0 ? "no egg" :
				   $eggs == 1 ? "an egg" :
				    "$eggs eggs";
