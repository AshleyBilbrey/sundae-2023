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

int main() {
	slowPrint("LOGON:");
	printf(" ");
	fflush(stdout);

	char input[64];
	fgets(input, 64, stdin);
	int result = strncmp("Joshua\n", input, 64);

	if(result == 0) {
		slowPrint("GREETINGS PROFESSOR FALKEN.\n\n");
		slowPrint("SHALL WE PLAY A GAME?\n\n");
		slowPrint("List Games\n\n");
		slowPrint("FALKEN'S MAZE\n");
		slowPrint("BLACK JACK\n");
		slowPrint("GIN RUMMY\n");
		slowPrint("HEARTS\n");
		slowPrint("BRIDGE\n");
		slowPrint("CHECKERS\n");
		slowPrint("CHESS\n");
		slowPrint("POKER\n");
		slowPrint("FIGHTER COMBAT\n");
		slowPrint("GUERRILLA ENGAGEMENT\n");
		slowPrint("DESERT WARFARE\n");
		slowPrint("AIR-TO-GROUND ACTIONS\n");
		slowPrint("THEATERWIDE TACTICAL WARFARE\n");
		slowPrint("THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n\n");
		slowPrint("moo{GL0B41_TH3RM0NUCL3AR_W4R}\a\n");
	} else {
		slowPrint("IDENTIFICATION NOT RECOGNIZED BY SYSTEM\n");
		slowPrint("--CONNECTION TERMINATED--\a\n");
	}

	return 0;
}

