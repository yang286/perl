#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my ($value, $from, $to, $rate, $rates);
my %rates = (
	pounds		=> 1,
	dollars		=> 1.6,
	marks		=> 3.0,
	"french francs"	=> 10.0,
	yen			=> 174.8,
	"swiss francs"	=> 2.43,
	drachma		=> 492.3,
	euro		=> 1.5
);

print "Enter your starting currency: ";
print "<br />";
$from = <STDIN>;
if (not exists $rates {$from}) {
	die "I don't know anything about $from as a currency\n"
}
print "Enter your target currency: ";
print "<br />";
$to = <STDIN>;
if (not exists $rates {$to}) {
	die "I don't know anything about $to as a currency\n"
}
print "Enter your amount: ";
$value = <STDIN>;
print "<br />";

chomp ($from, $to, $value);

$rate = $rates{$to} / $rates{$from};

print "$value $from is ", $value*$rate, " $to. \n";
