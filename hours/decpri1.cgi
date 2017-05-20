#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my %account = (
	"number" => "32422423424234242",
	"opened" => "89-22-1123",
	"owners" => [
		{
			"name" => "Philip Fry",
			"DOB" => "1974-93-22",
		},
		{
			"name" => "Hubert Farnsworth",
			"DOB" => "2831-32-232",
		},
	],
);

#my $ownersRef = $account{"owners"};
#my @owners = @{ $ownersRef };
#my $owner1Ref = $owners[0];
#my %owner1 = %{ $owner1Ref };
#my $owner2Ref = $owners[1];
#my %owner2 = %{ $owner2Ref };
#print $account{"owners"}, "<br />";
#
#


#my @owners = @{ $account{"owners"} };
#my %owner1 = %{ $owners[0] };
#my %owner2 = %{ $owners[1] };
#print "Accout #", $account{"number"}, "<br />";
#print "Opened on ", $account{"opened"}, "<br />";
#print "Joint owners:";
#print "<br />", $owner1{"name"}, " (born ", $owner1{"DOB"}, ")<br />";
#print "<br />", $owner2{"name"}, " (born ", $owner2{"DOB"}, ")<br />";
#
#

#my $ownersRef = $account{"owners"};
#my $owner1Ref = $ownersRef->[0];
#my $owner2Ref = $ownersRef->[1];
#print "Accout #", $account{"number"}, "<br />";
#print "Opened on ", $account{"opened"}, "<br />";
#
#print "<br />", $owner1Ref->{"name"}, " (born ", $owner1Ref->{"DOB"}, ")<br />";
#print "<br />", $owner2Ref->{"name"}, " (born ", $owner2Ref->{"DOB"}, ")<br />";
#
#



print "Accout #", $account{"number"}, "<br />";
print "Opened on ", $account{"opened"}, "<br />";
print "Joint owners:";
print "<br />" , $account{"owners"}->[0]->{"name"}, " (born ", $account{"owners"}->[0]->{"DOB"}, ")<br />";
print "<br />" ,  $account{"owners"}->[1]->{"name"}, " (born ", $account{"owners"}->[1]->{"DOB"}, ")<br />";
