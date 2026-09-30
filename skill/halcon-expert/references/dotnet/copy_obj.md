# CopyObj (Operator)

## Name

`CopyObj` — Copy an iconic object in the HALCON database.

## Signature

`static void HOperatorSet.CopyObj(HObject objects, out HObject objectsSelected, HTuple index, HTuple numObj)`

`HObject HObject.CopyObj(int index, int numObj)`

`HImage HImage.CopyObj(int index, int numObj)`

`HRegion HRegion.CopyObj(int index, int numObj)`

`HXLD HXLD.CopyObj(int index, int numObj)`

`HXLDCont HXLDCont.CopyObj(int index, int numObj)`

`HXLDPoly HXLDPoly.CopyObj(int index, int numObj)`

`HXLDPara HXLDPara.CopyObj(int index, int numObj)`

`HXLDModPara HXLDModPara.CopyObj(int index, int numObj)`

`HXLDExtPara HXLDExtPara.CopyObj(int index, int numObj)`

## Description

`CopyObj` copies *`numObj`* iconic objects
beginning with index *`index`* (starting with 1) from the
iconic input object tuple *`objects`* to the output object
*`objectsSelected`*. If -1 is passed for *`numObj`*
all objects beginning with *`index`* are copied. No new
storage is allocated for the regions and images. Instead, new
objects containing references to the existing objects are created.
The number of objects in an object tuple can be queried with the
operator [`CountObj`](count_obj.md).

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (input_object)  object(-array) `→` [HObject](HObject.md)

Objects to be copied.

**`objectsSelected`** (output_object)  object(-array) `→` [HObject](HObject.md)

Copied objects.

**`index`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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

**`numObj`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of objects to be copied or -1.

Default:
1

Suggested values:
-1, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000

Value range:
`-1
≤
numObj`

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

Runtime complexity: O(|*`objects`*| + *`numObj`*);

Memory complexity of the result object: O(*`numObj`*)

## Result

`CopyObj` returns 2 (
H_MSG_TRUE)
if all objects are contained in
the HALCON database and all parameters are correct. If the input
is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`CountObj`

## Alternatives

`SelectObj`

## See also

`CountObj`,
`ConcatObj`,
`ObjToInteger`,
`CopyImage`

## Module

Foundation
