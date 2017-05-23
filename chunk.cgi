#!perl
print "content-type: text/html; charset=utf-8\n\n";

use strict;
use warnings;

my $var = '这是一个试用

多行子付存文本
的例子';

print $var;
