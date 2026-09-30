# shape_histo_all (Operator)

## Name

`shape_histo_all` — Determine a histogram of features along all threshold values.

## Signature

`shape_histo_all(Region, Image : : Feature : AbsoluteHisto, RelativeHisto)`

## Description

The operator `shape_histo_all` carries out 255 threshold
operations within *`Region`* with the gray values of
*`Image`*. The entry i in the histogram corresponds to the
number of connected components/holes of this image segmented with
the threshold i (*`Feature`* =
*'connected_components'*, *'holes'*) or the mean
value of the feature values of the regions segmented in this way
(*`Feature`* = *'convexity'*, *'compactness'*,
*'anisometry'*), respectively.

## Attention

The operator `shape_histo_all` expects a region and exactly
one gray value image as input. Because of the power of this
operator the runtime of `shape_histo_all` is relatively large!

Note that the operator `shape_histo_all` only considers
the given *`Region`* and ignores any previously set domain
of the input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region `→` object

Region in which the features are to be examined.

**`Image`** (input_object)  singlechannelimage `→` object (byte)

Gray value image.

**`Feature`** (input_control)  string `→`  (string)

Feature to be examined.

Default:
'connected_components'

List of values:
'anisometry', 'compactness', 'connected_components', 'convexity', 'holes'

**`AbsoluteHisto`** (output_control)  histogram-array `→`  (real / integer)

Absolute distribution of the feature.

**`RelativeHisto`** (output_control)  histogram-array `→`  (real)

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

The operator `shape_histo_all` returns the value 2 (
H_MSG_TRUE)
if an
image with the defined gray values is entered. The behavior in case
of empty input (no input images) is set via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`histo_to_thresh`,
`threshold`,
`gen_region_histo`

## Alternatives

`shape_histo_point`

## See also

`compactness`,
`connection`,
`connect_and_holes`,
`convexity`,
`count_obj`,
`entropy_gray`,
`gray_histo`

## Module

Foundation
