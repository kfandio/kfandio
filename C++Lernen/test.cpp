
#include<iostream> 

int main()
{
    //std::cout<<"Hello comment vous allez \n";
    // type name;
    // char   - character        - 'r'
    // int    - integer          - 50, 42
    // float  - floating points  - 4.2f
    // double - double precision - 5.0

    // int age = 0 ;
    //std::cin >> age; // pour entrer un nombre côté étulisateur
    //std::cin.ignore();


    // Operators : + * - / % & 
    // float r = 10.0f * 30.0f;

    //std::cout << age << std::endl;
    //std::cin.ignore();
    
    // bool condition = false;  // true or false

    int vie = 1;

    if (vie <= 0)
    {
        std::cout << "The player is dead" << std::endl;
    }
    else
    {
        std::cout << "The player ist alive" << std::endl;
    }
    std::cin.ignore();

    return 0;
}