# CreateSheetOfLightCalibObject (Operator)

## Name

`CreateSheetOfLightCalibObject` — Create a calibration object for sheet-of-light calibration.

## Signature

`static void HOperatorSet.CreateSheetOfLightCalibObject(HTuple width, HTuple length, HTuple heightMin, HTuple heightMax, HTuple fileName)`

## Description

`CreateSheetOfLightCalibObject` creates a CAD model of a
calibration object for sheet-of-light calibration with
[`CalibrateSheetOfLight`](calibrate_sheet_of_light.md) and stores it in *`fileName`*.

![figure](../assets/4e82668069d399f1.svg)

A calibration object for sheet-of-light calibration

The calibration object consists of a ramp with a truncated pyramid rotated
by 45 degrees. The calibration object contains an orientation mark in the
form of a circular hole. The dimensions of the calibration target in *`width`*,
*`length`*, *`heightMin`*, and *`heightMax`* must be given
in meters. *`length`* must be at least 10% larger than *`width`*.
The Z coordinate of the highest point on the truncated pyramid is at
most *`heightMax`*. The calibration object might not be found by
[`CalibrateSheetOfLight`](calibrate_sheet_of_light.md) if the height difference between the
truncated pyramid and the ramp is too small. In this case, adjust
*`heightMin`* and *`heightMax`* accordingly or increase the
sampling rate when acquiring the calibration data.

The dimensions of the calibration object should be chosen such that it
is possible to cover the measuring volume of the sheet-of-light setup.
In addition, when selecting the *`length`* of the calibration object,
the speed of the sheet-of-light setup should be considered such that the
calibration object is sampled with enough profile measurements.

![figure](../assets/5a1fcfe6850daef6.svg)

Technical drawing of the calibration object, where `c` is the
diameter of the orientation mark, `d` is the distance of the
pyramid from the front of the calibration object, `h` is the height
of the truncated pyramid, `b` is the length of the diagonal
of the pyramid at the bottom, `t` is the corresponding length at
the top, and $\alpha$ is the angle of the ramp as seen in the
drawing. You can calculate these dimensions with the procedure
`get_sheet_of_light_calib_object_dimensions`.

Set the parameter *"calibration_object"* to *`fileName`* with
[`SetSheetOfLightParam`](set_sheet_of_light_param.md) to use the generated calibration object
in a subsequent call to [`CalibrateSheetOfLight`](calibrate_sheet_of_light.md).

Note that MVTec does not offer 3D calibration objects. Instead,
use `CreateSheetOfLightCalibObject` to generate a customized
CAD model of a calibration object. This CAD model can then be used to
produce the calibration object. Milled aluminum is an established material
for this. However, depending on the required precision, its thermal
stability may be a problem. Note that the surface should be bright. Its
color may have to be adjusted depending on the color of the
laser to provide a sufficient contrast to the color of the laser.
Additionally, the surface must not be translucent nor reflective.
To achieve this, you can anodize or lacquer it. Please note that when
lacquering it, the accuracy might be decreased due to the applied paintwork.
However, a surface that is too rough leads to a decreasing precision as
well. It is advisable to have the produced calibration object remeasured
to determine whether the required accuracy can be achieved. The accuracy
of the calibration object should be ten times higher than the required
accuracy of measurement. After having the object measured, the results can
be manually inserted into the DXF file that can then be used for the
calibration with [`CalibrateSheetOfLight`](calibrate_sheet_of_light.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`width`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Width of the object.

Default:
0.1

**`length`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Length of the object.

Default:
0.15

**`heightMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum height of the ramp.

Default:
0.005

**`heightMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum height of the ramp.

Default:
0.04

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Filename of the model of the calibration object.

Default:
"calib_object.dxf"

File extension:
.`dxf`

## Result

The operator `CreateSheetOfLightCalibObject` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Module

3D Metrology
