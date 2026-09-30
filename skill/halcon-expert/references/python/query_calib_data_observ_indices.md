# query_calib_data_observ_indices (Operator)

## Name

`query_calib_data_observ_indices` — Query information about the relations between cameras, calibration objects,
and calibration object poses.

## Signature

`def query_calib_data_observ_indices(calib_data_id: HHandle, item_type: str, item_idx: int) -> Tuple[Sequence[int], Sequence[int]]`

## Description

A calibration data model (*`calib_data_id`*) contains a collection of
observations, which are added to the model by
[`set_calib_data_observ_points`](set_calib_data_observ_points.md). Each observation is associated
to an observing camera, an observed calibration object, and a calibration
object pose. With the operator `query_calib_data_observ_indices`, you
can query observation indices associated to a camera or an calibration
object, depending on the parameter *`item_type`*.

For *`item_type`*=*"camera"*, you must pass a
valid camera index in *`item_idx`*. Then, *`index_1`* returns
a list of calibration object indices and *`index_2`* returns a
list of pose indices. Each pair `[Index1[I],Index2[I]]`
represents calibration object pose that are 'observed' by camera
*`item_idx`*.

For *`item_type`*=*"calib_obj"*, you must specify
a valid calibration object index in *`item_idx`*. Then,
*`index_1`* returns a list of camera indices and *`index_2`* returns
a list of corresponding calibration object pose indices. Each pair
`[Index1[I],Index2[I]]` denotes that camera `Index1[I]`
is observing the `Index2[I]`th pose of calibration object
*`item_idx`*.

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

- calib_data_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calib_data_id`** (input_control, state is modified)  calib_data `→` HHandle

Handle of a calibration data model.

**`item_type`** (input_control)  string `→` str

Kind of referred object.

Default:
"camera"

List of values:
"calib_obj", "camera"

**`item_idx`** (input_control)  number `→` int

Camera index or calibration object index
(depending on the selected *`item_type`*).

Default:
0

Suggested values:
0, 1, 2

**`index_1`** (output_control)  number-array `→` Sequence[int]

List of calibration object indices or list of
camera indices (depending on *`item_type`*).

**`index_2`** (output_control)  number-array `→` Sequence[int]

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
