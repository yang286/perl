#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my $rc = system "perl", "array.cgi", "foo", "bar", "baz";
$rc >>= 8;
print $rc;
