#!perl
print "content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my @array = (
	"apples",
	"bananas",
	(
		"linner",
		"list",
		"several",
		"entries",
	),
	"cherries",
);

print "@array <br />";
print "$array[3] <br />";

my %hash = (
	"beer" => "good ",
	"bananas" => (
		"green " => "wait",
		"yellow " => "eat",
	),
);

print " %hash <br />"; # this doesn't work!!
print  %hash , "<br />"; 
print $hash{"beer"} , "1 <br />";
print $hash{"bananas"}, "2 <br />";
print $hash{"wait"}, " 3<br />";
print $hash{"eat"}, "4<br />";
print $hash{"green"}, "5<br />";
print $hash{"yellow"}, "5<br />";


