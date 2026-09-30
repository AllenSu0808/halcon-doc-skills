## Calibration

List of Sections ↓

This chapter provides information regarding camera calibration.

### General Objectives

To achieve maximum accuracy of measurement for your camera setup, you have
to calibrate it accordingly.
Therefore, a camera model is determined, which describes the projection
of a 3D world point into a (sub-)pixel in the image.

HALCON provides a wide range of operators to approach diverse tasks related
to calibration, such as

- describing and finding a calibration object
  ([Calibration / Calibration Object](toc_calibration_calibrationobject.md)),
- the projection of points from the 3D scene onto the image plane and
  the other way around ([Calibration / Projection](toc_calibration_projection.md),
  [Calibration / Inverse Projection](toc_calibration_inverseprojection.md)),
- compensating perspective and radial distortions
  ([Calibration / Rectification](toc_calibration_rectification.md)),
- handling the camera parameters
  ([Calibration / Camera Parameters](toc_calibration_cameraparameters.md)),
- performing a self-calibration
  ([Calibration / Self-Calibration](toc_calibration_selfcalibration.md)), and
- calibrating different setups consisting of

  - one camera ([Calibration / Monocular](toc_calibration_monocular.md)),
  - multiple cameras ([Calibration / Binocular](toc_calibration_binocular.md),
    [Calibration / Multi-View](toc_calibration_multiview.md)), or
  - a camera in combination with a robot
    ([Calibration / Hand-Eye](toc_calibration_handeye.md)).

This chapter gives guidance regarding the basic
concept of retrieving the internal and external parameters of your camera.
The following paragraphs state how to successfully calibrate a camera.
In particular, they describe

- the needed calibration object,
- the individual steps to calibrate the cameras, including

  - how to prepare the calibration input data,
  - how to perform the actual calibration with
    [`calibrate_cameras`](calibrate_cameras.md), and
  - how to check the success of the calibration,
- the camera parameters,
- additional information about the calibration process, including

  - how to obtain an appropriate calibration plate,
  - how to take a set of suitable images, and
  - which distortion model to use,
- the available 3D camera models and how 3D points are transformed
  into the image coordinate system, and
- limitations related to specific camera types.

### Calibration Object

For a successful calibration of your camera setup, at least one calibration
object with accurately known metric properties is needed, e.g., a HALCON
calibration plate.
For the calibration, take a series of images of the calibration
object in different positions and orientations.
The success of the calibration highly depends on the quality of the
calibration object and the images. So you might want to exercise special
diligence during the acquisition of the calibration images.
See the section “How to take a set of suitable images?” for further
information.

A calibration plate is covered by multiple calibration marks, which are
extracted in the calibration images in order to retrieve their coordinates.
The orientation of the plate has to be known distinctively, hence, a
finder pattern is also part of the imprint.

Your local sales partner can provide you with two different types of standard
HALCON calibration plates:

- **Calibration plate with hexagonally arranged marks:** —

  As finder pattern, there are special groups of mark hexagons where some of
  the marks contain dot-shaped holes (see [`create_caltab`](create_caltab.md)).
  One finder pattern has to be visible to locate the calibration plate.
  To make sure the plate is not inverted, at least a second one needs to be
  seen, but the plate does not have to be fully visible in the image.
  The origin of the coordinate system is located at the center of the central
  mark of the first finder pattern.
  The z-axis of the coordinate system is pointing into
  the calibration plate, its x-axis is pointing to the right, and
  its y-axis is pointing downwards with the direction of view along
  the z-axis.

  When using [`camera_calibration`](camera_calibration.md) instead of
  [`calibrate_cameras`](calibrate_cameras.md), this calibration plate is not applicable.

  ![figure](../assets/83a3eae38e2fde8b.svg)

  HALCON calibration plate with hexagonally arranged marks.
- **Calibration plate with rectangularly arranged marks:** —

  The finder pattern consists of the surrounding frame and the triangular
  corner marker (see [`gen_caltab`](gen_caltab.md)).
  Thus, the plate has to be fully visible in the image.
  The origin is located in the middle of the surface of the calibration plate.
  The z-axis of the coordinate system is pointing into
  the calibration plate, its x-axis is pointing to the right, and
  its y-axis is pointing downwards with the direction of view along
  the z-axis.

  ![figure](../assets/e5f4786746efcf2c.svg)

  HALCON calibration plate with rectangularly arranged marks.

When acquiring your calibration images, note that there are different
recommendations on how to take them, depending on your used calibration
plate (see section “How to take a set of suitable images?”).

### Preparing the Calibration Input Data

Before calling a calibration operator (e.g., [`calibrate_cameras`](calibrate_cameras.md)), you
must create and adapt the calibration data model with the following steps:

1. **Create a calibration data model** with the operator
   [`create_calib_data`](create_calib_data.md), specifying the number of cameras in the
   setup and the number of used calibration objects.
2. **Specify the camera type and the initial internal
   camera parameters** with the operator
   [`set_calib_data_cam_param`](set_calib_data_cam_param.md).
3. **Specify the description of all calibration objects**
   with the operator [`set_calib_data_calib_object`](set_calib_data_calib_object.md).
4. **Collect observation data** with the operators
   [`find_calib_object`](find_calib_object.md) or [`set_calib_data_observ_points`](set_calib_data_observ_points.md),
   i.e., obtain the image coordinates of the extracted calibration marks of
   the calibration object and a roughly estimated pose of the
   calibration object relative to the observing camera.
5. **Configure the calibration process**, e.g., exclude certain
   camera parameters from the optimization.
   You can specify these parameters with the operator [`set_calib_data`](set_calib_data.md).
   For example, if the image sensor cell size of camera 0 is known precisely
   and only the rest of the parameters needs to be calibrated, you call

   |  |
   | --- |
   | [`set_calib_data(CalibDataID, 'camera', 0, 'excluded_settings', ['sx','sy'])`](set_calib_data.md). |

### Performing the Actual Camera Calibration and Obtaining its Results

Using all the information stored within the calibration data model, the
actual calibration can be performed calling [`calibrate_cameras`](calibrate_cameras.md).
Thereby, the input model is modified by optimizing the initial internal
camera parameters, computing and adding further data like the external
camera parameters or standard deviations.
Furthermore, the standard deviations and covariances of the calibrated
internal parameters and the root mean square error of the back projection
are calculated in order to check the success of the calibration.

The results can then be queried with the operator [`get_calib_data`](get_calib_data.md).

### Checking the Success of the Calibration

After a successful calibration, the root mean square error (RMSE) of
the back projection of the optimization is returned in
*`Error`* (in pixels). The error gives a general indication
whether the optimization was successful as it corresponds to the average
distance (in pixels) between the back projected calibration points and their
extracted image coordinates.

If only a single camera is calibrated, an *`Error`* in the
order of 0.1 pixel (the typical detection error by extraction of the
coordinates of the projected calibration markers) is an indication
that the optimization fits the observation data well. If
*`Error`* strongly differs from 0.1 pixels, the calibration did
not perform well. Reasons for this might be, e.g., a poor image
quality, an insufficient number of calibration images, or an
inaccurate calibration plate.

For information about how to check the success of the calibration
using a multi-view camera setup, see the respective section in the
chapter [Calibration / Multi-View](toc_calibration_multiview.md).

### Camera Parameters

Regarding camera parameters, you can distinguish between internal and
external camera parameters.

- **Internal camera parameters:** —

  These parameters describe the characteristics of the used camera,
  especially the dimension of the sensor itself and the projection
  properties of the used combination of lens, camera, and frame
  grabber. Below is an overview of all available camera types and
  their respective parameters `CameraParam`. In the list,
  “projective cameras” refers to the property that the lens
  performs a perspective projection on the object-side of the lens,
  while “telecentric cameras” refers to the property that the lens
  performs a telecentric projection on the object-side of the lens.

  - **Area scan cameras** —

    have 9 to 16 internal parameters depending on the camera type.

    For reasons explained below, parameters that are marked with an *
    asterisk are fixed and not estimated by the algorithm.

    - **Area scan cameras with regular lenses** —

      *Projective area scan cameras with regular lenses*

      - *`'area_scan_division'`*:
        *`['area_scan_division', Focus, Kappa, Sx, Sy*, Cx,
        Cy, ImageWidth, ImageHeight]`*
      - *`'area_scan_polynomial'`*:
        *`['area_scan_polynomial', Focus, K1, K2, K3, P1, P2,
        Sx, Sy*, Cx, Cy, ImageWidth, ImageHeight]`*

      *Telecentric area scan cameras with regular lenses*

      - *`'area_scan_telecentric_division'`*:
        *`['area_scan_telecentric_division', Magnification,
        Kappa, Sx, Sy*, Cx, Cy, ImageWidth, ImageHeight]`*
      - *`'area_scan_telecentric_polynomial'`*:
        *`['area_scan_telecentric_polynomial', Magnification,
        K1, K2, K3, P1, P2, Sx, Sy*, Cx, Cy, ImageWidth, ImageHeight]`*
    - **Area scan cameras with tilt lenses** —

      *Projective area scan cameras with tilt lenses*

      - *`'area_scan_tilt_division'`*:
        *`['area_scan_tilt_division', Focus, Kappa,
        ImagePlaneDist, Tilt, Rot, Sx, Sy*, Cx, Cy, ImageWidth, ImageHeight]`*
      - *`'area_scan_tilt_polynomial'`*:
        *`['area_scan_tilt_polynomial', Focus, K1, K2, K3, P1,
        P2, ImagePlaneDist, Tilt, Rot, Sx, Sy*, Cx, Cy, ImageWidth,
        ImageHeight]`*
      - *`'area_scan_tilt_image_side_telecentric_division'`*:
        *`['area_scan_tilt_image_side_telecentric_division',
        Focus, Kappa, Tilt, Rot, Sx*, Sy*, Cx, Cy, ImageWidth, ImageHeight]`*
      - *`'area_scan_tilt_image_side_telecentric_polynomial'`*:
        *`['area_scan_tilt_image_side_telecentric_polynomial',
        Focus, K1, K2, K3, P1, P2, Tilt, Rot, Sx*, Sy*, Cx, Cy,
        ImageWidth, ImageHeight]`*

      *Telecentric area scan cameras with tilt lenses*

      - *`'area_scan_tilt_bilateral_telecentric_division'`*:
        *`['area_scan_tilt_bilateral_telecentric_division',
        Magnification, Kappa, Tilt, Rot, Sx*, Sy*, Cx, Cy,
        ImageWidth, ImageHeight]`*
      - *`'area_scan_tilt_bilateral_telecentric_polynomial'`*:
        *`['area_scan_tilt_bilateral_telecentric_polynomial',
        Magnification, K1, K2, K3, P1, P2, Tilt, Rot, Sx*, Sy*, Cx,
        Cy, ImageWidth, ImageHeight]`*
      - *`'area_scan_tilt_object_side_telecentric_division'`*:
        *`['area_scan_tilt_object_side_telecentric_division',
        Magnification, Kappa, ImagePlaneDist, Tilt, Rot, Sx, Sy*,
        Cx, Cy, ImageWidth, ImageHeight]`*
      - *`'area_scan_tilt_object_side_telecentric_polynomial'`*:
        *`['area_scan_tilt_object_side_telecentric_polynomial',
        Magnification, K1, K2, K3, P1, P2, ImagePlaneDist, Tilt,
        Rot, Sx, Sy*, Cx, Cy, ImageWidth, ImageHeight]`*
    - **Area scan cameras with hypercentric lenses** —

      *Projective area scan cameras with hypercentric lenses*

      - *`'area_scan_hypercentric_division'`*:
        *`['area_scan_hypercentric_division', Focus, Kappa, Sx, Sy*,
        Cx, Cy, ImageWidth, ImageHeight]`*
      - *`'area_scan_hypercentric_polynomial'`*:
        *`['area_scan_hypercentric_polynomial', Focus, K1, K2, K3, P1,
        P2, Sx, Sy*, Cx, Cy, ImageWidth, ImageHeight]`*
    - **Description of the internal camera parameters of area scan cameras:** —
      - **CameraType:** —

        Type of the camera, as listed above.
      - **Focus:** —

        Focal length of the lens (only for lenses that perform a
        perspective projection on the object side of the lens).

        The initial value is the nominal focal length of the used lens,
        e.g., 0.008m.
      - **Magnification:** —

        Magnification of the lens (only for lenses that perform a
        telecentric projection on the object side of the lens).

        The initial value is the nominal magnification of the used
        telecentric lens (the image size divided by the object size),
        e.g., 0.2.
      - **Kappa $(\kappa)$:** —

        Distortion coefficient to model the radial lens distortions
        (only for the division model).

        Use 0.0 $m^{-2}$ as initial value.
      - **K1, K2, K3, P1, P2:** —

        Distortion coefficients to model the radial $(K_{1},K_{2},K_{3})$ and decentering $(P_{1},P_{2})$ lens distortions (only for the
        polynomial model).

        Use 0.0 as initial value for all five coefficients.
      - **ImagePlaneDist:** —

        Distance of the exit pupil of the lens to
        the image plane. The exit pupil is the (virtual) image of the
        aperture stop (typically the diaphragm), as viewed from the
        image side of the lens. Typical values are in the order of a
        few centimeters to very large values if the lens is close to
        being image-side telecentric.
      - **Tilt, Rot:** —

        The tilt angle $tilt(0^{\circ}\le tilt<90^{\circ})$ describes the angle by which the optical
        axis is tilted with respect to the normal of the sensor plane
        (corresponds to a rotation around the x-axis).
        The rotation angle $rot(0^{\circ}\le rot<360^{\circ})$ describes the rotation around the optical axis
        (z-axis).
        For a rotation $rot=0^{\circ}$ the optical
        axis gets tilted vertically down with respect to the camera
        housing, $rot=90^{\circ}$ corresponds to the optical
        axis being tilted horizontally to the left (direction of view along the
        z-axis), $rot=180^{\circ}$ corresponds to the optical
        axis being tilted vertically up, and $rot=270^{\circ}$
        corresponds to the optical axis being tilted horizontally to
        the right by $tilt$.

        These parameters are only used if a tilt lens is part of the camera
        setup.

        ![figure](../assets/2c46927c15452359.svg)

        The tilt of the lens is described by the parameters $rot$, $tilt$ and `ImagePlaneDist`.
        $rot$ describes the orientation of the tilt axis in
        relation to the x-axis of the sensor and has to be applied first.
        $tilt$ describes the actual tilt of
        the lens. `ImagePlaneDist` is the distance of the
        exit pupil of the lens to the image plane.

        These angles are typically roughly known based on the
        considerations that led to the use of the tilt lens or can be
        read off from the mechanism by which the lens is tilted.
      - **Sx, Sy:** —

        Scale factors. They correspond to the horizontal and vertical
        distance between two neighboring cells on the sensor. Since in
        most cases the image signal is sampled line-synchronously,
        $S_{y}$ is determined by the dimension of the sensor and
        does not need to be estimated by the calibration process.

        The initial values depend on the dimensions of the used chip of
        the camera. See the technical specification of your camera for
        the actual values. Attention: These values increase if the
        image is subsampled!

        As **projective cameras** are described through the pinhole camera
        model, it is impossible to determine
        `Focus`, $S_{x}$, and $S_{y}$ simultaneously.
        Therefore, the algorithm will keep $S_{y}$ fixed.

        For **telecentric lenses**, it is
        impossible to determine `Magnification`,
        $S_{x}$, and $S_{y}$ simultaneously. Therefore,
        the algorithm will keep $S_{y}$ fixed.

        For **image-side telecentric tilt lenses** (see chapter “Basics”,
        section “Camera Model and Parameters” in the
        `“Solution Guide III-C 3D Vision”` for an overview of different
        types of tilt lenses), it is impossible
        to determine `Focus`, $S_{x}$, $S_{y}$,
        and the tilt parameters $tilt$ and $rot$
        simultaneously. Therefore, additionally to $S_{y}$, the
        algorithm will keep $S_{x}$ fixed.

        For **bilateral telecentric tilt lenses**,
        it is impossible to determine `Magnification`,
        $S_{x}$, $S_{y}$, and the tilt parameters
        $tilt$ and $rot$ simultaneously. Therefore,
        additionally to $S_{y}$, the algorithm will keep $S_{x}$
        fixed.
      - **Cx, Cy:** —

        Column ($C_{x}$) and row ($C_{y}$) coordinate of
        the principal point of the image (center of the radial
        distortion).

        Use the half image width and height as initial values.
        Attention: These values decrease if the image is subsampled!
      - **ImageWidth, Image Height:** —

        Width and height of the sampled image. Attention: These values
        decrease if the image is subsampled!
  - **Line scan cameras** —

    have 12 or 16 internal parameters depending on the camera type.

    For reasons explained below, parameters that are marked with an *
    asterisk are fixed and not estimated by the algorithm.

    - **Line scan cameras with regular lenses** —

      *Projective line scan cameras with regular lenses*

      - *`'line_scan_division'`*:
        *`['line_scan_division', Focus, Kappa, Sx*, Sy*, Cx,
        Cy, ImageWidth, ImageHeight, Vx, Vy, Vz]`*
      - *`'line_scan_polynomial'`*:
        *`['line_scan_polynomial', Focus, K1, K2, K3, P1, P2,
        Sx*, Sy*, Cx, Cy, ImageWidth, ImageHeight, Vx, Vy, Vz]`*

      *Telecentric line scan cameras with regular lenses*

      - *`'line_scan_telecentric_division'`*:
        *`['line_scan_telecentric_division', Magnification,
        Kappa, Sx*, Sy*, Cx, Cy, ImageWidth, ImageHeight, Vx, Vy, Vz*]`*
      - *`'line_scan_telecentric_polynomial'`*:
        *`['line_scan_telecentric_polynomial', Magnification,
        K1, K2, K3, P1, P2, Sx*, Sy*, Cx, Cy, ImageWidth,
        ImageHeight, Vx, Vy, Vz*]`*
    - **Description of the internal camera parameters of line scan cameras:** —
      - **CameraType:** —

        Type of the camera, as listed above.
      - **Focus:** —

        Focal length of the lens (only for lenses that perform a
        perspective projection on the object side of the lens).

        The initial value is the nominal focal length of the used lens,
        e.g., 0.008m.
      - **Magnification:** —

        Magnification of the lens (only for lenses that perform a
        telecentric projection on the object side of the lens).

        The initial value is the nominal magnification of the used
        telecentric lens (the image size divided by the object size),
        e.g., 0.2.
      - **Kappa $(\kappa)$:** —

        Distortion coefficient of the division model to model the radial
        lens distortions.

        Use 0.0 $m^{-2}$ as initial value.
      - **K1, K2, K3, P1, P2:** —

        Distortion coefficients to model the radial $(K_{1},K_{2},K_{3})$ and decentering $(P_{1},P_{2})$ lens distortions (only for the
        polynomial model).

        Use 0.0 as initial value for all five coefficients.
      - **Sx:** —

        Scale factor. Corresponds to the horizontal distance between two
        neighboring cells on the sensor. Note that `Focus` or
        `Magnification`, respectively, and $S_{x}$ cannot
        be determined simultaneously. Therefore, $S_{x}$ is
        kept fixed in the calibration. The initial value for
        $S_{x}$ can be taken from the technical specifications
        of the camera. Attention: This value increases if the image is
        subsampled!
      - **Sy:** —

        Scale factor. During the calibration, it appears only in the
        form $p_{v}=-S_{y}\cdot C_{y}$.
        Consequently, $S_{y}$ and $C_{y}$ cannot be
        determined simultaneously. Therefore, in the calibration,
        $S_{y}$ is kept fixed. $p_{v}$ describes the
        distance of the image center point from the sensor line in
        meters. The initial value for $S_{y}$ can be taken from
        the technical specifications of the camera. Attention: This
        value increases if the image is subsampled!
      - **Cx:** —

        Column coordinate of the image center point (center of the
        radial distortions). Use half of the image width as the initial value
        for $C_{x}$. Attention: This value decreases if the
        image is subsampled!
      - **Cy:** —

        Distance of the image center point (center of the radial
        distortions) from the sensor line in scanlines. The initial
        value can normally be set to 0.
      - **ImageWidth, ImageHeight:** —

        Width and height of the sampled image. Attention: These values
        decrease if the image is subsampled!
      - **Vx, Vy, Vz:** —

        X-, Y-, and Z-component of the motion vector.

        The initial values for the x-, y-, and z-component of the motion
        vector depend on the image acquisition setup. Assuming a camera
        that looks perpendicularly onto a conveyor belt and that is
        rotated around its optical axis such that the sensor line is
        perpendicular to the conveyor belt, i.e., the y-axis of the
        camera coordinate system is parallel to the conveyor belt, use
        the initial values $V_{x}=V_{z}\text{= 0}$. The
        initial value for $V_{y}$ can then be determined, e.g.,
        from a line scan image of an object with known size (e.g.,
        calibration plate, ruler):

        $$V_y = \frac{l[m]}{l[\text{row}]}$$ ![figure](../assets/96eab4fa6ad3c2ae.svg)

        With
        $$l[m] = Length of the object in object coordinates [meter]\\l[row] = Length of the object in image coordinates [rows]$$ ![figure](../assets/0f8bacc4df9d6f10.svg)

        If, compared to the above setup, the camera is rotated 30
        degrees around its optical axis, i.e., around the z-axis of the
        camera coordinate system, the above determined initial values
        must be changed as follows:
        $$V_x^{z} = \sin(30^{\circ}) V_y \\ V_y^{z} = \cos(30^{\circ}) V_y \\ V_z^{z} = V_z = 0$$ ![figure](../assets/af3e89b6b8c6a8a6.svg)

        If, compared to the first setup, the camera is rotated -20
        degrees around the x-axis of the camera coordinate system, the
        following initial values result:
        $$V^x_x = V_x = 0 V^x_y = cos(-20^o)V_y V^x_z = sin(-20^o)V_y$$ ![figure](../assets/9d34413a812a29dc.svg)

        The quality of the initial values for $V_{x}$,
        $V_{y}$, and $V_{z}$ are crucial for the success
        of the whole calibration. If they are not precise enough, the
        calibration may fail.

        Note that for telecentric line scan cameras, the value of
        $V_{z}$ has no influence on the image position of 3D
        points and therefore cannot be determined. Consequently,
        $V_{z}$ is not optimized and left at its initial
        value for telecentric line scan cameras. Therefore, the
        initial value of $V_{z}$ should be set to
        *0*. For setups with multiple telecentric line scan
        cameras that share a common motion vector (for a detailed
        explanation, see [Calibration / Multi-View](toc_calibration_multiview.md)), however,
        $V_{z}$ can be determined based on the camera poses.
        Therefore, in this case $V_{z}$ is optimized.
  - **Restrictions for internal camera parameters** —

    Note that the term *focal length* is not quite correct and
    would be appropriate only for an infinite object distance. To
    simplify matters, always the term *focal length* is used even
    if the *image distance* is meant.

    For all operators that use camera parameters as input
    the respective parameter values are checked as to whether they fulfill the
    following restrictions:

    $$S_x > 0 S_y ≥ 0 Focus > 0 Magnification > 0 ImageWidth > 0 ImageHeight > 0 ImagePlaneDist > 0 0 ≤ tilt < 90 0 ≤ rot < 360 V_x^2 + V_y^2 + V_z^2 ≠ 0$$ ![figure](../assets/fceaf803e3f2cd22.svg)

    For some operators the restrictions differ slightly. In
    particular, for operators that do not support line scan cameras
    the following restriction applies:
    $$S_{y}>0$$
- **External camera parameters:** —

  The following 6 parameters describe the 3D pose, i.e., the position and
  orientation of the world coordinate system relative to the camera
  coordinate system. The x- and y-axis of the camera coordinate system are
  parallel to the column and row axes of the image, while the z-axis is
  perpendicular to the image plane. For line scan cameras, the pose of the
  world coordinate system refers to the camera coordinate system of the
  first image line.

  - **TransX:** —

    Translation along the x-axis of the camera coordinate system.
  - **TransY:** —

    Translation along the y-axis of the camera coordinate system.
  - **TransZ:** —

    Translation along the z-axis of the camera coordinate system.
  - **RotX:** —

    Rotation around the x-axis of the camera coordinate system.
  - **RotY:** —

    Rotation around the y-axis of the camera coordinate system.
  - **RotZ:** —

    Rotation around the z-axis of the camera coordinate system.

  The pose tuple contains one more element, which is the
  representation type of the pose. It codes the combination of the
  parameters *`OrderOfTransform`*, *`OrderOfRotation`*, and
  *`ViewOfTransform`*. See [`create_pose`](create_pose.md) for more information
  about 3D poses.

  When using a standard HALCON calibration plate, the world
  coordinate system is defined by the coordinate system of the
  calibration plate.
  See the section “Calibration Object” above for further information.

  If a HALCON calibration plate is used, you can use the operator
  [`find_calib_object`](find_calib_object.md) to determine initial values for all
  parameters. Using HALCON calibration plates with rectangularly
  arranged marks, a combination of the two operators [`find_caltab`](find_caltab.md)
  and [`find_marks_and_pose`](find_marks_and_pose.md) will have the same effect.
- **Parameter units:** —

  HALCON calibration plates use meters as unit.
  The camera parameters use corresponding units.
  Of course, calibration can be done using different units, but in this case
  the related parameters have to be adapted.
  Here, we list the HALCON default units for the different camera
  parameters:

  |  | Parameter | Unit |
  | --- | --- | --- |
  | External | RotX, RotY, RotZ | $deg$, $deg$, $deg$ |
  |  | TransX, TransY, TransZ | $m$, $m$, $m$ |
  | Internal | Cx, Cy | $px$, $px$ |
  |  | Focus | $m$ |
  |  | ImagePlaneDist | $m$ |
  |  | ImageWidth, ImageHeight | $px$, $px$ |
  |  | K1, K2, K3 | $m^{-2}$, $m^{-4}$, $m^{-6}$ |
  |  | Kappa $(\kappa)$ | $m^{-2}$ |
  |  | P1, P2 | $m^{-1}$, $m^{-1}$ |
  |  | Magnification | - (scalar) |
  |  | Sx, Sy | $m/px$, $m/px$ |
  |  | Tilt, Rot | $deg$, $deg$ |
  |  | Vx, Vy, Vz | $m/scanline$, $m/scanline$, $m/scanline$ |

### Additional Information about the Calibration Process

The use of [`calibrate_cameras`](calibrate_cameras.md) leads to some questions, which
are addressed in the following sections:

- ****How to obtain an appropriate calibration plate?**** —

  You can obtain high-precision calibration plates in various sizes
  and materials from your local sales partner. These calibration
  plates come with associated description files and can be easily
  extracted with [`find_calib_object`](find_calib_object.md).

  It is also possible to use any arbitrary object for
  calibration. The only requirement is that the object has
  characteristic points that can be robustly detected in the image
  and that the 3D world position of these points is known with high
  accuracy. See the `“Solution Guide III-C 3D Vision”` for details.

  Self-printed calibration objects are usually not accurate enough
  for high-precision applications.
- ****How to take a set of suitable images?**** —

  With the combination of lens (fixed focus
  setting!), camera, and frame grabber to be calibrated, a set of
  images of the calibration plate must be taken (see
  [`open_framegrabber`](open_framegrabber.md) and [`grab_image`](grab_image.md)).

  Your local sales partner can provide you with two different types of
  standard HALCON calibration plates: Calibration plates with hexagonally
  arranged marks (see [`create_caltab`](create_caltab.md)) and calibration plates
  with rectangularly arranged marks (see [`gen_caltab`](gen_caltab.md)). Since
  these two calibration plates substantially differ from each other,
  in some cases additional particularities apply (see below).

  The parameters and hints listed below should be considered when taking
  the calibration images.
  For a successful calibration, the setup and the used set of images should
  have certain qualities. These qualities may vary for the specific task and
  demand. In order to give guidance, values and hints suitable for a basic
  monocular camera setup are mentioned.

  - **Regarding the camera setup:** —
    - **Aperture**

      The aperture of the camera must not be changed during the
      acquisition of the images. If the aperture is changed after
      the calibration, the camera must be calibrated anew.
    - **Camera pose**

      The position of the camera must not be changed during the
      image acquisition.
    - **Focus**

      The calibration images should be sharply focused, i.e., transitions
      between objects should be clearly delimited. The focus, respectively
      the focal length, must not be changed during the image acquisition.
  - **Regarding the placement of the calibration plates:** —
    - **Field of view coverage and orientation**

      Within the set of calibration images, every part of the field of view
      should be covered by the plate at least once.
      The calibration plate may also fill the entire image.
      The orientation of the plate should vary within the set of images.
    - **Tilt angles**

      The set of calibration images should also contain images with tilted
      calibration plates. Thereby the plate should be tilted in different
      directions at an angle of about 30-45°.
      Note, that if the recommended angle cannot be realized due to, e.g.,
      limited depth of field, you should at least tilt your plate as steeply
      as possible with your setup.
    - **Number of images/ calibration plate poses**

      - Plate with hexagonally arranged marks: At least 6 images
        (Not all, but at least 4 of them with tilted calibration plates).
      - Plate with rectangularly arranged marks: At least 15 images.

      Nevertheless, you must make sure that the poses of the
      calibration plates also fulfill the other requirements.
    - **Inverted acquisition of the calibration plate**

      The calibration marks must not be acquired inverted. This can,
      e.g., happen if a calibration plate made of glass is acquired
      from its backside or if a line scan camera is not moving
      downwards with respect to the image coordinate system (i.e.,
      $V_{y}$ is negative).
  - **Regarding image properties and content:** —
    - **Pattern coverage**

      How much of the calibration pattern must at least be contained in
      the images depends on the used plate.

      - Plate with hexagonally arranged marks: At least one finder
        pattern needs to be visible. If at least two finder patterns
        are visible in the image, it is possible to detect whether
        the calibration plate is mirrored or not.
        In a mirrored case, a suitable error will be returned.
      - Plate with rectangularly arranged marks: Plate needs to be
        completely visible, as the finder pattern is the frame
        surrounding the point marks.

      Nevertheless, of course, the more of the calibration pattern is
      visible to the camera and the more of the field of view is
      filled by the calibration plate, the better.
    - **Mark diameter**

      The marks of the calibration plates should have a diameter of at
      least 20 pixels in each image. This requirement is essential for a
      successful calibration.
    - **Contrast**

      The contrast between the light and dark areas of the calibration
      plate should be at least 100 gray values (regarding byte images).
    - **Overexposure**

      To avoid overexposed images, make sure that gray values of the light
      parts of the calibration plate do not exceed 240 (regarding byte
      images), especially not in the neighborhood of the calibration marks.
    - **Homogeneity**

      The calibration plate should be illuminated homogeneously and
      reflections should be avoided. As a rule of thumb, the range
      of gray values of the light parts of the plate should not
      exceed 45 (regarding byte images).
  - **Regarding image format and preprocessing:** —
    - **Image format**

      Calibration images should be saved in an uncompressed format.
      Compression artifacts which occur, e.g., when using JPG format
      and high compression rates need to be avoided.
    - **Preprocessing**

      Calibration images should not be preprocessed. If image properties
      like contrast or focus are insufficient (see above),
      the issues need to be resolved by adjusting the camera setup
      instead of processing the images ahead of the calibration.
- ****Which distortion model should be used?**** —

  Two distortion models can be used: The division model and the
  polynomial model. The division model uses one parameter to model
  the radial distortions while the polynomial model uses five
  parameters to model radial and decentering distortions (see the
  sections “Camera parameters” and “The Used 3D camera model”).

  The advantages of the division model are that the distortions can be
  applied faster, especially the inverse distortions, i.e., if world
  coordinates are projected into the image plane. Furthermore, if
  only few calibration images are used or if the field of view is not
  covered sufficiently, the division model typically yields more
  stable results than the polynomial model. The main advantage of the
  polynomial model is that it can model the distortions more
  accurately because it uses higher order terms to model the radial
  distortions and because it also models the decentering distortions.
  Note that the polynomial model cannot be inverted analytically.
  Therefore, the inverse distortions must be calculated iteratively,
  which is slower than the calculation of the inverse distortions with
  the (analytically invertible) division model.

  Typically, the division model should be used for the calibration.
  If the accuracy of the calibration is not high enough, the
  polynomial model can be used. Note, however, that the calibration
  sequence used for the polynomial model must provide an even better
  coverage of the area in which measurements will later be
  performed. The distortions may be modeled inaccurately outside of
  the area that was covered by the calibration plate. This holds for
  the image border as well as for areas inside the field of view that
  were not covered by the calibration plate.

### The Used 3D Camera Model

In general, camera calibration means the exact determination of the
parameters that model the (optical) projection of any 3D world point
$\mathbf{p}^{\textit{w}}$ into a (sub-)pixel (r,c) in the
image. This is important if the original 3D pose of an object must be
computed from the image (e.g., for measuring industrial parts).
The appropriate projection model depends on the camera type used
in your setup.

For the modeling of this projection process, which is determined by
the used combination of camera, lens, and frame grabber, HALCON
provides the following 3D camera models:

- **Area scan pinhole camera:** —

  The combination of an area scan camera with a lens that effects a
  perspective projection on the object side of the lens and that may
  show radial and decentering distortions. The lens may be a tilt
  lens, i.e., the optical axis of the lens may be tilted with respect
  to the camera's sensor (this is sometimes called a Scheimpflug
  lens). Since hypercentric lenses also perform a perspective
  projection, cameras with hypercentric lenses are pinhole cameras.
  The models for regular (i.e., non-tilt) pinhole and
  image-side telecentric lenses are identical. In contrast, the
  models for pinhole and image-side telecentric tilt lenses differ
  substantially, as described below.
- **Area scan telecentric camera:** —

  The combination of an area scan camera with a lens that is
  telecentric on the object-side of the lens, i.e., that effects a
  parallel projection on the object-side of the lens, and that may
  show radial and decentering distortions. The lens may be a tilt
  lens. The models for regular (i.e., non-tilt) bilateral and
  object-side telecentric lenses are identical. In contrast, the
  models for bilateral and object-side telecentric tilt lenses differ
  substantially, as described below.
- **Line scan pinhole camera:** —

  The combination of a line scan camera with a lens that effects a
  perspective projection and that may show radial distortions. Tilt
  lenses are currently not supported for line scan cameras.
- **Line scan telecentric camera:** —

  The combination of a line scan camera with a lens that effects a
  telecentric projection and that may show radial distortions. Tilt
  lenses are currently not supported for line scan cameras.

To transform a 3D point $\mathbf{p}^{\textit{w}}=(\mathbf{x}^{\textit{w}},\mathbf{y}^{\textit{w}},\mathbf{z}^{\textit{w}})^{T}$
which is given in world coordinates, into a 2D point $\mathbf{q}^{\textit{i}}=(\mathbf{r},\mathbf{c})^{T}$,
which is given in pixel coordinates, a chain of transformations is
needed:

$$p^{w} \rightarrow p^{c} \rightarrow q^{c} \rightarrow \tilde{q}^{c} [ \rightarrow q^{t} ] \rightarrow q^{i}$$ ![figure](../assets/9409dfdbcf0bbcf1.svg)

|  |  |
| --- | --- |
|  |  |
| $\mathbf{p}^{\textit{w}}$ | 3D world point |
| $\mathbf{p}^{\textit{c}}$ | Transformed into camera coordinate system |
| $\mathbf{q}^{\textit{c}}$ | Projected into image plane (2D point, still in metric coordinates) |
| $\tilde{q}^{c}$ ![figure](../assets/2b3900f1ba9eced5.svg) | Lens distortion applied |
| $\mathbf{q}^{\textit{t}}$ | If a tilted lens is used, the point $\tilde{q}^{c}$ ![figure](../assets/2b3900f1ba9eced5.svg) is projected on the point $\mathbf{q}^{\textit{t}}$ in the tilted image plane. In this case the distorted point $\tilde{q}^{c}$ ![figure](../assets/2b3900f1ba9eced5.svg) only lies on a virtual image plane of a system without tilt. |
| $\mathbf{q}^{\textit{i}}$ | Pixel coordinates |

The following paragraphs describe these steps in more detail for area scan
cameras and subsequently for line scan cameras.
For a even more detailed description of the different 3D camera models as
well as some explanatory diagrams please refer to the chapter “Basics”,
section “Camera Model and Parameters” in the
`“Solution Guide III-C 3D Vision”`.

- **Transformation step 1: $\mathbf{p}^{\textit{w}}\rightarrow\mathbf{p}^{\textit{c}}$** —

  The point $\mathbf{p}^{\textit{w}}$ is transformed from world
  into camera coordinates (points as homogeneous vectors, compare
  [`affine_trans_point_3d`](affine_trans_point_3d.md)) by :
  $$\begin{pmatrix} p^{c} \\ 1 \\ end{pmatrix} = \begin{pmatrix} x^{c} \\ y^{c} \\ z^{c} \\ 1 \end{pmatrix} = \begin{bmatrix} \mathbf{R} & \mathbf{T} \\ 0 & 1 \end{bmatrix} \cdot \begin{pmatrix} p^{w} \\ 1 \end{pmatrix}$$ ![figure](../assets/9746e321e154719f.svg)

  with $\mathbf{R}$ and $\mathbf{T}$ being
  the rotation and translation matrices (refer to
  the chapter “Basics”, section “3D Transformations and Poses`” in the
  `“Solution Guide III-C 3D Vision”` for detailed information).
- **Transformation step 2: $\mathbf{p}^{\textit{c}}\rightarrow\mathbf{q}^{\textit{c}}$** —

  If the underlying camera model is an **area scan pinhole
  camera**, the projection of $\mathbf{p}^{\textit{c}}=(\mathbf{x}^{\textit{c}},\mathbf{y}^{\textit{c}},\mathbf{z}^{\textit{c}})^{T}$
  into the image plane is described by the following equation:
  $$\mathbf{q}^{\mathrm{c}} = \begin{pmatrix} u \\ v \end{pmatrix} = \frac{f}{Z^{\mathrm{c}}}\begin{pmatrix} x^{\mathrm{c}} \\ y^{\mathrm{c}} \end{pmatrix}$$ ![figure](../assets/7d9510c1ebf8bc78.svg)
  where $f=\texttt{Focus}$. For cameras with
  hypercentric lenses, the following equation holds instead:
  $$\vec{q}^{\,c} = \begin{pmatrix} u \\ v \\end{pmatrix} = -\frac{f}{z^{\,c}} \biggl( \begin{pmatrix} x^{\,c} \\ y^{\,c} \end{pmatrix} \biggr)$$ ![figure](../assets/9c76d626320d5100.svg)

  If an **area scan telecentric camera** is used, the
  corresponding equation is:
  $$\mathbf{q}^{\mathrm{c}} = \begin{pmatrix} u \\ v \end{pmatrix} = m \begin{pmatrix} x^{\mathrm{c}} \\ y^{\mathrm{c}} \end{pmatrix}$$ ![figure](../assets/21f6e938e7744548.svg)
  where $m=\texttt{Magnification}$.
- **Transformation step 3: $\mathbf{q}^{\mathrm{c}} \;\rightarrow\; \tilde{\mathbf{q}}^{\mathrm{c}}$ ![figure](../assets/958ab800c275603a.svg)** —

  For all types of cameras, the lens distortions can be modeled
  either by the division model or by the polynomial model.

  The **division model** uses one parameter `Kappa`
  to model the radial distortions.

  The following equations transform the distorted image plane
  coordinates into undistorted image plane coordinates if the division
  model is used:
  $$\begin{pmatrix} u \\ v \end{pmatrix} = \frac{1}{1 + \kappa(\tilde{u}^2 + \tilde{v}^2)} \begin{pmatrix} \tilde{u} \\ \tilde{v} \end{pmatrix}$$ ![figure](../assets/d744b974a661e9a7.svg)

  These equations can be inverted analytically, which leads to the
  following equations that transform undistorted coordinates into
  distorted coordinates:
  $$\tilde{\mathbf{q}}^{c} = \begin{pmatrix} \tilde{u} \\ \tilde{v} \end{pmatrix} = \frac{2}{1 + \sqrt{1 - 4\kappa(u^2 + v^2)}} \begin{pmatrix} u \\ v\end{pmatrix}$$ ![figure](../assets/366ff3bb6a1ebcbe.svg)

  The **polynomial model** uses three parameters ($K_{1},K_{2},K_{3}$) to model the radial distortions and two
  parameters ($P_{1},P_{2}$) to model the decentering
  distortions.

  The following equations transform the distorted image plane
  coordinates into undistorted image plane coordinates if the
  polynomial model is used:
  $$\left(\begin{array}{c}u\\v\end{array}\right) = \left(\begin{array}{cc} \tilde{u} + \tilde{u}(K_1 r^2 + K_2 r^4 + K_3 r^6) + P_1(r^2 + 2\tilde{u}^2) + 2P_2 \tilde{u}\tilde{v}\\ \tilde{v} + \tilde{v}(K_1 r^2 + K_2 r^4 + K_3 r^6) + 2P_1 \tilde{u}\tilde{v} + P_2(r^2 + 2\tilde{v}^2) \end{array}\right)$$ ![figure](../assets/22cfa0747eb336ba.svg)
  with $r = \sqrt{\tilde{u}^2 + \tilde{v}^2}$ ![figure](../assets/fd7ffd73898f3041.svg)

  These equations cannot be inverted analytically. Therefore,
  distorted image plane coordinates must be calculated from
  undistorted image plane coordinates numerically.
- **Additional transformation step for tilt lenses: $\tilde{q}^{c} \rightarrow \mathbf{q}^{t}$ ![figure](../assets/51c0df32ce69dacc.svg)** —

  If the camera lens is a **tilt lens**, the tilt of the lens with
  respect to the image plane is described by the rotation
  angle $rot$ and the tilt angle $tilt$.

  In this step you have to further distinguish between different types of tilt
  lenses as described below. See chapter “Basics”, section “Camera Model and
  Parameters” in the `“Solution Guide III-C 3D Vision”` for an
  overview of different types of tilt lenses.

  For **projective tilt lenses** and **object-side
  telecentric tilt lenses** (which perform a perspective projection on
  the image side of the lens) the projection of $\tilde{\mathbf{q}}^{c} = (\tilde{\mathbf{u}}, \tilde{\mathbf{v}})^{T}$ ![figure](../assets/4cd8c2044f7d860b.svg) into the point $q^{t} = (\hat{u}, \hat{v})^{T}$ ![figure](../assets/b4516d8eec1e1c87.svg), which lies
  in the tilted image plane, is described by a projective 2D
  transformation, i.e., by the homogeneous 3×3
  matrix $\mathbf{H}$ (see
  [`projective_trans_point_2d`](projective_trans_point_2d.md)):

  $$\left( \begin{array}{c} q^{t}_{1} \\ q^{t}_{w} \end{array} \right) = \mathbf{H} \cdot \left( \begin{array}{c} \tilde{q}^{c} \\ 1 \end{array} \right)$$ ![figure](../assets/1966618ac001f638.svg)
  where $q_{w}^{t}$ is the additional coordinate from the
  projective transformation of a homogeneous point.
  $$H = \begin{pmatrix} h_{11} & h_{12} & h_{13} \\ h_{21} & h_{22} & h_{23} \\ h_{31} & h_{32} & h_{33} \end{pmatrix} = \begin{pmatrix} q_{11}q_{33} - q_{13}q_{31} & q_{21}q_{33} - q_{23}q_{31} & 0 \\ q_{12}q_{33} - q_{13}q_{32} & q_{22}q_{33} - q_{23}q_{32} & 0 \\ q_{13}/d & q_{23}/d & q_{33} \end{pmatrix}$$ ![figure](../assets/279a3fb5fd5de8a5.svg)
  where $d=\texttt{ImagePlaneDist}$ and
  $$\mathbf{Q} = \begin{pmatrix} q_{11} & q_{12} & q_{13} \\ q_{21} & q_{22} & q_{23} \\ q_{31} & q_{32} & q_{33} \end{pmatrix} \\\qquad = \\\begin{pmatrix} (\cos \rho)^2(1-\cos \tau) + \cos \tau & \cos \rho \sin \rho (1-\cos \tau) & \sin \rho \sin \tau \\ \cos \rho \sin \rho (1-\cos \tau) & (\sin \rho)^2(1-\cos \tau) + \cos \tau & -\cos \rho \sin \tau \\ -\sin \rho \sin \tau & \cos \rho \sin \tau & \cos \tau \end{pmatrix} }$$ ![figure](../assets/ff3be0d8eb1609ee.svg)
  with $\rho=rot$ and $\tau=tilt$.

  For **image-side telecentric tilt lenses** and
  **bilateral telecentric tilt lenses** (which perform a parallel
  projection on the image side of the lens), the projection onto the
  tilted image plane is described by a linear 2D transformation, i.e.,
  by a 2×2 matrix:
  $$H = \begin{pmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{pmatrix} = \frac{1}{q_{11}q_{22} - q_{12}q_{21}} \begin{pmatrix} q_{22} & -q_{12} \\ -q_{21} & q_{11} \end{pmatrix}$$ ![figure](../assets/05d091a57e764fc1.svg)
  where $\mathbf{Q}$ is defined as above for projective
  lenses.
- **Transformation step 4: $\mathbf{q}^{\textit{t}}\rightarrow\mathbf{q}^{\textit{i}}$ / $\tilde{q}^{\,c} \rightarrow q^{i}$ ![figure](../assets/7e526bdca18dd1f7.svg)** —

  Finally, the point $\tilde{\mathbf{q}}^{c} = (\tilde{\mathbf{u}}, \tilde{\mathbf{v}})^{T}$ ![figure](../assets/4cd8c2044f7d860b.svg) (or $\mathbf{q}^{\textit{t}}$ if a
  tilt lens is present) is transformed from the image plane coordinate
  system into the image coordinate system (the pixel coordinate
  system):
  $$\mathbf{q}^{i} = \begin{pmatrix} r \\ c \end{pmatrix} = \begin{pmatrix} \frac{\tilde{u}}{S_y} + C_y \\ \frac{\tilde{u}}{S_x} + C_x \end{pmatrix}$$ ![figure](../assets/76ef6f8dc84f685a.svg)

For **line scan cameras**, also the relative motion between the
camera and the object must be modeled. In HALCON, the following
assumptions for this motion are made:

1. The camera moves with constant velocity along a straight
   line.
2. The orientation of the camera is constant.
3. The motion is equal for all images.

The motion is described by the motion vector $V=(V_{x},V_{y},V_{z})^{T}$ that must be given in [meter/row]
in the camera coordinate system. The motion vector describes the
motion of the camera, assuming a fixed object. In fact, this is
equivalent to the assumption of a fixed camera with the object
traveling along $-V$.

The camera coordinate system of line scan cameras is defined as
follows: The origin of the coordinate system is the center of
projection (for pinhole cameras) or the center of distortion (for
telecentric cameras), respectively. The z-axis is identical to the
optical axis and directed so that the visible points have positive z
coordinates. The y-axis is perpendicular to the sensor line and to
the z-axis. It is directed so that the motion vector has a positive
y-component. The x-axis is perpendicular to the y- and z-axis, so
that the x-, y-, and z-axis form a right-handed coordinate system.

As the camera moves over the object during the image acquisition,
also the camera coordinate system moves relatively to the object,
i.e., each image line has been imaged from a different
position. This means there would be an individual pose for each
image line. To make things easier, in HALCON all transformations
from world coordinates into camera coordinates and vice versa are
based on the pose of the first image line only. The motion $V$ is
taken into account during the projection of the point
$\mathbf{p}^{\textit{c}}$ into the image. Consequently, only
the pose of the first image line is computed by the operator
[`find_calib_object`](find_calib_object.md) (and stored by [`calibrate_cameras`](calibrate_cameras.md)
in the calibration results).

For **line scan cameras**, the transformation from world to
camera coordinates ($\mathbf{p}^{\textit{w}}\rightarrow\mathbf{p}^{\textit{c}}$) works in the same way. Therefore, you can
also apply transformation step 1 as described for area scan cameras
above.

For **line scan pinhole cameras**, the projection of the point
$\mathbf{p}^{\textit{c}}$ that is given in the camera
coordinate system into (sub-)pixel coordinates $(r,c)$ in the
image is modeled as follows:

Assuming
$$p^{c} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$$ ![figure](../assets/2094595a8efdf8b1.svg)
the following set of equations must be solved for $m$,
$\tilde{u}$ ![figure](../assets/ca7043f252367aee.svg), and $t$:
$$m \cdot u(\tilde{u}, p_{v}) = x - t \cdot V_{x} \\ m \cdot v(\tilde{u}, p_{v}) = y - t \cdot V_{y} \\ m \cdot Focus = z - t \cdot V_{z}$$ ![figure](../assets/1e6f05b638877edf.svg)
were $u\left(\tilde{u}, \tilde{v}\right)$ ![figure](../assets/30d919f606f819ef.svg) and
$v\left(\tilde{u},\tilde{v}\right)$ ![figure](../assets/9a74dd175a867093.svg) are the undistortion
functions that are described above for area scan cameras and $p_{v}=-S_{y}\cdot C_{y}$.

For **line scan telecentric cameras**, the following set of
equations must be solved for $\tilde{u}$ ![figure](../assets/ca7043f252367aee.svg) and $t$:
$$u( ilde{u},p_v)/Magnification = x - t \, V_x\n v( ilde{u},p_v)/Magnification = y - t \, V_y$$ ![figure](../assets/bc61c093f596a731.svg)
with $u\left(\tilde{u}, \tilde{v}\right)$ ![figure](../assets/30d919f606f819ef.svg),
$v\left(\tilde{u},\tilde{v}\right)$ ![figure](../assets/9a74dd175a867093.svg) and $p_{v}$ as
defined above. Note that neither $z$ nor $V_{z}$
influence the projection for telecentric cameras.

The above formulas already include the compensation for image
distortions.

Finally, the point is transformed into the image coordinate system,
i.e., the pixel coordinate system:

$$\mathbf{q}^{i} = \begin{pmatrix} r \\ c \end{pmatrix} = \left( \frac{\tilde{t}}{S_x} + C_x \right)$$ ![figure](../assets/678f2d317fc90b97.svg)

### Further Limitations Related to Specific Camera Types

For **pinhole cameras**, if the calibration plates are parallel
to each other in all images (in particular, if they all lie in the
same plane), it is impossible to determine `Focus` together
with all six of the external camera parameters. For example, it is
impossible to determine `Focus` and the distance of the
calibration plates to the camera in this case. To be able to
calibrate all camera parameters uniquely, make sure that you acquire
images of the calibration plate tilted in different orientations.

For **telecentric lenses**, the distance of the calibration
plate from the camera cannot be determined. Therefore, the
z-component of the resulting calibration plate pose is set to 1 m in
the calibration results. Furthermore, as described previously, for
telecentric line scan cameras, $V_{z}$ cannot be determined
and is left at its initial value, except for multi-camera setups
that have a common motion vector, in which case $V_{z}$ can
be determined.

For **tilt lenses**, the greater the lens distortion is, the
more accurately the tilt can be determined. For lenses with small
distortions, the tilt cannot be determined robustly. Therefore, the
optimized tilt parameters may differ significantly from the nominal
tilt parameters of the setup. If this is the case, please check
*`Error`*. If *`Error`* is small, the resulting camera
parameters describe the imaging geometry consistently within the
calibrated volume and can be used for accurate measurements.

For **perspective tilt lenses** and **object-side
telecentric tilt lenses**, the image plane distance can only be
determined uniquely if the tilt is not 0 degrees. The smaller the tilt, the
less accurately the image plane distance can be determined.
Therefore, the optimized image plane distance may differ
significantly from the nominal image plane distance of the setup.
If this is the case, please check *`Error`*. If *`Error`*
is small, the resulting camera parameters describe the imaging
geometry consistently within the calibrated volume and can be used
for accurate measurements.

For **perspective tilt lenses** and **object-side
telecentric tilt lenses** that are tilted around the horizontal or
vertical axis, i.e., for which the rotation angle is 0, 90, 180, or
270 degrees, the tilt angle $tilt$, scale factor $S_{x}$,
the focal length $f$ (for perspective tilt lenses) or the
magnification $m$ (for object-side telecentric tilt lenses),
and the distance of the tilted image plane from the perspective
projection center $d$ cannot be determined uniquely. In this
case, $S_{x}$ should be excluded from the optimization by
calling

[`set_calib_data(CalibDataID, 'camera', 'general', 'excluded_settings', 'sx')`](set_calib_data.md).

Additionally, note that for tilt lenses it is only possible to
determine $tilt$ and $rot$ simultaneously. This
is an implementation choice that makes the optimization numerically
more robust. Consequently, the parameters $tilt$ and
$rot$ are excluded simultaneously from the optimization by
calling

[`set_calib_data(CalibDataID, 'camera', 'general', 'excluded_settings', 'tilt')`](set_calib_data.md).

Pinhole cameras with tilt lenses with large focal lengths have
nearly telecentric projection characteristics. Therefore, as
described before, $S_{x}$ and the tilt
parameters $tilt$ and $rot$ are correlated and
can only be determined imprecisely simultaneously. In this case, it
is again advisable to exclude $S_{x}$ from the optimization.

For telecentric lenses, there are always two possible poses of a calibration
plate for a single image. Therefore, it is not possible to
decide which one of the two poses is actually present in the image.
This ambiguity also effects the tilt parameters $tilt$ and
$rot$ of a telecentric tilt lens. Consequently, depending
on the initial parameters for $tilt$ and $rot$
the camera calibration may return the alternative parameters instead
of the nominal ones. If this is the case, please check
*`Error`*. If *`Error`* is small, the resulting camera
parameters describe the imaging geometry consistently within the
calibrated volume and can be used for accurate measurements.

For **line scan cameras with the polynomial distortion model**
(for cameras with perspective as well as telecentric lenses), the
parameters $P_{1}$ and $P_{2}$ are highly correlated
with other parameters in the camera model. Therefore, they
typically cannot be determined reliably and should be excluded from
the calibration by calling

[`set_calib_data(CalibDataID, 'camera', 'general', 'excluded_settings', 'poly_tan_2')`](set_calib_data.md).

### Further Information

Learn about camera calibration any many other topics in interactive online
courses at our
[MVTec Academy](https://academy.mvtec.com/cstart/course/203).

---

#### List of Sections

- [Binocular](toc_calibration_binocular.md)
- [Calibration Object](toc_calibration_calibrationobject.md)
- [Camera Parameters](toc_calibration_cameraparameters.md)
- [Hand-Eye](toc_calibration_handeye.md)
- [Inverse Projection](toc_calibration_inverseprojection.md)
- [Monocular](toc_calibration_monocular.md)
- [Multi-View](toc_calibration_multiview.md)
- [Projection](toc_calibration_projection.md)
- [Rectification](toc_calibration_rectification.md)
- [Self-Calibration](toc_calibration_selfcalibration.md)
