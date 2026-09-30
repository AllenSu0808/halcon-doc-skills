# QuatNormalize (Operator)

## Name

`QuatNormalize` — Normalize a quaternion.

## Signature

`static void HOperatorSet.QuatNormalize(HTuple quaternion, out HTuple normalizedQuaternion)`

`HQuaternion HQuaternion.QuatNormalize()`

## Description

The operator `QuatNormalize` scales the input quaternion
*`quaternion`* such that its norm is 1. The result is returned
in *`normalizedQuaternion`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Input quaternion.

**`normalizedQuaternion`** (output_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Normalized quaternion.

## Possible Predecessors

`AxisAngleToQuat`

## Possible Successors

`QuatToHomMat3d`,
`QuatRotatePoint3d`

## See also

`AxisAngleToQuat`,
`QuatInterpolate`,
`QuatCompose`,
`QuatConjugate`,
`DualQuatToHomMat3d`

## Module

Foundation
