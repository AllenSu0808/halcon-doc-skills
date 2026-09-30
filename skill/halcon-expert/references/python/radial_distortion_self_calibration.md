# radial_distortion_self_calibration (Operator)

## Name

`radial_distortion_self_calibration` — Calibrate the radial distortion.

## Signature

`def radial_distortion_self_calibration(contours: HObject, width: int, height: int, inlier_threshold: float, rand_seed: int, distortion_model: str, distortion_center: str, principal_point_var: float) -> Tuple[HObject, Sequence[Union[int, float, str]]]`

## Description

`radial_distortion_self_calibration` estimates the distortion
parameters and the distortion center of a lens from a set of XLD
*`contours`*.

The distortion parameters are returned in *`camera_param`*.
Because no other parameters are estimated - particularly not the focal
length or the magnification - a telecentric camera model is returned with
`Magnification` 1 and scale factor 1 for $S_{x}$ and
$S_{y}$.
See [Calibration](toc_calibration.md) for more information on the different
camera models.

**Application**

Based on the result of `radial_distortion_self_calibration`, you
can remove lens distortions from images by passing the parameter
*`camera_param`*, which contains the distortion parameters, to the
operators [`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md) and
[`change_radial_distortion_image`](change_radial_distortion_image.md).

**Basic principle**

The estimation of the distortions is based on the assumption that a
significant number of straight lines are visible in the image.
Because of lens distortions, these lines will
be projected to curved contours. The operator now determines suitable
parameters by which the curved contours can be straightened again, thus
compensating the lens distortions.

**Extract input contours**

To get suitable input contours *`contours`*, you can, e.g., use
[`edges_sub_pix`](edges_sub_pix.md) or [`lines_gauss`](lines_gauss.md).
The contours should be equally distributed
and should lie near the image border because there the degree of
distortion is at its maximum and therefore the calibration is most
stable. To improve speed and robustness, you can try to
to obtain long linear or circular segments, e.g., with
[`segment_contours_xld`](segment_contours_xld.md), [`union_collinear_contours_xld`](union_collinear_contours_xld.md),
[`union_cocircular_contours_xld`](union_cocircular_contours_xld.md), or [`select_shape_xld`](select_shape_xld.md).
If a single image does
not contain enough straight contours in the scene,
you can use the contours of multiple images ([`concat_obj`](concat_obj.md)).

**Set parameters for contour selection**

The operator automatically estimates those contours from
*`contours`* that are images of straight lines in the scene using
the robust RANSAC method. The contours that do not fulfill this
condition and hence are not suited for the calibration process are
called outliers. The operator can cope with a maximum outlier
percentage of 50 percent. A contour is classified as an outlier if
the mean deviation of the contour from its associated straight line
is, after the distortion correction, higher than a given threshold
T.
$$\frac{1}{m} \sum_{j=1}^{m} |d_j| > \text{InlierThreshold} \cdot \frac{m}{100} = T$$ ![figure](../assets/e49cbb71ef96a3be.svg)
The value *`inlier_threshold`* describes the mean deviation of a
contour from its associated line in pixels for a contour that
contains 100 points. The actual threshold T is derived from
*`inlier_threshold`* by scaling it with the reference length
(100) and the number of contour points m. Therefore, similar
contours are classified alike. Typical values of
*`inlier_threshold`* range from 0.05 to 0.5. The higher the
value, the more deviation is tolerated. By choosing the value 0, all
the contours of *`contours`* are used for the calibration
process. The RANSAC contour selection will then be suppressed to
enable a manual contour selection. This can be helpful if the
outlier percentage is higher than 50 percent.

With the parameter *`rand_seed`*, you can control the randomized
behavior of the RANSAC algorithm and force it to return reproducible
results. The parameter is passed as initial value to the internally
used random number generator. If it is set to a positive value, the
operator returns identical results for each call with identical
parameter values.
The value set for the HALCON system variable *"seed_rand"*
(see [`set_system`](set_system.md)) does not affect the results of
`radial_distortion_self_calibration`.

`radial_distortion_self_calibration` returns the contours
that were chosen for the calibration process in *`selected_contours`*.

**Select distortion model**

The distortion model used in the calibration can be selected with
the parameter *`distortion_model`*. By choosing the division model
(*`distortion_model`* = *"division"*), the distortions are
modeled by the distortion parameter $\kappa$.
By choosing the polynomial model
(*`distortion_model`* = *"polynomial"*), the
distortions are modeled by the radial distortion parameters
$K_{1},K_{2},K_{3}$ and the decentering distortion
parameters $P_{1},P_{2}$.
See [Calibration](toc_calibration.md) for details on the different camera
models.

**Set parameters for the distortion center estimation**

The starting value for the estimation of the distortion center
$c=(c_{x},c_{y})$ is the center of the image;
the image size is defined by *`width`* and *`height`*.

The distortion parameters
$(\kappa,c_{x},c_{y})$ or
$(K_{1},K_{2},K_{3},P_{1},P_{2},c_{x},c_{y})$, respectively, are estimated via the
methods *"variable"*, *"adaptive"*, or
*"fixed"*, which are specified via the parameter
*`distortion_center`*:

- **'variable'** —

  In the default mode *"variable"*,
  the distortion center c is estimated with all the other calibration
  parameters at the same time. Here, many contours should lie equally
  distributed near the image borders or the distortion should be high.
  Otherwise, the search for the distortion center could be ill-posed,
  which results in instability.
- **'adaptive'** —

  With the method *"adaptive"*,
  the distortion center c is at first fixed in the image center.
  Then, the outliers are eliminated by using the
  *`inlier_threshold`*. Finally, the calibration process is rerun
  by estimating $(\kappa,c_{x},c_{y})$ or
  $(K_{1},K_{2},K_{3},P_{1},P_{2},c_{x},c_{y})$, respectively, which will be accepted
  if $c=(c_{x},c_{y})$ results from a stable
  calibration and lies near the image center. Otherwise, c will be
  assumed to lie in the image center. This method should be used if
  the distortion center can be assumed to lie near the image center
  and if very few contours are available or the position of other
  contours is bad (e.g., the contours have the same direction or lie
  in the same image region).
- **'fixed'** —

  By choosing the method *"fixed"*,
  the distortion center will be assumed fixed in the image center and
  only $\kappa$ or
  $(K_{1},K_{2},K_{3},P_{1},P_{2})$,
  respectively, will be estimated. This method should be used in case of
  very weak distortions or few contours in bad position.

In order to control the deviation of c from the image center, the
parameter *`principal_point_var`* can be used in the methods
*"adaptive"* and *"variable"*. If the deviation from
the image center should be controlled, *`principal_point_var`*
must lie between 1 and 100. The higher the value, the more the
distortion center can deviate from the image center. By choosing
the value 0, the principal point is not controlled, i.e., the
principal point is determined solely based on the contours. The
parameter *`principal_point_var`* should be used in cases of weak
distortions or similarly oriented contours. Otherwise, a stable
solution cannot be guaranteed.

**Runtime**

The runtime of
`radial_distortion_self_calibration` is shortest for
*`distortion_center`* = *"variable"* and
*`principal_point_var`* = *0*. The runtime for
*`distortion_center`* = *"variable"* and
*`principal_point_var`* > *0* increases significantly
for smaller values of *`principal_point_var`*. The runtimes for
*`distortion_center`* = *"adaptive"* and
*`distortion_center`* = *"fixed"* are also
significantly higher than for *`distortion_center`* =
*"variable"* and *`principal_point_var`* =
*0*.

## Attention

Since the polynomial model
(*`distortion_model`* = *"polynomial"*) uses more parameters
than the division model (*`distortion_model`* = *"division"*)
the calibration using the polynomial model can be slightly less stable than
the calibration using the division model, which becomes noticeable in the
accuracy of the decentering distortion parameters $P_{1},P_{2}$.
To improve the stability, contours of multiple images can be used.
Additional stability can be achieved by setting
*`distortion_center`* = *"fixed"*,
*`distortion_center`* = *"adaptive"*, or
*`principal_point_var`* > *0*, which was already mentioned
above.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` HObject

Contours that are available for the calibration.

**`selected_contours`** (output_object)  xld_cont-array `→` HObject

Contours that were used for the calibration

**`width`** (input_control)  extent.x `→` int

Width of the images from which the contours
were extracted.

Default:
640

Suggested values:
640, 768

Restriction:
`Width > 0`

**`height`** (input_control)  extent.y `→` int

Height of the images from which the contours
were extracted.

Default:
480

Suggested values:
480, 576

Restriction:
`Height > 0`

**`inlier_threshold`** (input_control)  real `→` float

Threshold for the classification of outliers.

Default:
0.05

Suggested values:
0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1

Restriction:
`InlierThreshold >= 0`

**`rand_seed`** (input_control)  integer `→` int

Seed value for the random number generator.

Default:
42

**`distortion_model`** (input_control)  string `→` str

Determines the distortion model.

Default:
"division"

List of values:
"division", "polynomial"

**`distortion_center`** (input_control)  string `→` str

Determines how the distortion center will be
estimated.

Default:
"variable"

List of values:
"adaptive", "fixed", "variable"

**`principal_point_var`** (input_control)  real `→` float

Controls the deviation of the distortion center
from the image center; larger values allow
larger deviations from the image center; 0
switches the penalty term off.

Default:
0.0

Suggested values:
0.0, 5.0, 10.0, 20.0, 50.0, 100.0

Restriction:
`PrincipalPointVar >= 0.0 && PrincipalPointVar <= 100.0`

**`camera_param`** (output_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

## Example (HDevelop)

```
* Assume that GrayImage is one image in gray values with a
* resolution of 640 x 480 and a suitable number of contours.  Then
* the following example performs the calibration using these
* contours and corrects the image with the estimated distortion
* parameters.
edges_sub_pix (GrayImage, Edges, 'canny', 1.0, 20, 40)
segment_contours_xld (Edges, ContoursSplit, 'lines_circles', 5, 8, 4)
radial_distortion_self_calibration (ContoursSplit, SelectedContours, \
                                    640, 480, 0.08, 42, 'division', \
                                    'variable', 0, CameraParam)
get_domain (GrayImage, Domain)
change_radial_distortion_cam_par ('fullsize', CameraParam, 0, CamParamOut)
change_radial_distortion_image (GrayImage, Domain, ImageRectified, \
                                CameraParam, CamParamOut)
```

## Result

If the parameters are valid, the operator
`radial_distortion_self_calibration` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`edges_sub_pix`,
`segment_contours_xld`

## Possible Successors

`change_radial_distortion_cam_par`,
`change_radial_distortion_image`

## See also

`camera_calibration`

## References

T. Thormählen, H. Broszio: “Automatic line-based estimation of
radial lens distortion”; in: Integrated Computer-Aided
Engineering; vol. 12; pp. 177-190; 2005.

## Module

Calibration
