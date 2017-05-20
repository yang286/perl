#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my @array = (
	"print ",
	"these ",
	"strings ",
	"out ",
	"for ",
	"me 8"
);

my $array = "这个值不一样, <br />";

print $array[1];
print $array[2];
print $array[3];
print $array[4];
print $array[5];
print $array[6];
print $array[7] . "<br />";

print $array[-1];
print $array[-2];
print $array[-3];
print $array[-4];
print $array[-5];
print $array[-6];
print $array[-7] . "<br />";

print $array;

print "this array has " . (scalar @array) . "elements <br />"; # To get an array's length
print "The last populated index is " .$#array . "<br />"; # The last populated index is 5
print "Hello $array <br />";
print "Hello @array <br />";

#
#print "This is my email: yang286@gmial.com";
#Server Error.
#

print 'This is my email: yang286@gmial.com <br />';
print "This is my email: yang286\@gmial.com <br />";

print "Hello \$array <br />";
print "Hello \@array <br />";
