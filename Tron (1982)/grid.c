#include <stdio.h>
#include <string.h>
#include <unistd.h>

void slowPrint(char* string) {	
	const size_t length = strlen(string);
	const useconds_t pauseLen = 90000;

	for(size_t index = 0; index < length; index++) {
		usleep(pauseLen);
		printf("%c", string[index]);
		fflush(stdout);
	}
}

int decompile() {
	slowPrint("MASTER CONTROL PROGRAM: Wrong answer, program. Muahahah!\n");
	slowPrint("You were de-rezzed in the grid.\n\a");
	return 0;
}

int main() {
	slowPrint("You are typing at your computer, when suddenly you were digitized into the grid!\n");
	slowPrint("YOU: !!!\n");
	slowPrint("Before you is a cylindro-conical lookin' dude with a face.\n");
	slowPrint("MASTER CONTROL PROGRAM: Hello program, you must compete in the games.\n");
	slowPrint("YOU: ._.\n");
	slowPrint("MASTER CONTROL PROGRAM: To survive, you must guess my super secure password! Muahahah!\n");
	slowPrint("YOU: :|\n");
	slowPrint("INPUT:");
	printf(" ");
	fflush(stdout);

	char input[64];
	fgets(input, 64, stdin);

	if(input[0] != 'm' || input[1] != 'o' || input[2] != 'o' || input[3] != '{' || input[23] != '}' || input[24] != '\n') {
		return decompile();
	}

	int word1[] = {624, 622, 590, 621, 629, 634};
	for(size_t index1 = 0; index1 < 6; index1++) {
		if((input[index1 + 4] + 539) != word1[index1]) return decompile(); 
	
	}

	char word2[] = "cOqNz";
	for(size_t index2 = 0; index2 < 5; index2++) {
		if((input[index2 + 10] + 133377) % 127 != word2[index2]) return decompile();
	}

	char offset[] = "joincowsay";
	int word3[] = {454, 303, 417, 490};
	for(size_t index3 = 0; index3 < 4; index3++) {
		if((input[index3 + 15] << 2) + offset[index3] != word3[index3]) return decompile();
	}

	char word4[] = "C($T";
	char offset2electricboogaloo[] = "daviscybersec.org";
	for(size_t index4 = 0; index4 < 4; index4++) {
		if((input[index4 + 19] ^ offset2electricboogaloo[index4 + 10]) != word4[index4]) return decompile();
	}

	slowPrint("MASTER CONTROL PROGRAM: I knew you were a user, not a program. I had underestimated you.\n");
	slowPrint("You rematerialized into reality.\n\a");
	return 0;
}

