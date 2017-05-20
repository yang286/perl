#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my @outer = ("Sun", "Mercury", "Venus", undef, "Mars");
my @inner = ("Earth", "Moon");

$outer[2] = @inner;
print $outer[2] ," <br />";


my $color = "Indigo";
my $slarref = \$color;

print $color . "<br />";
print $slarref . "<br />";
print ${ $slarref } . "<br />";
print $$slarref  . "<br />";


#如果是一个对array或者hash的引用，你可以用花括号或者更加风靡的箭头运算符->：
#

my @colours = ("red", "Orange", "Yellow", "Green", "blue");
my $arrRef = \@colours;

print $colours [0] . "<br />";
print ${ $arrRef } [0] . "<br />";
print $arrRef->[0] . "<br />";

my %atomicWeights = ("Hydrogen" => 1.008, "Helium" => 4.003, "Manganese" => 45.97);
my $hashref = \%atomicWeights;

print $atomicWeights {"Helium"} . "<br />";
print ${$hashref}{"Hydrogen"} . "<br />";
print $hashref->{Manganese} . "<br />";
						#print $hashref->{"Manganese"} . "<br />"; same al the above;

