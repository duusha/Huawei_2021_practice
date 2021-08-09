#include <stdint.h>

typedef struct s {
	int a, b ,c;
	char d;
};

int main() {
	int a  = 1;
	char b;
	s.a = 4;
	s.b = 48;
	if (s.a + s.b < 60) {
		s.a = 5;
	}
	s.c = s.b + s.a;
 

  for (int i = 0; i < 3; i++) {
    s.a += i;
  }

  return s.d;
}
