/*!
 *  \file   endian.c
 *  \brief  determine what the endian is for your computer.
 *  \author Frederique Hsu (frederique.hsu@outlook.com)
 *  \date   Sat.    08 Jan. 2022
 *  
 */

#include <stdio.h>

int main(int argc, char* argv[])
{
    printf("Current program is %ld-bits.\n", sizeof(void*) * 8);
    unsigned int data = 0x158CB2F8;

    unsigned char *endian = (unsigned char*)&data;

    printf("*endian is: 0x%X\n\n", *endian);
    
    printf("data's value = 0x%08X\n", data);
    printf("data's address in memory = 0x%016llX\n\n", (unsigned long long)&data);
    printf("value | address   \n");

    for (size_t index = 0; index < sizeof(data); ++index)
    {
        printf("------+--------------------\n");
        printf("%02X    | 0x%016llX \n", *(endian+index), (unsigned long long)(endian+index));
    }

    printf("\n");
    if ((*endian) == (data & 0x000000FF))
    {
        printf("Current architecture is little-endian.\n");
    }
    else if ((*endian) == ((data & 0xFF000000) >> 24))
    {
        printf("Current architecture is big-endian.\n");
    }

    printf("\n");
    return 0;
}