#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
  *check_cycle - check if a cycle occurs
  *list: head pointer
  *
  *Return: 1 or 0
  */
int check_cycle(listint_t *list)
{
	listint_t *temp_slow = list;
	listint_t *temp_fast = list;
	while(temp_slow != NULL && temp_fast != NULL && temp_fast->next != NULL)
	{
		temp_fast = temp_fast->next;
		temp_fast = temp_fast->next;
		if (temp_slow == temp_fast)
			return (1);
		temp_slow = temp_slow->next;
	}
	return (0);
} 
