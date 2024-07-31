#include <iostream>

int main(){
    auto func = [](int x) -> int{
        return x + 2;
    };
    std::cout << func(2);
}
