@a = (0..9);
@b = (0..9);
@c = (0..9);
foreach $a (@a) {
	foreach $b (@b) {
		foreach $c (@c) {
		print " $a \t $b \t $c\n";
	}
}
}
