#include <stdio.h>
#include <stdlib.h>

int main() {
	int magic;
	char input[60];

	puts("Guess the correct key to win!");
	magic = -559038737;
	printf("Enter the key: ");
	gets(input);
	if (magic == 0xCAFEBABE)
		return system("cat flag.txt");
	puts("Wrong Key");
	return puts("Try again!");
}
