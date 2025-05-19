The union() method returns a set that contains all items from the original set, and all items from the specified set(s).

You can specify as many sets you want, separated by commas.

It does not have to be a set, it can be any iterable object.

If an item is present in more than one set, the result will contain only one appearance of this item.

As a shortcut, you can use the | operator instead, see example below.

Syntax
set.union(set1, set2...)
Parameter Values
Parameter	Description
set1	Required. The iterable to unify with
set2	Optional. The other iterable to unify with.
You can compare as many iterables as you like.
Separate each iterable with a comma
Shorter Syntax
set | set1 | set2 ...
Parameter Values
Parameter	Description
set1	Required. The iterable to unify with
set2	Optional. The other iterable to unify with.
You can compare as many iterables as you like.
Separate each iterable with | (a pipe operator).
See examples below.
