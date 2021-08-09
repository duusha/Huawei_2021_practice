struct s
{
  int a;
  int b;
  int c;
  char d;
};
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
    a += i;
  }

  return a;
}


