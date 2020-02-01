#include <iostream>
#include <string>

using namespace std;

int main (int argc, char **argv) {

    string name = "World";

    if (argc > 1) name = argv[1];

    cout << "Hello, " << name << "!";

    return EXIT_SUCCESS;
}