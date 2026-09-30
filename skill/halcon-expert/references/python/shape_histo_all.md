# shape_histo_all (Operator)

## Name

`shape_histo_all` — Determine a histogram of features along all threshold values.

## Signature

`def shape_histo_all(region: HObject, image: HObject, feature: str) -> Tuple[Sequence[Union[int, float]], Sequence[float]]`

## Description

The operator `shape_histo_all` carries out 255 threshold
operations within *`region`* with the gray values of
*`image`*. The entry i in the histogram corresponds to the
number of connected components/holes of this image segmented with
the threshold i (*`feature`* =
*"connected_components"*, *"holes"*) or the mean
value of the feature values of the regions segmented in this way
(*`feature`* = *"convexity"*, *"compactness"*,
*"anisometry"*), respectively.

## Attention

The operator `shape_histo_all` expects a region and exactly
one gray value image as input. Because of the power of this
operator the runtime of `shape_histo_all` is relatively large!

Note that the operator `shape_histo_all` only considers
the given *`region`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` HObject

Region in which the features are to be examined.

**`image`** (input_object)  singlechannelimage `→` HObject (byte)

Gray value image.

**`feature`** (input_control)  string `→` str

Feature to be examined.

Default:
"connected_components"

List of values:
"anisometry", "compactness", "connected_components", "convexity", "holes"

**`absolute_histo`** (output_control)  histogram-array `→` Sequence[Union[int, float]]

Absolute distribution of the feature.

**`relative_histo`** (output_control)  histogram-array `→` Sequence[float]

Relative distribution of the feature.

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
