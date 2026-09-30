# SetCalibDataCalibObject (Operator)

## Name

`SetCalibDataCalibObject` — Define a calibration object in a calibration model.

## Signature

`static void HOperatorSet.SetCalibDataCalibObject(HTuple calibDataID, HTuple calibObjIdx, HTuple calibObjDescr)`

`void HCalibData.SetCalibDataCalibObject(int calibObjIdx, HTuple calibObjDescr)`

`void HCalibData.SetCalibDataCalibObject(int calibObjIdx, double calibObjDescr)`

## Description

The operator `SetCalibDataCalibObject` defines the
calibration object with the index *`calibObjIdx`* in the camera
calibration data model *`calibDataID`*. The index must be
between 0 and `numCalibObjects`-1 (`numCalibObjects`
is specified during model creation with [`CreateCalibData`](create_calib_data.md)
and can be queried with [`GetCalibData`](get_calib_data.md)).

If a calibration object description with index *`calibObjIdx`* is
already defined, then the current object description overwrites it (the
description is 'substituted'). Note that all `numCalibObjects`
calibration objects must be set to perform [`CalibrateCameras`](calibrate_cameras.md).

The parameter *`calibObjDescr`* can be used in two ways:

- ***as a file name:*** —

  it specifies a calibration
  plate description file as created with [`CreateCaltab`](create_caltab.md) or
  [`GenCaltab`](gen_caltab.md).
- ***as a numerical tuple:*** —

  it specifies
  the 3D coordinates of all points of the calibration object. All
  X, Y, and Z coordinates, respectively, of all points must be
  packed sequentially in the tuple in form: `[X, Y, Z]`,
  i.e., `[X1, ..., Xn, Y1, ..., Yn, Z1, ..., Zn]`, where
  `|X| = |Y| = |Z|` and all coordinates are in meters.

To query the calibration objects parameters stored earlier in
a calibration data model, use [`GetCalibData`](get_calib_data.md).

To get detailed information about the calibration process of
your camera setup see the chapter [Calibration](toc_calibration.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- calibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calibDataID`** (input_control, state is modified)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a calibration data model.

**`calibObjIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Calibration object index.

Default:
0

Suggested values:
0, 1, 2

**`calibObjDescr`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

3D point coordinates or a description file name.

List of values:
"calplate.cpd", "calplate_10mm.cpd", "calplate_1200mm.cpd", "calplate_160mm.cpd", "calplate_20mm.cpd", "calplate_20mm_dark_on_light.cpd", "calplate_320mm.cpd", "calplate_40mm.cpd", "calplate_40mm_dark_on_light.cpd", "calplate_5mm.cpd", "calplate_640mm.cpd", "calplate_80mm.cpd", "calplate_80mm_dark_on_light.cpd", "caltab.descr", "caltab_100mm.descr", "caltab_10mm.descr", "caltab_200mm.descr", "caltab_2500um.descr", "caltab_30mm.descr", "caltab_650um.descr", "caltab_6mm.descr", "caltab_800mm.descr", "caltab_big.descr", "caltab_small.descr"

## Possible Predecessors

`CreateCalibData`,
`SetCalibDataCamParam`

## Possible Successors

`SetCalibDataCamParam`,
`SetCalibDataObservPoints`,
`FindCalibObject`

## Module

Calibration
