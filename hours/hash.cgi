#!perl
print "content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;


my %scientists = (
	"Newton"	=>	"isaac",
	"Einstein"	=>	"Albert",
	"Darwin"	=>	"Charles",
);

print $scientists{Newton} . "<br />";
print $scientists{"Einstein"} . "<br />";
print $scientists{"Darwin"} . "<br />";
print $scientists{Nyson} . "<br />";

my @scientists = %scientists;

print "@scientists" . "<br />";
print scalar @scientists . "<br />";

my $data = "orange";
my @data = ("purple");
my %data = ( "1" => "blue");

print $data , "<br />";
print $data[0] ,"<br />" ;
print $data["0"] ,"<br />" ;
print $data{1} ,"<br />" ;
print $data{"1"} ,"<br />" ;
