#include "lists.h"
#include <stdio.h>

/*
* insert_node - insert node into a sorted linked list
* @head: pointer to the linked list
* @number: number to the inserted
*
* Description: insert a node into a sorted linked list
*
* Return: address of new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	if (current->n > number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}


	while (current->next != NULL)
	{
		if (current->next->n > number)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		if (current->next->next == NULL)
		{
			new_node->next = NULL;
			current->next->next = new_node;
			return (new_node);
		}
		current = current->next;
	}
	return (*head);
}
