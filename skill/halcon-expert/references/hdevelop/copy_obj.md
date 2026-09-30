# copy_obj (Operator)

## Name

`copy_obj` — Copy an iconic object in the HALCON database.

## Signature

`copy_obj(Objects : ObjectsSelected : Index, NumObj : )`

## Description

`copy_obj` copies *`NumObj`* iconic objects
beginning with index *`Index`* (starting with 1) from the
iconic input object tuple *`Objects`* to the output object
*`ObjectsSelected`*. If -1 is passed for *`NumObj`*
all objects beginning with *`Index`* are copied. No new
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

**`Objects`** (input_object)  object(-array) `→` object

Objects to be copied.

**`ObjectsSelected`** (output_object)  object(-array) `→` object

Copied objects.

**`Index`** (input_control)  integer `→`  (integer)

Starting index of the objects to be copied.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000

Value range:
`1
≤
Index`

Restriction:
`Index <= number(Objects)`

**`NumObj`** (input_control)  integer `→`  (integer)

Number of objects to be copied or -1.

Default:
1

Suggested values:
-1, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000

Value range:
`-1
≤
NumObj`

Restriction:
`NumObj + Index - 1 <= number(Objects) && NumObj != 0`

## Example (HDevelop)

```
gen_circle (Circles, [100,200,400], [200,100,400], [100,100,50])
copy_obj (Circles, CircleCopy, 2, 3)
erosion_circle (CircleCopy, CircleErosion, 15.5)
dev_set_color ('red')
dev_set_draw ('fill')
dev_display(Circles)
dev_set_color ('white')
dev_set_draw ('margin')
dev_display (CircleCopy)
dev_set_color ('green')
dev_display (CircleErosion)
```

## Complexity

Runtime complexity: O(|*`Objects`*| + *`NumObj`*);

Memory complexity of the result object: O(*`NumObj`*)

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
