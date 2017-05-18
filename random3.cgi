#!D:\WebWAPM\XAMPP\perl\bin\perl.exe -w
print "Content-type: text/html\n\n";
@a = (0..7);
@b = (0..9);
@c = (0..9);
 my %sns = ();
for(my $i = 0;$i < 10; $i ++) {
   my $range = 10000;
   do{
   $no = rand($range);
   $no = int($no);
   $no = $no * 3 + 1;
   
   }while($sns{"$no"} == 1);
   $sns{"$no"} = 1;
   print " $no <br>";

}
