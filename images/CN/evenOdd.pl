#!/bin/perl
print "I can find out if the number is even or odd\n";
print "Enter an integer of your choice:\n";
$num=<>;
chomp($num);
if(int($num) % 2 == 0){
	print "The number you entered i.e. $num is Even\n";
} else {
	print "The number you entered i.e. $num is Odd\n";
}
print "Thank You :))\n";

