# ShapeHistoAll (Operator)

## Name

`ShapeHistoAll` — Determine a histogram of features along all threshold values.

## Signature

`static void HOperatorSet.ShapeHistoAll(HObject region, HObject image, HTuple feature, out HTuple absoluteHisto, out HTuple relativeHisto)`

`HTuple HRegion.ShapeHistoAll(HImage image, string feature, out HTuple relativeHisto)`

## Description

The operator `ShapeHistoAll` carries out 255 threshold
operations within *`region`* with the gray values of
*`image`*. The entry i in the histogram corresponds to the
number of connected components/holes of this image segmented with
the threshold i (*`feature`* =
*"connected_components"*, *"holes"*) or the mean
value of the feature values of the regions segmented in this way
(*`feature`* = *"convexity"*, *"compactness"*,
*"anisometry"*), respectively.

## Attention

The operator `ShapeHistoAll` expects a region and exactly
one gray value image as input. Because of the power of this
operator the runtime of `ShapeHistoAll` is relatively large!

Note that the operator `ShapeHistoAll` only considers
the given *`region`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Region in which the features are to be examined.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Gray value image.

**`feature`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Feature to be examined.

Default:
"connected_components"

List of values:
"anisometry", "compactness", "connected_components", "convexity", "holes"

**`absoluteHisto`** (output_control)  histogram-array `→` [HTuple](HTuple.md) (*double* / int / long)

Absolute distribution of the feature.

**`relativeHisto`** (output_control)  histogram-array `→` [HTuple](HTuple.md) (*double*)

Relative distribution of the feature.

## Example (HDevelop)

```
* Simulation of shape_histo_all with feature 'connected_components':
* my_shape_histo_all(Region,Image,AbsHisto,RelHisto):
reduce_domain(Region,Image,RegionGray)
for i := 0 to 255 by 1
    threshold(RegionGray,Seg,i,255)
    connect_and_holes (Seg, NumConnected, _)
    AbsHisto[i] := NumConnected
endfor
Sum := 0
for i := 0 to 255 by 1
    Sum := Sum+AbsHisto[i]
endfor
for i := 0 to 255 by 1
    RelHisto[i] := AbsHisto[i]/Sum
endfor
```

## Complexity

If F is the area of the input region and N the mean number of
connected components the runtime complexity is
$O(255(F + \sqrt{F} \sqrt{N}))$ ![figure](../assets/741f01e10f16176a.svg).

## Result

The operator `ShapeHistoAll` returns the value 2 (
H_MSG_TRUE)
if an
image with the defined gray values is entered. The behavior in case
of empty input (no input images) is set via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`HistoToThresh`,
`Threshold`,
`GenRegionHisto`

## Alternatives

`ShapeHistoPoint`

## See also

`Compactness`,
`Connection`,
`ConnectAndHoles`,
`Convexity`,
`CountObj`,
`EntropyGray`,
`GrayHisto`

## Module

Foundation
