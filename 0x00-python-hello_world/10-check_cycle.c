#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - a function that a linked list is present
 * @list: A singly linked list
 *
 * Return: 0 if link is absent, 1 is link is present
 */


int check_cycle(listint_t  *list)
{
	listint_t *fastlane, *slowlane;

	/* check for NULL*/
	if (list == NULL || list->next == NULL)
		return (0);
	slowlane = list->next;
	fastlane = list->next->next;

	while (slowlane && fastlane && fastlane->next)
	{
		if (slowlane == fastlane)
			return (1);

		slowlane = slowlane->next;
		fastlane = fastlane->next->next;
	}

	return (0);
}
