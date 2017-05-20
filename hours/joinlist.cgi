#!perl
print "content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my @bones = ("humerus", ("jaw", "skull"), "tibia");
my @fingers = ("thumb", "index","middle", "ring", "little");
my @parts = (@bones, @fingers, ("foot", "toes"), "eyeball", "kunuckle");
print "@parts <br />";
print scalar (@parts) , " <br />";
print $parts[0] . "<br />";
print $parts[2] . "<br />";
print $parts[8] . "<br />";
print $parts[9] . "<br />";
print $parts[10] . "<br />";
print $parts[11] . "<br />";
print $parts[12] . "12<br />";
print $parts[13] . "13<br />";


my @array = ("alpha","beta", "Gamma","Pie");
my $scalar1 =("alpha","beta", "Gamma","Pie");
print $scalar1 . " 8<br />";
my $scalar = @array;
print $scalar. " a<br />";

my @arrya = ("alpa", "beta", "goo");
my $scala = "-x-";
print @arrya ,10 , "<br />";
print $scala, @arrya, 99 , '<br /> a';
