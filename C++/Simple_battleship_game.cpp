#include <iostream>
using namespace std;

int main() {
    //! Initialization
    int number_of_hits = 0;
    int number_of_turns = 0;

    //! Determine the position, later uncomment this
    // int ship_placement[4][5] = {
    //     {0, 1, 0, 0, 1}, 
    //     {0, 1, 0, 0, 1}, 
    //     {1, 1, 1, 1, 0}, 
    //     {0, 1, 0, 1, 0}
    // };

    //! Use this one as the test subject
    int ship_placement[4][5] = {
        {0, 0, 0, 0, 0},
        {0, 0, 1, 0, 0},
        {0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0},
    };

    //! ask the user to input the row and column,
    //* if the user hit the 1, hit variable is increased by 1
    cout << "Enter the number of row (1 - 4): " << "\n";
    cout << "Enter the number of column (1 - 5): " << "\n";



    //! if it hit the column with the number 1 (or 0), immediately change the ship placement to 0

    //! win the game if the ship placement is all 0, and show the number of turns the user take to win the game


    //* will continue this later in the future
}