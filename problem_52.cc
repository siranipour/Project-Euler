#include<map>
#include<iostream>

unsigned int primed_product(int number)
{
	std::map< int, int> mappings;
	mappings[1] = 2;
	mappings[2] = 3;
	mappings[3] = 5;
	mappings[4] = 7;
	mappings[5] = 11;
	mappings[6] = 13;
	mappings[7] = 17;
	mappings[8] = 19;
	mappings[9] = 23;
	mappings[0] = 29;
   		
	unsigned int product = 1;
 
	while (number > 0)
	{
		int digits = number%10;
   		number /= 10;
		product *= mappings[digits];	
	}
	
	return product;
}

int main()
{
	bool found = false;
	unsigned int i = 1;
	
	while(found == false)
	{
		if(i % 10000 == 0)
		{
			std::cout << "\r" << std::flush;
			std::cout << i; 
		}
		unsigned int x = primed_product(i);
		if(primed_product(2*i) == x && primed_product(3*i) == x && primed_product(4*i) == x && primed_product(5*i) == x && primed_product(6*i) == x)
		{
			std::cout << "\r" << std::flush;
			std::cout << i << std::endl;
			found = true;
		}
		
		i++;
	}

	return 0;
}
