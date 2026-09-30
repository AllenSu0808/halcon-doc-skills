# DualQuatTransLine3d (Operator)

## Name

`DualQuatTransLine3d` — Transform a 3D line with a unit dual quaternion.

## Signature

`static void HOperatorSet.DualQuatTransLine3d(HTuple dualQuaternion, HTuple lineFormat, HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentOrPointX, HTuple lineMomentOrPointY, HTuple lineMomentOrPointZ, out HTuple transLineDirectionX, out HTuple transLineDirectionY, out HTuple transLineDirectionZ, out HTuple transLineMomentOrPointX, out HTuple transLineMomentOrPointY, out HTuple transLineMomentOrPointZ)`

`void HDualQuaternion.DualQuatTransLine3d(string lineFormat, HTuple lineDirectionX, HTuple lineDirectionY, HTuple lineDirectionZ, HTuple lineMomentOrPointX, HTuple lineMomentOrPointY, HTuple lineMomentOrPointZ, out HTuple transLineDirectionX, out HTuple transLineDirectionY, out HTuple transLineDirectionZ, out HTuple transLineMomentOrPointX, out HTuple transLineMomentOrPointY, out HTuple transLineMomentOrPointZ)`

`void HDualQuaternion.DualQuatTransLine3d(string lineFormat, double lineDirectionX, double lineDirectionY, double lineDirectionZ, double lineMomentOrPointX, double lineMomentOrPointY, double lineMomentOrPointZ, out double transLineDirectionX, out double transLineDirectionY, out double transLineDirectionZ, out double transLineMomentOrPointX, out double transLineMomentOrPointY, out double transLineMomentOrPointZ)`

## Description

The operator `DualQuatTransLine3d` transforms a 3D line that
is represented by its Plücker coordinates by a 3D rigid transformation that
is given by the unit dual quaternion *`dualQuaternion`*.

For a brief introduction to dual quaternions, Plücker coordinates and the
used notation, see `“Solution Guide III-C - 3D Vision”`.

If *`lineFormat`* is set to *"moment"*, the moment of
the line must be passed in *`lineMomentOrPointX`*,
*`lineMomentOrPointY`*, and *`lineMomentOrPointZ`*.

If *`lineFormat`* is set to *"point"*, instead of the moment
an arbitrary point on the line can be passed in *`lineMomentOrPointX`*,
*`lineMomentOrPointY`*, and *`lineMomentOrPointZ`*.

The parameters of the transformed line are returned in
*`transLineDirectionX`*, *`transLineDirectionY`*,
*`transLineDirectionZ`*, *`transLineMomentOrPointX`*,
*`transLineMomentOrPointY`*, and *`transLineMomentOrPointZ`* in the
format that was specified in *`lineFormat`*.
If *`lineFormat`* is set to *"point"*, the point on the line
that is closest to the origin of the coordinate system is returned.

## Attention

`DualQuatTransLine3d` returns meaningful results only if
*`dualQuaternion`* is a unit dual quaternion and the length of
the line direction is 1.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dualQuaternion`** (input_control)  dual_quaternion `→` [HDualQuaternion](HDualQuaternion.md), [HTuple](HTuple.md) (*double* / int / long)

Unit dual quaternion representing the transformation.

**`lineFormat`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Format of the line parameters.

Default:
"moment"

List of values:
"moment", "point"

**`lineDirectionX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the direction vector of the line.

**`lineDirectionY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the direction vector of the line.

**`lineDirectionZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the direction vector of the line.

**`lineMomentOrPointX`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the moment vector or a point on the line.

**`lineMomentOrPointY`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the moment vector or a point on the line.

**`lineMomentOrPointZ`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the moment vector or a point on the line.

**`transLineDirectionX`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the direction vector of the
transformed line.

**`transLineDirectionY`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the direction vector of the
transformed line.

**`transLineDirectionZ`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the direction vector of the
transformed line.

**`transLineMomentOrPointX`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X component of the moment vector or a point on the
transformed line.

**`transLineMomentOrPointY`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Y component of the moment vector or a point on the
transformed line.

**`transLineMomentOrPointZ`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Z component of the moment vector or a point on the
transformed line.

## Possible Predecessors

`PointsToPlueckerLine`,
`PointDirectionToPlueckerLine`

## Possible Successors

`DualQuatCompose`,
`DualQuatConjugate`,
`PoseToDualQuat`

## Alternatives

`AffineTransPoint3d`,
`DualQuatTransPoint3d`

## See also

`DualQuatToHomMat3d`,
`DualQuatToScrew`,
`DualQuatToPose`,
`DualQuatNormalize`,
`SerializeDualQuat`,
`DeserializeDualQuat`,
`QuatRotatePoint3d`

## Module

Foundation
