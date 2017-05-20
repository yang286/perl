#!perl
print "content-type: text/html; charset = utf-8\n\n";


use strict;
use warnings;

my $word = "ad[]aaarsdfjfjslsdflsldkfj ddif hxi";
my $strlen = length $word;
print $strlen;

if ($strlen > 15) {
	print "'", $word, "' is a very long word<br />";
} elsif (10 <= $strlen && $strlen <= 15) {
	print "'", $word, "' isas a medium-length word<br />";
} else {
	print "'", $word, "' is a short word<br />";
}

print "'", $word, "' is actually enormous<br />" if $strlen >=20;

#unless...else...
#
my $temperature = 11;
unless ($temperature > 30) {
	print $temperature, " degrees celsius is not very hot<br />";
} else {
	print $temperature, " degrees Celsius is actually pretty hot";
}


#而相比之下，这种写法就被强烈推荐，因为实在是太易于阅读了：
#
print "oh no, it's too cold" unless $temperature > 15;


