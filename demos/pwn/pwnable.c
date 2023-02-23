#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void win1();
void win2();

int main() {
	char stuff[] = "important stuff. pls don't change";
	char name[64];

	printf("input: ");
	gets(name);

	printf("\ninput is: %s\n", name);
	printf("stuff is: %s\n", stuff);

	return 0;
}

void win1() {
	printf("you win!\n");

	FILE *f = fopen("flag.txt", "r");
	if (!f) {
		printf("flag file not found\n");
		exit(1);
	}

	char buf[64 + 1];
	fgets(buf, 64, f);
	printf("%s\n", buf);

	exit(0);
}

void win2() {
	if (time(NULL) != 0) {
		printf("boo!\n");
		exit(0);
	}

	printf("you win!\n");
	printf("fake{flag}\n");

	exit(0);
}
