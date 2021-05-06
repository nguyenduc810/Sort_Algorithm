#include <iostream>
#include <conio.h>
using namespace std;
#define MAX 1000000

void Merge (float * a,int Left , int Mid , int Right)
{
    float * b = new float[MAX];
    int il  = Left, ir = Mid + 1 , i = Left ;
    while (il <= Mid && ir <= Right)
    {
        if(a[il] <= a[ir])
        {
            b[i] = a[il];
            il++;
            i++;
        }
        else 
        {
            b[i] = a[ir];
            ir++;
            i++;
        }
    }
    if(il > Mid )
        {
            for(int j = ir ; j <= Right ; j ++)
            {
                b[i] = a[j];
                i++;
            }
        }
        else
        {
            for(int j = il ; j <=Mid ; j ++)
            {
                b[i] = a[j];
                i++;
            }
        }
    for(int j = Left ; j <= Right ; j++) a[j] = b[j];
    delete []b;
}

void MergeSort (float * a,int Left , int Right)
{
    if(Left < Right)
    {
        int Mid = (Right + Left)/2;
        MergeSort(a, Left , Mid);
        MergeSort(a ,Mid+1 , Right);
        Merge(a ,Left , Mid , Right);
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
    int n; 
    cout<<"Size of Array: ";
    cin >>n;
    float arr[n];
    Input(arr,n);
    cout<<"Truoc khi sap xep: "<<endl;
    Output(arr, n);
    MergeSort(arr, 0, n-1);
    cout<<"Sau khi sap xep: "<<endl;
    Output(arr, n);
    getch();
}