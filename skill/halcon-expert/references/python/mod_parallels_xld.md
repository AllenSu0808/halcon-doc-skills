# mod_parallels_xld (Operator)

## Name

`mod_parallels_xld` — Extract parallel XLD polygons enclosing a homogeneous area.

## Signature

`def mod_parallels_xld(parallels: HObject, image: HObject, quality: Union[float, int], min_gray: int, max_gray: int, max_standard: Union[float, int]) -> Tuple[HObject, HObject]`

## Description

`mod_parallels_xld` selects XLD parallels enclosing
homogeneous areas from the input parallels *`parallels`*.
The parameter *`image`* contains the corresponding gray value
image.

Only parallels having a quality factor larger than
*`quality`* are examined. The algorithm performs parallel
cross sections one pixel apart, and parallel to the line segments in
the area of overlap between two parallel line segments.

In the first iteration, the mean gray value for each of the lines in
the cross section is calculated. In the second iteration, the
standard deviations of the gray values along each line are computed.

If the mean gray value of an area between parallels lies in the
interval [*`min_gray`*,*`max_gray`*], and if the mean of
all standard deviations is smaller than the upper threshold
*`max_standard`*, the corresponding parallels are returned as
modified parallels in *`mod_parallels`*.

In a second step, all polygon segments adjacent to parallels
bordering homogeneous areas are checked for homogeneity. To do so,
a rectangle having the width of the last area enclosed by a
modified parallel is constructed, and checked for homogeneity using
the algorithm described above. This process is continued as long as
there are adjacent polygon segments. The polygons thus found are
returned as extended parallels in *`ext_parallels`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`parallels`** (input_object)  xld_para-array `→` HObject

Input XLD parallels.

**`image`** (input_object)  singlechannelimage `→` HObject (byte)

Corresponding gray value image.

**`mod_parallels`** (output_object)  xld_mod_para-array `→` HObject

Modified XLD parallels.

**`ext_parallels`** (output_object)  xld_ext_para-array `→` HObject

Extended XLD parallels.

**`quality`** (input_control)  number `→` Union[float, int]

Minimum quality factor (measure of parallelism).

Default:
0.4

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.6

Restriction:
`0.0 <= Quality && Quality <= 1.0`

**`min_gray`** (input_control)  integer `→` int

Minimum mean gray value.

Default:
160

Suggested values:
80, 100, 120, 140, 160, 180

Restriction:
`0 <= MinGray && MinGray <= 255`

**`max_gray`** (input_control)  integer `→` int

Maximum mean gray value.

Default:
220

Suggested values:
140, 160, 180, 200, 220, 240

Restriction:
`0 <= MaxGray && MaxGray <= 255 && MaxGray >= MinGray`

**`max_standard`** (input_control)  number `→` Union[float, int]

Maximum allowed standard deviation.

Default:
10.0

Suggested values:
5.0, 10.0, 15.0, 20.0

Restriction:
`MaxStandard >= 0.0`

## Possible Predecessors

`gen_parallels_xld`

## Possible Successors

`max_parallels_xld`

## See also

`info_parallels_xld`

## Module

Foundation
