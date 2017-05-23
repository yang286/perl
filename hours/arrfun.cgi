#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my @elements = ("Antimonyl", "Arsenic", "Aluminum", "Selenium");
print @elements, "<br />";
print "@elements <br />";
print join ",", @elements , "<br />";

print reverse("Hello", "world") ," <br />";
my $hello = "Hello, world";
print scalar reverse $hello . "2c" ;
print "<br />";

my @capitals = ("Baton Rouge", "Indianapolis", "Columbus", "Montgomery", "Helena", "Denver", "Boise");
print  join ", ",  map { uc $_ } @capitals;
print "<br />";
print join "    ,   ", grep { length $_  == 6 } @capitals;
print "<br />";
print grep { $_ eq "Columbus" } @capitals;
print "<br />";

my @elevations = (19, 1, 2, 100, 3, 34, 98, 102, 99, 2234, 28);
print "@elevations";
print "<br />";
print sort "@elevations";
print "<br />";
print join ", ", sort @elevations;
print "<br />";
print sort { $a cmp $b } @elevations;
print "<br />";
print join ", ", sort { $a cmp $b } @elevations;
print "<br />";
print sort { $a <=> $b } @elevations;
print "<br />";
print join ", ", sort { $a <=> $b } @elevations;

sub comparator {
	#lost of code...
	#return -1, 0 or 1
}
#print join ", ", sort comparator @elevations;
#不过你不能对grep或map这样做。

