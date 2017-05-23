#!perl
print "content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my @array = (qw/ Udf fe iksfw fc m"mx/ );
#my $i=5;

#
##do {
##	print $i, ": ", $array[$i];
##	$i++;
##} while ($i < scalar @array);
#

##do {
##	print $i, ":  $array[$i] " ;
##	$i++;
##} until ($i >= scalar @array );
#

for (my $i = 0; $i < scalar @array; $i++){
	print " $i: $array[$i];";
}

foreach my $string ( @array ) {
	print " $string ";
}


foreach my $i ( 0 .. $#array ) {
	print "here is $i, $array[$i]. ";
}
