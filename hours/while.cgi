#!perl
print "content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;



my @array = ("aabb", "fftt", "1234", "229i", "29ci", "word", "content", "type", "aaa");



#my $i = 10;
#while ($i > scalar @array) {
#	print $i, ":  $array[$i]. ";
#	$i++;
#}
#


my $i = 0;
until ($i >= scalar @array) {
	print $i, ":  $array[$i]. ";
	$i++;
}
