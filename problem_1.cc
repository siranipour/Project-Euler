#include<iostream>
#include<vector>

unsigned int sum(unsigned int multiple){
	std::vector<unsigned int> vector;
	for(unsigned int i = multiple; i < 1000; i = i + multiple)
		vector.push_back(i);	
	
	unsigned int total = 0;

	for(auto i : vector)
		total += i;

	return total;
}

int main(){
	std::cout << sum(3) + sum(5) - sum(15) << std::endl;
	return 0;
}
