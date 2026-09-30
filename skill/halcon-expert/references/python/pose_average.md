# pose_average (Operator)

## Name

`pose_average` — Compute the average of a set of poses.

## Signature

`def pose_average(poses: Sequence[int], weights: Sequence[Union[float, int]], mode: str, sigma_t: Union[float, int, str], sigma_r: Union[float, int, str]) -> Tuple[Sequence[Union[float, int]], Sequence[float]]`

## Description

`pose_average` computes the average rotation and translation of the
poses passed in *`poses`*, and returns this average pose in
*`average_pose`*.
The poses can be weighted using the parameter *`weights`*. If an
empty tuple is passed as weight, all poses have the same influence on the
result. Otherwise, a tuple that contains one positive weight per
pose needs to be passed. A higher weight leads to a higher influence of
that pose on the average.

`pose_average` supports two modes for averaging the poses, which
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
rotation can be set with the parameters *`sigma_t`* and
*`sigma_r`*, respectively. Both values can be set to *"auto"*,
in which case they are automatically estimated. In this case,
*`sigma_t`* is set to the spread of the translations of the poses, and
*`sigma_r`* is set to a constant value.
Both values describe the expected spread of the translation and the
rotation, and influence the weighting of the poses.
For the direct method, both parameters are ignored.

A measure of the quality of the computed pose is returned in
*`quality`*.
*`quality`* contains a tuple with four elements, which describe
the average and maximum deviation of the passed poses from the returned
average pose *`average_pose`*.
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

**`poses`** (input_control)  pose-array `→` Sequence[int]

Set of poses of which the average if computed.

**`weights`** (input_control)  number-array `→` Sequence[Union[float, int]]

Empty tuple, or one weight per pose.

Default:
[]

Restriction:
`Weights > 0 && length(Weights) == 0 || length(Weights) == length(Poses) / 7`

**`mode`** (input_control)  string `→` str

Averaging mode.

Default:
"iterative"

List of values:
"direct", "iterative"

**`sigma_t`** (input_control)  number `→` Union[float, int, str]

Weight of the translation.

Default:
"auto"

Suggested values:
"auto", 0.1, 1, 100

**`sigma_r`** (input_control)  number `→` Union[float, int, str]

Weight of the rotation.

Default:
"auto"

Suggested values:
"auto", 0.1, 1, 10

**`average_pose`** (output_control)  pose `→` Sequence[Union[float, int]]

Weighted mean of the poses.

**`quality`** (output_control)  number-array `→` Sequence[float]

Deviation of the mean from the input poses.

Assertion:
`length(Quality) == 4`

## Result

If the parameters are valid, the operator `pose_average` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`read_pose`,
`hom_mat3d_to_pose`

## See also

`read_pose`,
`hom_mat3d_to_pose`,
`pose_to_hom_mat3d`

## Module

Foundation
