#include <iostream>
#include <conio.h>
using namespace std;
#define MAX 255

int Find_Max(int * a , int n )
{
    int max = a[0];
    for(int i = 1 ; i < n ; i++)
    {
        if(a[i] > max) max = a[i];
    }
    return max;
}

void CountSort (int * a , int n)
{
    int max = Find_Max(a ,n);
    int * b = new int[max+1];
    for(int i = 0 ; i <= max ; i++) b[i] = 0;
    int * c = new int[n];
    for(int i = 0 ; i < n ; i ++)
    {
        b[a[i]] +=1;
    }
    for(int i = 1 ; i <= max ; i ++)
    {
        b[i] += b[i-1];
    }
    for(int i = 0 ; i < n ; i++)
    {
        b[a[i]] -= 1;
        c[b[a[i]]] = a[i];
    }
    for(int i = 0 ;  i < n ; i ++) cout<<c[i]<<"\t";
}
int main ()
{
    system("cls");
    int n ; 
    cout<<"Size of array: ";
    cin>>n;
    int a[n];
    for(int i = 0 ; i < n ; i ++)
    {
        cout<<"Arr["<<i<<"]= ";
        cin>>a[i];
    }
    CountSort(a , n);
}