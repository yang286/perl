#!D:\WebWAPM\XAMPP\perl\bin\perl.exe -w
print "Content-type: text/html; charset=GB2312\n\n";
$input = <STDIN>;
if ($input = "\n") {
print "That was just a blank line! <br>";
} else {
print "That line of input was: $input";
}

$text = "a line of test \n\n";
print $text;
chomp $text;
print $text;
print $bb;
print '  $bb';
