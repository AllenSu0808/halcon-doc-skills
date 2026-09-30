# obj_to_integer (Operator)

## Name

`obj_to_integer` — Convert an iconic object into an “integer number.”

## Signature

`obj_to_integer(Objects : : Index, Number : SurrogateTuple)`

## Description

`obj_to_integer` stores *`Number`*, starting at index
*`Index`*, of the database keys of the input object
*`Objects`* as integer numbers in the output parameter
*`SurrogateTuple`*. If -1 is passed for *`Number`* all
objects beginning with *`Index`* are copied. This facilitates
a direct access to an arbitrary element of *`Objects`*. In
conjunction with [`count_obj`](count_obj.md) (returns the number of objects in
*`Objects`*) the elements of *`Objects`* can be processed
successively. The objects are not duplicated by
`obj_to_integer` and thus must not be cleared by
[`clear_obj`](clear_obj.md).

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Attention

The objects' data is not duplicated.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Objects`** (input_object)  object(-array) `→` object

Objects for which the surrogates are to be returned.

**`Index`** (input_control)  integer `→`  (integer)

Starting index of the surrogates to be returned.

Default:
1

Value range:
`1
≤
Index`

**`Number`** (input_control)  integer `→`  (integer)

Number of surrogates to be returned.

Default:
-1

Restriction:
`Number == -1 || Number + Index <= number(Objects)`

**`SurrogateTuple`** (output_control)  pointer(-array) `→`  (integer)

Tuple containing the surrogates.

## Example (HDevelop)

```
* Access the i-th element:
obj_to_integer(Objects,i,1,Surrogat)
```

## Complexity

Runtime complexity: O(|*`Objects`*| + *`Number`*)

## Result

`obj_to_integer` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Alternatives

`copy_obj`,
`select_obj`,
`copy_image`,
`gen_image_proto`

## See also

`integer_to_obj`,
`count_obj`

## Module

Foundation
