#include <iostream>
#include <math.h>     
#include <algorithm>
#include<vector>
using namespace std;

namespace test {

	int SubstractTen(int item)
	{
		return item - 10;
	}
	int Square(int item)
	{
		return pow(item, 2);
	}
	int AddOne(int item)
	{
		return item + 1;
	}
}
int main()
{
	vector<int> mydata = { 7, 4, 5, 6, 3, 8, 10 };
	vector<int> output ;
  
	//--------------------imperative--------------------------
	for (int item : mydata)
	{
		double val = test::SubstractTen(test::Square(test::AddOne(item)));
		//cout << val << endl;
	}
	//--------------------declerative-------------------------

	//back_inserter call push back
	transform(mydata.begin(), mydata.end(), back_inserter(output),test::AddOne);
	transform(output.begin(), output.end(), output.begin(), test::Square);
	transform(output.begin(), output.end(), output.begin(), test::SubstractTen);
	for (auto item : output)
	{
		//cout << item << endl;
	}

	//dd one then square then select only x <20 to pass it to the last step (SubstractTen)

	transform(mydata.begin(), mydata.end(), back_inserter(output), test::AddOne);
	transform(output.begin(), output.end(), output.begin(), test::Square);
	auto is_less_20 = [](int& value) {
		if (value > 20)
			return true;
		return false;
	};
	output.erase(remove_if(output.begin(), output.end(), is_less_20),output.end());
	transform(output.begin(), output.end(), output.begin(), test::SubstractTen);

	for (auto item : output)
	{
		//cout << item << endl;
	}

	//add one then square then select only x < 70 and only take two and pass it to the last step(SubstractTen)
  
	transform(mydata.begin(), mydata.end(), back_inserter(output), test::AddOne);
	transform(output.begin(), output.end(), output.begin(), test::Square);
	auto is_less_70 = [](int& value) {
		if (value > 70)
			return true;
		return false;
	};
	output.erase(remove_if(output.begin(), output.end(), is_less_70), output.end());
	sort(output.begin(), output.end());
	output.erase(output.begin()+2, output.end());
	transform(output.begin(), output.end(), output.begin(), test::SubstractTen);

	for (auto item : output)
	{
		//cout << item << endl;
	}

	return 0;
}
