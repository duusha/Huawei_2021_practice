typedef struct _s1 {
	int a;
	int b;
}_s1;
_s1 s1;
typedef struct _s2 {
	int c;
	char d;
}_s2;
_s2 s2;
int main()
{
  int a = 1;
  char b;
  s1.a = 4;
  s1.b = 48;
  if ((s1.a + s1.b) < 60)
  {
    s1.a = 5;
  }

  s2.c = s1.b + s1.a;
  for (int i = 0; i < 3; i++)
  {
    s1.a += i;
  }

  return s2.d;
}


