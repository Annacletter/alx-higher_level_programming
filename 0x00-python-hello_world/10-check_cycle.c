#include "lists.h"

/**
* check_cycle - Program that checks if singly linked list has a cycle in it
* @list: list to check
* Return: Always 0
*/

int check_cycle(listint_t *list)
{
	listint_t *first, *second;
	first = second = list;

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
		{
			first = list;
			while (first != NULL && second != NULL)
			{
				if (first == second)
					return (1);
				first = first->next;
				second = second->next;
			}
		}
	}
	return (0);
}
