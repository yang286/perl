#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

sub hyphenate {
	#从array中取出第一个参数
	my $word = shift @_;

	$word = join "-", map { substr $word, $_, 1 } (0 ..  (length $word) - 1);
	return $word;
}

print hyphenate("exterminate");
print "<br />";

my $x = 7;
sub reassign {
	$x = 148;
}

reassign($x);
print $x;
