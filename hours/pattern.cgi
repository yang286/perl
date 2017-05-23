#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;


my $string = "Hello world";

if ($string =~ m/(\w+)\s+(\w+)/) {
	print "success";
}
print "<br />";

print $1;
print "<br />";
print $2;
print "<br />";

my $str ="colourless green ideas sleep furiously";
print "$str";
print "<br />";
my @matches = $str =~ m/(\w+)\s+((\w+)\s(\w+))\s+(\w+)\s+(\w+)/;
print join ", ", map { "'" .$_. "'" } @matches;


print "<br />";

my $stri = "good morning world";
print $stri;
print "<br />";

$stri =~ s/world/yangroy/;
print $stri;
print "<br />";


my $string = "a tonne of feathers or a tonne  or bricks";
while ($string =~ m/(\w+)/g) {
	print "'".$1."\n";
}
print "<br />";


$string =~ s/[aeiou]/r/;
print $string;
print "<br />";
$string =~ s/[aeiou]/r/;
print $string;
print "<br />";
$string =~ s/[aeiou]/r/g;
print $string;
print "<br />";
