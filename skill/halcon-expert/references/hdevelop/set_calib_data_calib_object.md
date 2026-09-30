# set_calib_data_calib_object (Operator)

## Name

`set_calib_data_calib_object` — Define a calibration object in a calibration model.

## Signature

`set_calib_data_calib_object( : : CalibDataID, CalibObjIdx, CalibObjDescr : )`

## Description

The operator `set_calib_data_calib_object` defines the
calibration object with the index *`CalibObjIdx`* in the camera
calibration data model *`CalibDataID`*. The index must be
between 0 and `NumCalibObjects`-1 (`NumCalibObjects`
is specified during model creation with [`create_calib_data`](create_calib_data.md)
and can be queried with [`get_calib_data`](get_calib_data.md)).

If a calibration object description with index *`CalibObjIdx`* is
already defined, then the current object description overwrites it (the
description is 'substituted'). Note that all `NumCalibObjects`
calibration objects must be set to perform [`calibrate_cameras`](calibrate_cameras.md).

The parameter *`CalibObjDescr`* can be used in two ways:

- ***as a file name:*** —

  it specifies a calibration
  plate description file as created with [`create_caltab`](create_caltab.md) or
  [`gen_caltab`](gen_caltab.md).
- ***as a numerical tuple:*** —

  it specifies
  the 3D coordinates of all points of the calibration object. All
  X, Y, and Z coordinates, respectively, of all points must be
  packed sequentially in the tuple in form: `[X, Y, Z]`,
  i.e., `[X1, ..., Xn, Y1, ..., Yn, Z1, ..., Zn]`, where
  `|X| = |Y| = |Z|` and all coordinates are in meters.

To query the calibration objects parameters stored earlier in
a calibration data model, use [`get_calib_data`](get_calib_data.md).

To get detailed information about the calibration process of
your camera setup see the chapter [Calibration](toc_calibration.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- CalibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`CalibDataID`** (input_control, state is modified)  calib_data `→`  (handle)

Handle of a calibration data model.

**`CalibObjIdx`** (input_control)  number `→`  (integer)

Calibration object index.

Default:
0

Suggested values:
0, 1, 2

**`CalibObjDescr`** (input_control)  number(-array) `→`  (real / integer / string)

3D point coordinates or a description file name.

List of values:
'calplate.cpd', 'calplate_10mm.cpd', 'calplate_1200mm.cpd', 'calplate_160mm.cpd', 'calplate_20mm.cpd', 'calplate_20mm_dark_on_light.cpd', 'calplate_320mm.cpd', 'calplate_40mm.cpd', 'calplate_40mm_dark_on_light.cpd', 'calplate_5mm.cpd', 'calplate_640mm.cpd', 'calplate_80mm.cpd', 'calplate_80mm_dark_on_light.cpd', 'caltab.descr', 'caltab_100mm.descr', 'caltab_10mm.descr', 'caltab_200mm.descr', 'caltab_2500um.descr', 'caltab_30mm.descr', 'caltab_650um.descr', 'caltab_6mm.descr', 'caltab_800mm.descr', 'caltab_big.descr', 'caltab_small.descr'

## Possible Predecessors

`create_calib_data`,
`set_calib_data_cam_param`

## Possible Successors

`set_calib_data_cam_param`,
`set_calib_data_observ_points`,
`find_calib_object`

## Module

Calibration
