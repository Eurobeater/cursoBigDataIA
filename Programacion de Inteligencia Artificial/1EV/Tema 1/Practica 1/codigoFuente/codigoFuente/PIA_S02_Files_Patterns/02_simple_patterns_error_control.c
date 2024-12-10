#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main (int argc, char *argv[]) {
  FILE *fp;
  char *line, *pattern;
  int occurrences;
  size_t len;
  ssize_t read;

  if (argc < 3) {
    fprintf(stderr, "Error! You need to provide the filepath and the pattern.\n");
    fprintf(stderr, "Sinopsis: ./02_simple_patterns_error_control <file> <pattern>\n");
    exit(EXIT_FAILURE);
  }
  
  pattern = argv[2];
  occurrences = 0;
  len = 0;

  if ((fp = fopen(argv[1], "r")) == NULL) {
    fprintf(stderr, "Error opening file %s!\n", argv[1]);
    exit(EXIT_FAILURE);
  }

  while ((read = getline(&line, &len, fp)) != -1) {
    if (strstr(line, pattern) != NULL) {
      occurrences++;
    }

  }

  fclose(fp);
  
  printf("The word %s appeared %d times in the file %s\n",
	 argv[2], occurrences, argv[1]);

  return 0;
}
