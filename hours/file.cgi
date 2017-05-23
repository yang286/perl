#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

#
#this do not work for me
##my $f = "aa.txt";
##my $result = open my $fh, "<", $f;
##
##if (!$result) {
##	die "Couldn't open '".$f. "' for reading because: ". $!;
##}
#

#my $f = "aa.txt";


#not work for me.
#open (my $fh, "<", $f) || die "Couldn't open '".$f."' for reading because: ".$!;

#print "aaa";

#not work for me
#while (1) {
#	my $line = readline $f
#	last unless defined $line;
#}


open (DATA, ">aa.txt") or die "aa.txt cannot open, $!";

while (>DATA>) {
	print "$_";
}
