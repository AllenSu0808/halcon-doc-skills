# copy_obj (Operator)

## Name

`copy_obj` — Copy an iconic object in the HALCON database.

## Signature

`def copy_obj(objects: HObject, index: int, num_obj: int) -> HObject`

## Description

`copy_obj` copies *`num_obj`* iconic objects
beginning with index *`index`* (starting with 1) from the
iconic input object tuple *`objects`* to the output object
*`objects_selected`*. If -1 is passed for *`num_obj`*
all objects beginning with *`index`* are copied. No new
storage is allocated for the regions and images. Instead, new
objects containing references to the existing objects are created.
The number of objects in an object tuple can be queried with the
operator [`count_obj`](count_obj.md).

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` HObject

Objects to be copied.

**`objects_selected`** (output_object)  object(-array) `→` HObject

Copied objects.

**`index`** (input_control)  integer `→` int

Starting index of the objects to be copied.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000

Value range:
`1
≤
index`

Restriction:
`Index <= number(Objects)`

**`num_obj`** (input_control)  integer `→` int

Number of objects to be copied or -1.

Default:
1

Suggested values:
-1, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000

Value range:
`-1
≤
num_obj`

Restriction:
`NumObj + Index - 1 <= number(Objects) && NumObj != 0`

## Complexity

Runtime complexity: O(|*`objects`*| + *`num_obj`*);

Memory complexity of the result object: O(*`num_obj`*)

## Result

`copy_obj` returns 2 (
H_MSG_TRUE)
if all objects are contained in
the HALCON database and all parameters are correct. If the input
is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`count_obj`

## Alternatives

`select_obj`

## See also

`count_obj`,
`concat_obj`,
`obj_to_integer`,
`copy_image`

## Module

Foundation
