#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the first element in the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t **n_stck = NULL, **tmp = NULL, *node = NULL;
	int i = 0, j = 0, st_size = 0;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	node = *head;
	while (node != NULL)
	{
		st_size += sizeof(listint_t *);
		tmp = malloc(st_size);
		if (tmp == NULL)
			return (0);
		for (i = 0; i + 1 < (int)(st_size / sizeof(listint_t *)); i++)
			tmp[i] = n_stck[i];
		if (n_stck != NULL)
			free(n_stck);
		n_stck = tmp;
		n_stck[j] = node;
		node = node->next;
		j = j + 1;
	}
	i = 0;
	--j;
	while (i < j)
	{
		if (n_stck[i++]->n != n_stck[j--]->n)
			return (0);
	}
	free(n_stck);
	return (1);
}
