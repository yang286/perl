#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

sub contextualsubroutine {
	return ("Everest", "K2", "Etna") if wantarray;
	return 3;
}

my @arr = contextualsubroutine();
print @arr;
print "<br />";
print "<br />";
my $sca = contextualsubroutine();
print $sca;
