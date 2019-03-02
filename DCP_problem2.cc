#include<iostream>
#include<vector>
#include<algorithm>

template<typename T>
void printVector(std::vector<T> vect){
    for(typename std::vector<T>::iterator i = vect.begin(); i != vect.end(); i++)
        std::cout << *i << std::endl;
}

std::vector<int> naiveProductVector(std::vector<int> vect){
    int product = 1;
    
    std::vector<int> resultVector = vect;

    for(std::vector<int>::iterator i = vect.begin(); i != vect.end(); i++)
        product *= *i;

    for(std::vector<int>::iterator i = resultVector.begin(); i != resultVector.end(); i++)
        *i = product / (*i);

    return resultVector;
}

std::vector<int> productVector(std::vector<int> vect){
    std::vector<int> leftVector, rightVector, resultVector, reversedRightVector;
    int product = 1, product2 = 1;

    for(std::vector<int>::iterator i = vect.begin(); i != vect.end(); ++i)
    {
        leftVector.push_back(product);
        product *= *i;
    }

    for(std::vector<int>::iterator j = vect.end() - 1; j != vect.begin() - 1; --j)
    {
        rightVector.push_back(product2);
        product2 *= *j;
    }
    
    std::reverse(rightVector.begin(), rightVector.end());

    for(int i = 0; i < leftVector.size(); ++i){
        resultVector.push_back(rightVector[i] * leftVector[i]);
    }

    return resultVector; 
}

int main(){
    std::vector<int> input {1,2,3,4,5}, input2 {3,2,1};

    printVector(productVector(input));
    std::cout << "\t" << std::endl;
    printVector(productVector(input2));
    return 0;
}