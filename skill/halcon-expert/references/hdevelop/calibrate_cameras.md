# calibrate_cameras (Operator)

## Name

`calibrate_cameras` — Determine all camera parameters by a simultaneous minimization
process.

## Signature

`calibrate_cameras( : : CalibDataID : Error)`

## Description

The operator `calibrate_cameras` calculates the internal and
external camera parameters of a calibration data model specified in
*`CalibDataID`*. The calibration data model describes a setup of one
or more cameras and is specified during the creation of the data model. You
can find detailed information about the calibration process in the chapter
reference [Calibration](toc_calibration.md).

The root mean square error (RMSE) of the back projection of the
optimization is returned in *`Error`* (in pixels). The error
gives a general indication whether the optimization was
successful. You can find more details about the RMSE in the chapter
reference mentioned above.

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

**`Error`** (output_control)  number `→`  (real)

Back projection root mean square error (RMSE) of the
optimization.

## Possible Predecessors

`create_calib_data`,
`set_calib_data_cam_param`,
`set_calib_data_calib_object`,
`set_calib_data_observ_points`,
`find_calib_object`,
`set_calib_data`,
`remove_calib_data_observ`

## Possible Successors

`get_calib_data`

## References

Carsten Steger: “A Comprehensive and Versatile Camera Model for
Cameras with Tilt Lenses”; International Journal of Computer
Vision, vol. 123, no. 2, pp. 121-159, 2017.
  
Carsten Steger, Markus Ulrich, Christian Wiedemann: “Machine Vision
Algorithms and Applications”; Wiley-VCH, Weinheim, 2nd Edition,
2018.
  
Markus Ulrich, Carsten Steger: “A Camera Model for Cameras with
Hypercentric Lenses and Some Example Applications”; Machine Vision
and Applications, vol. 30, no. 6, pp. 1013-1028, 2019.
  
Carsten Steger, Markus Ulrich: “A Camera Model for Line-Scan
Cameras with Telecentric Lenses”; International Journal of
Computer Vision, vol. 129, no. 1, pp. 80-99, 2021.
  
Carsten Steger, Markus Ulrich: “A Multi-view Camera Model for
Line-Scan Cameras with Telecentric Lenses”; Journal of
Mathematical Imaging and Vision, vol. 64, no. 2, pp. 105-130, 2022.

## Module

Calibration
