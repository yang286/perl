#!perl
print "content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my @stack = (
	"Eileen ",
	"Denise " ,
	"charlie ",
	"Roy "    ,
	"Fred "
);

print @stack , '<br />';
print pop @stack, "<br />";
print @stack , '<br />';
push @stack, "Yang ", "Long";
print @stack , '<br />';
print shift @stack, "<br />";
print @stack , '<br />';
unshift @stack, "Angela", "hechuan";
print @stack, "<br />";
