%module example
%{
extern double variable;
extern int fact(int n);
extern int mod(int x, int y);
extern const char* time();
%}

extern double variable;
extern int fact(int n);
extern int mod(int x, int y);
extern const char* time();
