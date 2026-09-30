# obj_to_integer (Operator)

## Name

`obj_to_integer` — Convert an iconic object into an “integer number.”

## Signature

`def obj_to_integer(objects: HObject, index: int, number: int) -> Sequence[int]`

`def obj_to_integer_s(objects: HObject, index: int, number: int) -> int`

## Description

`obj_to_integer` stores *`number`*, starting at index
*`index`*, of the database keys of the input object
*`objects`* as integer numbers in the output parameter
*`surrogate_tuple`*. If -1 is passed for *`number`* all
objects beginning with *`index`* are copied. This facilitates
a direct access to an arbitrary element of *`objects`*. In
conjunction with [`count_obj`](count_obj.md) (returns the number of objects in
*`objects`*) the elements of *`objects`* can be processed
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

**`objects`** (input_object)  object(-array) `→` HObject

Objects for which the surrogates are to be returned.

**`index`** (input_control)  integer `→` int

Starting index of the surrogates to be returned.

Default:
1

Value range:
`1
≤
index`

**`number`** (input_control)  integer `→` int

Number of surrogates to be returned.

Default:
-1

Restriction:
`Number == -1 || Number + Index <= number(Objects)`

**`surrogate_tuple`** (output_control)  pointer(-array) `→` Sequence[int]

Tuple containing the surrogates.

## Complexity

Runtime complexity: O(|*`objects`*| + *`number`*)

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
