#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <strings.h>
#include <vector>
#include "git_exec.h"//exec_git_command & exec_git_getsha1

using namespace std;

int main(int argc, char* argv[])
{
//181ed5489bfc64cc0f241f385f1d24f3241cb155
if(argc == 2 && strlen(argv[1]) == 40)
{
    cout <<"#Git commands emulation..." << endl;
    //string S1("git rev-list --min-parents=0 HEAD");

    string S_SHA1(argv[1]);

    vector<string> Vector_SHA1;
    //cout << Vector_SHA1.size() << endl;

    exec_git_getsha1(S_SHA1, &Vector_SHA1);
    //cout << Vector_SHA1.size() << endl;

    for(long long i = 0; i < Vector_SHA1.size(); i++)
    {
            //cout << VS[i] << endl;
            string S_checkout("git checkout ");
            S_checkout += Vector_SHA1[i];
            exec_git_command(S_checkout);
    }
    exec_git_command("git checkout master");

    //exec_git_command("git diff HEAD~1 HEAD");

    cout <<"#Process is over..." << endl;
}
else
    cout << "Exactly one parameter needed - SHA1 of starting commit!" << endl;

    return 0;
}