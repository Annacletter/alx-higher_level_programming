#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * Description: Program prints singly linked list node structure
 * @number: prints an integer
 * @next: this points to the next node
 * @number: prints an integer
 */



size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;
#endif
