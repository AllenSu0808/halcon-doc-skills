# QuatConjugate (Operator)

## Name

`QuatConjugate` — Generate the conjugation of a quaternion.

## Signature

`static void HOperatorSet.QuatConjugate(HTuple quaternion, out HTuple conjugatedQuaternion)`

`HQuaternion HQuaternion.QuatConjugate()`

## Description

The operator `QuatConjugate` generates the conjugation
*`conjugatedQuaternion`* of the input quaternion *`quaternion`*.

The conjugation of a quaternion
$q=x_{0}+x_{1}i+x_{2}j+x_{3}k$
is given by $\bar{q} = x_{0} - x_{1}i - x_{2}j - x_{3}k$ ![figure](../assets/eda74a8cbaca4665.svg).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`quaternion`** (input_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Input quaternion.

**`conjugatedQuaternion`** (output_control)  quaternion `→` [HQuaternion](HQuaternion.md), [HTuple](HTuple.md) (*double*)

Conjugated quaternion.

## Possible Predecessors

`AxisAngleToQuat`

## Possible Successors

`QuatToHomMat3d`,
`QuatRotatePoint3d`

## See also

`AxisAngleToQuat`,
`QuatToHomMat3d`,
`QuatRotatePoint3d`,
`QuatNormalize`,
`QuatCompose`,
`QuatInterpolate`,
`DualQuatConjugate`

## Module

Foundation
