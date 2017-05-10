#!D:\WebWAPM\XAMPP\perl\bin\perl.exe -w
print "Content-type: text/html; charset=GB2312\n\n";
$fred = 2;
$fred += 8;
print "$fred\r";
print 15;
print "<${fred}s>\r . sdfl\n";
$a = 2 ** 9;
print "one ";
print 35 != 30 + 5;
print "two ";
print 35 == 30 + 5;
print '        three ';
print 33 == 30 + 5;
print '<br>' , "<br>";
$b = 'ÎÒ°®Äã $fred\' ';
print $b;
print '35' eq "35";
print 'Fred' gt 'barney' , '<br>';
print "aaa\n\r\h<br>";
if ($aa) {
	print "true";
}
else {
	print "false";
}
