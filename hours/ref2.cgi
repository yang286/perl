#!perl
print "content-type: text/html; charset = utf-8\n\n";

use strict;
use warnings;

my @array1 = (1, 2,3, 4,5 ,);
print @array1;

my @array2 = [1, 2, 3, 4, 5];
print @array2 , "<br />";


my $array3Ref = [1,2,3,4, 5];
print $array3Ref, "<br />";;
print @{ $array3Ref }, "<br />";
print @$array3Ref;
