#include <ctime>
#include <iostream>

int main(){
    srand(time(NULL));
    int coin = rand() %2;

    if (coin == 0){
        std::cout << "head";
    } else {
        std::cout << "tail";
    }
    return 0;
}