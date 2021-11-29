#!/bin/perl
print "I will Print the Power Table of the number you enter\n";
print "Please enter a number:\n";
$num=<STDIN>;
for($i=1; $i<=10; $i++)
{
	$power=$num ** $i;
	print "$num ^ $i = $power\n";
}
print "Thank You"

