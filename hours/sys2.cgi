#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;


my $text = `perl wrong.cgi foo bar baz`;
print $text;
