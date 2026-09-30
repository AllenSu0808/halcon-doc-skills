# query_calib_data_observ_indices (Operator)

## Name

`query_calib_data_observ_indices` — Query information about the relations between cameras, calibration objects,
and calibration object poses.

## Signature

`query_calib_data_observ_indices( : : CalibDataID, ItemType, ItemIdx : Index1, Index2)`

## Description

A calibration data model (*`CalibDataID`*) contains a collection of
observations, which are added to the model by
[`set_calib_data_observ_points`](set_calib_data_observ_points.md). Each observation is associated
to an observing camera, an observed calibration object, and a calibration
object pose. With the operator `query_calib_data_observ_indices`, you
can query observation indices associated to a camera or an calibration
object, depending on the parameter *`ItemType`*.

For *`ItemType`*=*'camera'*, you must pass a
valid camera index in *`ItemIdx`*. Then, *`Index1`* returns
a list of calibration object indices and *`Index2`* returns a
list of pose indices. Each pair `[Index1[I],Index2[I]]`
represents calibration object pose that are 'observed' by camera
*`ItemIdx`*.

For *`ItemType`*=*'calib_obj'*, you must specify
a valid calibration object index in *`ItemIdx`*. Then,
*`Index1`* returns a list of camera indices and *`Index2`* returns
a list of corresponding calibration object pose indices. Each pair
`[Index1[I],Index2[I]]` denotes that camera `Index1[I]`
is observing the `Index2[I]`th pose of calibration object
*`ItemIdx`*.

This operator is particularly suitable for accessing observation data
of a calibration data model whose configuration is unknown at the moment
of its usage (e.g., if it was just read from a file). As a special case,
this operator can be used to get the precise list of poses of
one calibration object (see the example).

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

**`ItemType`** (input_control)  string `→`  (string)

Kind of referred object.

Default:
'camera'

List of values:
'calib_obj', 'camera'

**`ItemIdx`** (input_control)  number `→`  (integer)

Camera index or calibration object index
(depending on the selected *`ItemType`*).

Default:
0

Suggested values:
0, 1, 2

**`Index1`** (output_control)  number-array `→`  (integer)

List of calibration object indices or list of
camera indices (depending on *`ItemType`*).

**`Index2`** (output_control)  number-array `→`  (integer)

Calibration object numbers.

## Example (HDevelop)

```
* Read a calibration model from a file.
read_calib_data ('calib_data.ccd',CalibDataID)

* Get calibration object indices assigned to calibration object 0.
query_calib_data_observ_indices (CalibDataID, 'calib_obj', 0, _, \
                                 CalibObjPoseIndices)
* CalibObjPoseIndices contains the list of pose indices of calibration
* object 0. In order to be stored in the model, each calibration object
* needs to be observed by at least one camera in the setup (a calibration
* object pose that is not observed by any camera cannot be stored in
* the model). Typically, a calibration object pose can be observed by more
* than one camera. Hence, some calibration object pose indices might appear
* repeatedly in CalibObjPoseIndices. We use tuple_sort and tuple_uniq to
* extract a unique list of calibration object pose indices for calibration
* object 0.
tuple_sort (CalibObjPoseIndices, CalibObjPoseIndices)
tuple_uniq (CalibObjPoseIndices, CalibObjPoseIndices)

* Get poses of calibration objects observed by camera 2.
calibrate_cameras (CalibDataID, Error)
query_calib_data_observ_indices (CalibDataID, 'camera', 2, CalibObjIndices,\
                                 CalibObjPoseIndices)
for I := 0 to |CalibObjIndices|-1 by 1
  get_calib_data (CalibDataID, 'calib_obj_pose', \
                  [CalibObjIndices[I], CalibObjPoseIndices[I]], \
                  'pose', CalibObjPose)
endfor
```

## Module

Calibration
