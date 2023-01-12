/*
Day 57 coding Statement : C++ Program to Store Information of a Student in a Structure

This program stores the information (name, roll and marks entered by the user) of a student 
in a structure and displays it on the screen.
*/

#include <iostream>
using namespace std;
struct student {
   int rollNo;
   char name[50];
   float marks;
   char grade;
};
int main() {
   struct student s = { 12 , "Harry" , 90 , 'A' };
   cout<<"The student information is given as follows:"<<endl;
   cout<<endl;
   cout<<"Roll Number: "<<s.rollNo<<endl;
   cout<<"Name: "<<s.name<<endl;
   cout<<"Marks: "<<s.marks<<endl;
   cout<<"Grade: "<<s.grade<<endl;
   return 0;
}