# select_obj (Operator)

## Name

`select_obj` — Select objects from an object tuple.

## Signature

`select_obj(Objects : ObjectSelected : Index : )`

## Description

`select_obj` copies the iconic objects with the indices given
by *`Index`* (starting with 1) from the iconic input object
tuple *`Objects`* to the output object *`ObjectSelected`*.
No new storage is allocated for the regions and images. Instead,
new objects containing references to the existing objects are
created. The number of objects in an object tuple can be queried
with the operator [`count_obj`](count_obj.md).

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Objects`** (input_object)  object(-array) `→` object

Input objects.

**`ObjectSelected`** (output_object)  object(-array) `→` object

Selected objects.

**`Index`** (input_control)  integer(-array) `→`  (integer)

Indices of the objects to be selected.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 100, 200, 500, 1000, 2000, 5000

Restriction:
`Index >= 1`

## Example (C)

```
/* Access to all Regions */

count_obj(Regions,&Num);
for (i=1; i<=Num; i++)
{
  select_obj(Regions,&Single,i);
  T_get_region_polygon(Single,5.0,&Row,&Column);
  T_disp_polygon(WindowHandleTuple,Row,Column);
  destroy_tuple(Row);
  destroy_tuple(Column);
}
```

## Complexity

Runtime complexity: O(|*`Objects`*|)

## Result

`select_obj` returns 2 (
H_MSG_TRUE)
if all objects are contained in
the HALCON database and all parameters are correct. If the input
is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`count_obj`

## Alternatives

`copy_obj`

## See also

`count_obj`,
`concat_obj`,
`obj_to_integer`

## Module

Foundation
