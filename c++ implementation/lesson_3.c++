#include <iostream>
#include <math.h>     
#include <algorithm>
#include<vector>
#include <tuple>

using namespace std;

namespace test {

	class Order {
	public:
		int OrderID;
		int ProductIndex;
		double Quantity;
		double UnitPrice;
    
		Order(int orderod,int productindex,double quantity,double unitprice)
		{
			OrderID = orderod;
			ProductIndex = productindex;
			Quantity = quantity;
			UnitPrice = unitprice;
		}


	};
	enum ProductType
	{
		Food ,
		Beverage,
		RawMaterial

	};
	double Test1(double x)
	{
		return x / 2;
	}

	double Test2(double x)
	{
		return x / 4 + 1;
	}

	double Test3(double(*ptr)(double), double Value)
	{
		return ptr(Value) + Value;
	}

	tuple<double,double > ProductParamtersFood(double ProductIndex)
	{
		return make_tuple(ProductIndex/ (ProductIndex+100), ProductIndex/(ProductIndex+300));
	}
	tuple<double, double > ProductParamtersBeverage(double ProductIndex)
	{
		return make_tuple(ProductIndex / (ProductIndex + 300), ProductIndex / (ProductIndex + 400));
	}
	tuple<double, double > ProductParamtersRawMaterial(double ProductIndex)
	{
		return make_tuple(ProductIndex / (ProductIndex + 400), ProductIndex / (ProductIndex + 700));
	}

	double ClaculateDiscount(tuple<double, double >(*ptr)(double), Order r)
	{
		double x1, x2;
		tie(x1,x2) = ptr(r.ProductIndex);
		return x1 * r.Quantity + x2 * r.UnitPrice;

	}

}
using namespace test;
int main()
{
	vector<double (*)(double)> tt;

	double (*dlgtTest1)(double);
	double (*dlgtTest2)(double);
	dlgtTest1 = &Test1;
	dlgtTest2 = &Test2;

	tt.push_back(dlgtTest1);
	tt.push_back(dlgtTest2);

	cout << Test2(Test1(5)) << endl;
	cout << Test1(Test2(5)) << endl;

	cout << Test3(Test1, 5) << endl;
	cout << Test3(Test2, 5) << endl;
	
	cout <<(*tt[0])(5) << endl;
	cout << (*tt[1])(5) << endl;

	tuple<double,double> (*A)(double);
	tuple<double, double>(*B)(double);
	tuple<double, double>(*C)(double);

	A = &ProductParamtersFood;
	B = &ProductParamtersBeverage;
	C = &ProductParamtersRawMaterial;
	Order o = Order(10, 100, 20, 4);
	ProductType product;
	product = Food;
		

	tuple<double, double>(*p)(double);
	p = ((product==Food) ?A :((product==Beverage)?B :C));

	double discount = ClaculateDiscount(p, o);
	cout << discount << endl;
	

	return 0;
}

