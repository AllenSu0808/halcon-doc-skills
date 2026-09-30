# find_caltab (Operator)

## Name

`find_caltab` — Segment the region of a standard calibration plate with rectangularly
arranged marks in the image.

## Signature

`find_caltab(Image : CalPlate : CalPlateDescr, SizeGauss, MarkThresh, MinDiamMarks : )`

## Description

`find_caltab` is used to determine the region of a plane
calibration plate with circular marks in the input image
*`Image`*. The region must correspond to a standard calibration plate
with rectangularly arranged marks described in the file
*`CalPlateDescr`*. The successfully segmented
region is returned in *`CalPlate`*. The operator provides two algorithms.
By setting appropriate integer values in *`SizeGauss`*,
*`MarkThresh`*, and *`MinDiamMarks`*, respectively, you invoke
the *standard algorithm*. If you pass a tuple of parameter names in
*`SizeGauss`* and a corresponding tuple of parameter values in
*`MarkThresh`*, or just two empty tuples, respectively, you invoke the
*advanced algorithm* instead. In this case the value passed in
*`MinDiamMarks`* is ignored.

### Standard algorithm

First, the input image is smoothed (see [`gauss_image`](gauss_image.md)); the size of
the used filter mask is given by *`SizeGauss`*. Afterwards, a
threshold operator (see [`threshold`](threshold.md)) with a minimum gray value
*`MarkThresh`* is applied. Among the extracted connected regions
the most convex region with an almost correct number of holes (corresponding
to the dark marks of the calibration plate) is selected. Holes with a
diameter smaller than the expected size of the marks
*`MinDiamMarks`* are eliminated to reduce the impact of noise.
The number of marks is read from the calibration plate description
file *`CalPlateDescr`*. The complete explanation of this file
can be found within the description of [`gen_caltab`](gen_caltab.md).

### Advanced algorithm

First, an image pyramid based on *`Image`* is built. Starting from the
highest pyramid level, round regions are segmented with a dynamic threshold.
Then, they are associated in groups based on their mutual proximity and
it is evaluated whether they can represent marks of a potential
calibration plate. The search is terminated once the expected number of
marks has been identified in one group. The surrounding lighter area
is returned in *`CalPlate`*.

The image pyramid makes the search independent from the size of the image
and the marks. The dynamic threshold makes the algorithm immune to bad or
irregular illumination. Therefore, in general, no parameter is required.
Yet, you can adjust some auxiliary parameters of the advanced algorithm
by passing a list of parameter names (strings) to *`SizeGauss`* and
a list of corresponding parameter values to *`MarkThresh`*. Currently
the following parameter is supported:

- ***'gap_tolerance'*:** —

  Tolerance factor for gaps between the marks. If the marks appear
  closer to each other than expected, you might set
  *'gap_tolerance'* < *1.0* to avoid disturbing patterns
  outside the calibration plate to be associated with the calibration
  plate. This can typically happen if the plate is strongly tilted and
  positioned in front of a background that exposes mark-like patterns.
  If the distances between single marks deviate significantly, e.g., if
  the calibration plate appears with strong perspective distortion in the
  image, you might set *'gap_tolerance'* > *1.0* to enforce
  the grouping for the more distant marks.

  Suggested values:
   *0.75*, *0.9*,
  *1.0*, *1.1*,
  *1.2*, *1.5*

  Default:
   *1.0*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2)

Input image.

**`CalPlate`** (output_object)  region `→` object

Output region.

**`CalPlateDescr`** (input_control)  filename.read `→`  (string)

File name of the calibration plate description.

Default:
'caltab_100.descr'

List of values:
'caltab_100mm.descr', 'caltab_10mm.descr', 'caltab_200mm.descr', 'caltab_2500um.descr', 'caltab_30mm.descr', 'caltab_650um.descr', 'caltab_6mm.descr', 'caltab_800mm.descr', 'caltab_big.descr', 'caltab_small.descr'

File extension:
.`descr`

**`SizeGauss`** (input_control)  integer(-array) `→`  (integer / string)

Filter size of the Gaussian.

Default:
3

List of values:
0, 3, 5, 7, 9, 11, 'gap_tolerance'

**`MarkThresh`** (input_control)  integer(-array) `→`  (integer / real)

Threshold value for mark extraction.

Default:
112

Suggested values:
48, 64, 80, 96, 112, 128, 144, 160, 0.5, 0.9, 1.0, 1.1, 1.5

**`MinDiamMarks`** (input_control)  integer `→`  (integer)

Expected minimal diameter of the marks on the calibration
plate.

Default:
5

Suggested values:
3, 5, 9, 15, 30, 50, 70

## Example (HDevelop)

```
* Read calibration image.
read_image(Image, 'calib/calib_distorted_01')
* Find calibration pattern.
find_caltab(Image, CalPlate, 'caltab_100mm.descr', 3, 112, 5)
```

## Result

`find_caltab` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and an image region is found. The behavior in case
of empty input (no image given) can be set via
`set_system(::'no_object_result',<Result>:)`
and the behavior in case of an empty result region via
`set_system(::'store_empty_region',<'true'/'false'>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`read_image`

## Possible Successors

`find_marks_and_pose`

## See also

`find_marks_and_pose`,
`camera_calibration`,
`disp_caltab`,
`sim_caltab`,
`caltab_points`,
`gen_caltab`

## Module

Foundation
