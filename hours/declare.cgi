#!perl
pring "Context-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my %owner1 = (
	"name" => "Santa Claus",
	"DOB" => "1882-12-25",
);

#my $owner1Ref = \%owner1;

my %owner2 = (
	"name" => "Michey Mouse",
	"DOB" => "1928-11-18",
);

#my $owner2Ref = \%owner2;

#my @owners = ( $owner1Ref, $owner2Ref );

#my $ownersRef = \@owners;

my @owners = ( \%owner1, \%owner2 );

my %account = (
	"number" => "12345678",
	"opened" => "2000-01-01",
	"owners" => \@owners,
);



my $owner1Ref = {
	"name" => "Santo Claus",
	"DOB" => "1882-12-25",
};

my $owner2ref = {
	"name" => "Michey Mouse",
	"DOB" => "1928-11-18",
};

# 方括号表示匿名array
my $ownersRef = [ $owner1Ref, $owner2Ref ];

my %account = (
	"number" => "123456",
	"opened" => "2010-12-22",
	"owners" => $ownersRef,
);

my %account = (
	"number" => "21453423",
	"opened" => "2017-5-20",
	"owners" => [
		{
			"name" => "Philip Fry",
			"DOB" => "1987-04-11",
		},
		{
			"name" => "Hubert Farnsworth",
			"DOB" => "2888-222-22",
		},
	],
);
