# ObjToInteger (Operator)

## Name

`ObjToInteger` — Convert an iconic object into an “integer number.”

## Signature

`static void HOperatorSet.ObjToInteger(HObject objects, HTuple index, HTuple number, out HTuple surrogateTuple)`

`HTuple HObject.ObjToInteger(int index, int number)`

## Description

`ObjToInteger` stores *`number`*, starting at index
*`index`*, of the database keys of the input object
*`objects`* as integer numbers in the output parameter
*`surrogateTuple`*. If -1 is passed for *`number`* all
objects beginning with *`index`* are copied. This facilitates
a direct access to an arbitrary element of *`objects`*. In
conjunction with [`CountObj`](count_obj.md) (returns the number of objects in
*`objects`*) the elements of *`objects`* can be processed
successively. The objects are not duplicated by
`ObjToInteger` and thus must not be cleared by
[`ClearObj`](clear_obj.md).

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

**`objects`** (input_object)  object(-array) `→` [HObject](HObject.md)

Objects for which the surrogates are to be returned.

**`index`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Starting index of the surrogates to be returned.

Default:
1

Value range:
`1
≤
index`

**`number`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of surrogates to be returned.

Default:
-1

Restriction:
`Number == -1 || Number + Index <= number(Objects)`

**`surrogateTuple`** (output_control)  pointer(-array) `→` [HTuple](HTuple.md) (*IntPtr*)

Tuple containing the surrogates.

## Example (HDevelop)

```
* Access the i-th element:
obj_to_integer(Objects,i,1,Surrogat)
```

## Complexity

Runtime complexity: O(|*`objects`*| + *`number`*)

## Result

`ObjToInteger` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Alternatives

`CopyObj`,
`SelectObj`,
`CopyImage`,
`GenImageProto`

## See also

`IntegerToObj`,
`CountObj`

## Module

Foundation
