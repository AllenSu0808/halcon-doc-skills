# PoseAverage (Operator)

## Name

`PoseAverage` — Compute the average of a set of poses.

## Signature

`static void HOperatorSet.PoseAverage(HTuple poses, HTuple weights, HTuple mode, HTuple sigmaT, HTuple sigmaR, out HTuple averagePose, out HTuple quality)`

`static HPose HPose.PoseAverage(HPose[] poses, HTuple weights, string mode, HTuple sigmaT, HTuple sigmaR, out HTuple quality)`

`static HPose HPose.PoseAverage(HPose[] poses, HTuple weights, string mode, double sigmaT, double sigmaR, out HTuple quality)`

## Description

`PoseAverage` computes the average rotation and translation of the
poses passed in *`poses`*, and returns this average pose in
*`averagePose`*.
The poses can be weighted using the parameter *`weights`*. If an
empty tuple is passed as weight, all poses have the same influence on the
result. Otherwise, a tuple that contains one positive weight per
pose needs to be passed. A higher weight leads to a higher influence of
that pose on the average.

`PoseAverage` supports two modes for averaging the poses, which
can be selected with the parameter *`mode`*.
*"direct"* selects a direct computation of the average, where the
translation and rotation are averaged independently from each other.
*"iterative"* uses the average pose computed by the
*"direct"* method as initial value for an iterative method, which
computes the local mode of the poses.
The iterative method is slower than the direct method. However, it returns
more accurate poses especially in the presence of outlier poses, as such
outliers are downweighted automatically.

For the iterative method, the relative weight of the translation and the
rotation can be set with the parameters *`sigmaT`* and
*`sigmaR`*, respectively. Both values can be set to *"auto"*,
in which case they are automatically estimated. In this case,
*`sigmaT`* is set to the spread of the translations of the poses, and
*`sigmaR`* is set to a constant value.
Both values describe the expected spread of the translation and the
rotation, and influence the weighting of the poses.
For the direct method, both parameters are ignored.

A measure of the quality of the computed pose is returned in
*`quality`*.
*`quality`* contains a tuple with four elements, which describe
the average and maximum deviation of the passed poses from the returned
average pose *`averagePose`*.
The order of the values is: Root-Mean-Square error of the translation,
Root-Mean-Square error of the rotation, maximum translation and maximum
rotation deviation. The weights passed in *`weights`* are used in the
Root-Mean-Square errors of translation and rotation, but not for the last
two quality measures.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`poses`** (input_control)  pose-array `→` [HPose](HPose.md), [HTuple](HTuple.md) (*int* / long)

Set of poses of which the average if computed.

**`weights`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Empty tuple, or one weight per pose.

Default:
[]

Restriction:
`Weights > 0 && length(Weights) == 0 || length(Weights) == length(Poses) / 7`

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Averaging mode.

Default:
"iterative"

List of values:
"direct", "iterative"

**`sigmaT`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long / string)

Weight of the translation.

Default:
"auto"

Suggested values:
"auto", 0.1, 1, 100

**`sigmaR`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long / string)

Weight of the rotation.

Default:
"auto"

Suggested values:
"auto", 0.1, 1, 10

**`averagePose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Weighted mean of the poses.

**`quality`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Deviation of the mean from the input poses.

Assertion:
`length(Quality) == 4`

## Result

If the parameters are valid, the operator `PoseAverage` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`ReadPose`,
`HomMat3dToPose`

## See also

`ReadPose`,
`HomMat3dToPose`,
`PoseToHomMat3d`

## Module

Foundation
