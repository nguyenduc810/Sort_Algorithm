#include <iostream>
#include <conio.h>
using namespace std;

void ShellSort (float * arr, int n )
{
    for(int step  =  n/2 ; step > 0 ;step /=2)
    {
        for(int i = step ; i < n ; i++)
        {
            float x = arr[i];
            int v = i - step;
            while (v >= 0 && arr[v] > x)
            {
                arr[ v + step] = arr[v];
                v -= step;
            }
            arr[v + step] = x;
        }
    }
}
void Input(float * a, int n)
{
    for(int i = 0 ; i < n ; i ++)
    {
        cout<<"Arr["<<i<<"] = ";
        cin>>a[i];
    }
}
void Output(float * a, int n)
{
     for(int i = 0 ; i < n ; i ++) cout<<a[i]<<"\t"; 
     cout<<endl;  
}
int main ()
{
    system("cls");
    int n ;
    cout<<"Size of array: ";
    cin>>n;
    float arr[n];
    Input(arr,n);
    cout<<"Truoc khi sap xep: "<<endl;
    Output(arr, n);
    ShellSort(arr, n);
    cout<<"Sau khi sap xep: "<<endl;
    Output(arr, n);
    getch();
}