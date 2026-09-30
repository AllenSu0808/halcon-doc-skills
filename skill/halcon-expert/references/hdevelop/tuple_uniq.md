# tuple_uniq (Operator)

## Name

`tuple_uniq` — Discard all but one of successive identical elements of a tuple.

## Signature

`tuple_uniq( : : Tuple : Uniq)`

## Description

`tuple_uniq` discards all but one of successive identical
elements from the input tuple *`Tuple`* and returns the
remaining elements in *`Uniq`*.
For example, if *`Tuple`* contains the values
[0,0,1,1,1,2,0,1], the output tuple *`Uniq`* will contain
the values [0,1,2,0,1]. It is allowed to mix strings and numbers in the
input tuple.

To get a tuple *`Uniq`* that contains all different entries of
*`Tuple`* exactly once, use the operator [`tuple_sort`](tuple_sort.md) first. Note
however that in this case the output tuple *`Uniq`* is sorted.
The result of the above example then is [0,1,2].

### Exception: Empty input tuple

If the input tuple is empty, the operator returns an empty tuple.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_uniq`,
which can be used in an expression in the following syntax:

[`Uniq := uniq(Tuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

As mentioned above, you can use [`tuple_sort`](tuple_sort.md) to truly get all
unique elements of *`Tuple`*.

[`Uniq := uniq(sort(Tuple))`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Uniq`** (output_control)  tuple(-array) `→`  (integer / real / string)

Tuple without successive identical elements.

## Example (HDevelop)

```
Tuple := [0,0,1,1,1,2,0,1]
*
tuple_uniq (Tuple, Uniq)
*
tuple_sort (Uniq, Sorted)
tuple_uniq (Sorted, Uniq1)
```

## Possible Predecessors

`tuple_inverse`,
`tuple_sort`

## Alternatives

`tuple_intersection`

## Module

Foundation
