#!perl
print "content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my @scientists = (
	"aaa" => "bbb",
	"ccc" => "ddd",
	"name" => "roy yang",
	"age" => "31",
	"national" => "chinese",
);

#foreach my $k (keys %scientists) {
#	print "$k, : $scientists{$k}";
#}
##
#	foreach ( @scientists ) {
#		print $_;
#	}
#

print $_ foreach @scientists;
