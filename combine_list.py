def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  new_list = list2.extend(list1.reverse())
  return new_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"] # Reverse Order
Drews_list = ["Mike", "Carol", "Greg", "Marcia"] # First

print(combine_lists(Jamies_list, Drews_list))
