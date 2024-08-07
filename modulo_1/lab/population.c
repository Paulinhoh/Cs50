#include <stdio.h>

int main(void)
{
    int start, end, population, death, years = 0;
    do
    {
        printf("Start Size: ");
        scanf("%i", &start);
    } while (start < 9);

    do
    {
        printf("End Size: ");
        scanf("%i", &end);
    } while (end < start);

    while (start < end)
    {
        population = (start / 3) - (start / 4);
        start = start + population;
        years++;
    }

    printf("Years: %i", years);
}