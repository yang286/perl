#!perl
use strict;
use warnings;

print "Content-type: text/html; charset=utf-8\n\n";

my $undef= undef;
print "test<br />";
print $undef;


my $num = 4040.6662;
print $num , "<br />";

my $string = "Hello world";
print $string . '<br />';

print "Hello " , $num; 
