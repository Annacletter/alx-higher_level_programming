#include "lists.h"
#include <stdlib.h>

/**
* palindrome - Helps and verify the palindrome list
* @head: head of the list
* @temp: bottom of the list
* @length: length of the list
* Return: Always 0.
*/

int palindrome(listint_t *head, listint_t *temp, int len)
{
	listint_t *help = head;
	int i = 0;

	if (len <= 1)
		return (1);
	else if (head->n == temp->n)
	{
		while (i < len - 2)
		{
			help = help->next;
			i++;
		}
		return (palindrome(head->next, help, len - 2));
	}
	else
		return (0);
}

/**
* length_of_list - Shows the length of the list
* @head: head of the list
* Return: Always 0.
*/

int length_of_list(listint_t *head)
{
	int len = 0;

	while (head != NULL)
	{
		head = head->next;
		len++;
	}
	return (len);
}

/**
* last_number - Gets the number of the list on the last index
* @head: head of the list
* @length: length of the list
* Return: Always 0.
*/

int last_number(listint_t *head, int len)
{
	int i = 0;

	while (i < len - 1)
	{
		head = head->next;
		i++;
	}
	return (head->n);
}
/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: head of the list.
* Return: Always 0.
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int len = 0, i = 0;

	if (head == NULL)
		return (1);

	temp = *head;
	len = length_of_list(temp);
	while (i < len - 1)
	{
		temp = temp->next;
		i++;
	}
	return (palindrome(*head, temp, len));
}
