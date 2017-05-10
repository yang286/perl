#!D:\WebWAPM\XAMPP\perl\bin\perl.exe -w
print "Content-type: text/html; charset=GB2312\n\n";
$dk = <STDIN>;
$c = defined ($madonna);
print $c;
if ( defined ($madonna) ) {
	print "The input was $madonna ";
} else {
	print "No input available! ";
}

