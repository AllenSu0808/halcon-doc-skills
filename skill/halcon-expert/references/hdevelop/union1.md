# union1 (Operator)

## Name

`union1` — Return the union of all input regions.

## Signature

`union1(Region : RegionUnion : : )`

## Description

`union1` computes the union of all input regions and
returns the result in *`RegionUnion`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region-array `→` object

Regions of which the union is to be computed.

**`RegionUnion`** (output_object)  region `→` object

Union of all input regions.

Number of elements:
RegionUnion <= Region

## Example (HDevelop)

```
* Union of segmentation results:
threshold(Image,Region1,128,255)
dyn_threshold(Image,Mean,Region2,5,'light')
concat_obj(Region1,Region2,Regions)
union1(Regions,RegionUnion)
```

## Complexity

Let F be the sum of all areas of the input regions. Then the
runtime complexity is O(log(sqrt(F)) * sqrt(F)).

## Result

`union1` always returns 2 (
H_MSG_TRUE)
. The behavior in case of
empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`select_shape`,
`disp_region`

## Alternatives

`union2`

## See also

`intersection`,
`complement`

## Module

Foundation
