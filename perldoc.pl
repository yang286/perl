@lines = `perldoc`;
foreach (@lines) {
	s/\w<([^>]+)>/\U$1/g;
	print;
}
