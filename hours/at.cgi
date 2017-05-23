#!perl
print "Content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;


##sub left_pad {
##	my $oldstring = $_[0];
##	my $width 	= $_[1];
##	my $padchar = $_[2];
##	my $newstring = ($padchar x ($width - length $oldstring)) . $oldstring;
##	return $newstring;
##}
##
##sub left_pad {
##	my $oldstring	= shift @_;
##	my $width		= shift @_;
##	my $padchar		= shift @_;
##	my $newstring = ($padchar x ($width - length $oldstring)) . $oldstring;
##	return $newstring;
##}


##sub left_pad {
##	my $oldstring	= shift;
##	my $width		= shift;
##	my $padchar		= shift;
##	my $newstring	= ($padchar x ($width - length $oldstring)) . $oldstring;
##	return $newstring;
##}
##


##sub left_pad {
##	my ($oldstring, $width, $padchar) = @_;
##	my $newstring	= ($padchar x ($width - length $oldstring)) . $oldstring;
##	return $newstring;
##}

##print left_pad ("hello", 4, "+");
#
#


sub left_pad {
	my %args = @_;
	my $newstring	= ( $args{"padchar"} x ($args{"width"} - length $args{"oldstring"})) . $args{"oldstring"};
	return $newstring;
}

print left_pad ( "padchar" => "+","oldstring" => "he", "width" => 10);

