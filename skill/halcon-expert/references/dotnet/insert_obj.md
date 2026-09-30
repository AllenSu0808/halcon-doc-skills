# InsertObj (Operator)

## Name

`InsertObj` — Insert objects into an iconic object tuple.

## Signature

`static void HOperatorSet.InsertObj(HObject objects, HObject objectsInsert, out HObject objectsExtended, HTuple index)`

`HObject HObject.InsertObj(HObject objectsInsert, int index)`

`HImage HImage.InsertObj(HImage objectsInsert, int index)`

`HRegion HRegion.InsertObj(HRegion objectsInsert, int index)`

`HXLD HXLD.InsertObj(HXLD objectsInsert, int index)`

`HXLDCont HXLDCont.InsertObj(HXLDCont objectsInsert, int index)`

`HXLDPoly HXLDPoly.InsertObj(HXLDPoly objectsInsert, int index)`

`HXLDPara HXLDPara.InsertObj(HXLDPara objectsInsert, int index)`

`HXLDModPara HXLDModPara.InsertObj(HXLDModPara objectsInsert, int index)`

`HXLDExtPara HXLDExtPara.InsertObj(HXLDExtPara objectsInsert, int index)`

## Description

`InsertObj` inserts the elements of *`objectsInsert`* at
*`index`* into the object tuple *`objects`* and returns the
result in *`objectsExtended`*.

*`index`* must contain a single integer value. Note that, in contrast
to control tuples, indices of object tuple elements start at 1. The length
of *`objectsExtended`* is the sum of the length of *`objects`*
and *`objectsInsert`*.
It is allowed to mix images, regions and XLDs in *`objects`* and
*`objectsInsert`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` [HObject](HObject.md)

Input object tuple.

**`objectsInsert`** (input_object)  object(-array) `→` [HObject](HObject.md)

Object tuple to insert.

**`objectsExtended`** (output_object)  object(-array) `→` [HObject](HObject.md)

Extended object tuple.

**`index`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index to insert objects.

## Example (HDevelop)

```
gen_image_const (Image1, 'byte', 1, 1)
gen_image_const (Image3, 'byte', 3, 3)
concat_obj (Image1, Image3, Images)
gen_image_const (Image, 'byte', 2, 2)
insert_obj (Images, Image, Images, 2)
```

## Complexity

Typical runtime complexity: O(|*`objects`*| + |*`objectsInsert`*|).

## Possible Predecessors

`CountObj`

## Possible Successors

`CountObj`

## Alternatives

`ConcatObj`

## See also

`CountObj`,
`SelectObj`,
`CopyObj`,
`RemoveObj`

## Module

Foundation
