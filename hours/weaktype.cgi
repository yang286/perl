#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my $str1 = "4G ";
my $str2 = "4H ";

print $str1 . $str2 , "<br />";
print $str1 + $str2 , "<br />";
print $str1 eq $str2 , ' <br />';
print $str1 == $str2 , " <br />";

#The classic error
print "yes" == "no";


