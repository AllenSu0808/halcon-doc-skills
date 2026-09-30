# find_component_model (Operator)

## Name

`find_component_model` — Find the best matches of a component model in an image.

## Warning

**`find_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`find_component_model(Image : : ComponentModelID, RootComponent, AngleStartRoot, AngleExtentRoot, MinScore, NumMatches, MaxOverlap, IfRootNotFound, IfComponentNotFound, PosePrediction, MinScoreComp, SubPixelComp, NumLevelsComp, GreedinessComp : ModelStart, ModelEnd, Score, RowComp, ColumnComp, AngleComp, ScoreComp, ModelComp)`

## Description

The operator `find_component_model` finds the best
*`NumMatches`* instances of the component model
*`ComponentModelID`* in the input image *`Image`*.

The result of the search can be visualized using
[`get_found_component_model`](get_found_component_model.md).
Also the operator can be used to extract the component matches
of a certain component model instance.

### Further information about input parameters

- ***`ComponentModelID`*:** —

  Handle of the component model.

  The model must have been created previously by calling
  [`create_trained_component_model`](create_trained_component_model.md) or
  [`create_component_model`](create_component_model.md), or read in using
  [`read_component_model`](read_component_model.md).
- ***`RootComponent`*:** —

  Index of the root component.

  The components of the component model *`ComponentModelID`* are
  represented in a tree structure. The component that stands at the
  root of this search tree is the root component.

  The root component is searched within the full parameter space,
  i.e., at all allowed positions and in the allowed
  range of orientations (see below).
  In contrast, the remaining components are searched relative to the pose
  of their predecessor in the search tree within a restricted parameter space
  that is computed from the relations (recursive search).

  To what extent a model component is suited to act as root component depends
  on several factors. In principle, a model component that can be found
  in the image with a high probability, should be chosen. Therefore, a
  component that is sometimes occluded to a high degree or that is
  missing in some cases is not well suited to act as root
  component.
  For the behavior in such cases, see the entry *`IfRootNotFound`*
  below.

  A different possible criterion is the computation time
  that is associated with the root component during the search.
  A ranking of the model components that is
  based on the latter criterion is returned in `RootRanking`
  of the operator [`create_trained_component_model`](create_trained_component_model.md) or
  [`create_component_model`](create_component_model.md), respectively.
  If the complete ranking is passed in *`RootComponent`*,
  the first value *`RootComponent`*[0] is automatically selected
  as the root component.
- ***`AngleStartRoot`* and *`AngleExtentRoot`*:** —

  Specify the allowed angle range (in [rad]) within which the root
  component is searched.

  If necessary, the range of rotations
  is clipped to the range given when the component model was created
  with [`create_trained_component_model`](create_trained_component_model.md) or
  [`create_component_model`](create_component_model.md), respectively.
  The angle range for each component can be queried with
  [`get_shape_model_params`](get_shape_model_params.md).
  The necessary handle of the corresponding shape model can be obtained using
  [`get_component_model_params`](get_component_model_params.md).
- ***`MinScore`*:** —

  Determines what score a potential match of the component model must at
  least have to be regarded as an instance.

  If the component model can be expected never to be occluded in the images,
  *`MinScore`* may be set as high as *0.8* or even *0.9*.
  The value of this parameter only slightly influences the computation time.
  An exception is the case of *`IfRootNotFound`* set to
  *'select_new_root'* (see below).
- ***`NumMatches`*:** —

  Determines the maximum number of returned instances.

  If fewer than *`NumMatches`* are found, only that number is
  returned, i.e., the parameter *`MinScore`* takes precedence
  over *`NumMatches`*.
  In case more than *`NumMatches`* instances with a score greater than
  *`MinScore`* are found in the image, only the best
  *`NumMatches`* instances are returned.
  However, if all model instances exceeding *`MinScore`* in the image
  should be found, *`NumMatches`* must be set to *0*.
- ***`MaxOverlap`*:** —

  Determines by what fraction two instances may at most overlap,
  whereby this fraction is a number between 0 and 1.

  In some cases, found instances only differ in the pose of one or a few
  components.
  If two instances overlap each other by more than
  *`MaxOverlap`* only the best instance is returned.
  This means, for *`MaxOverlap`* = *0*, the found instances may
  not overlap at all, while for *`MaxOverlap`* = *1* no check for
  overlap is performed, and hence all instances are returned.
  The calculation of the overlap is based on the smallest enclosing
  rectangles of arbitrary orientation (see [`smallest_rectangle2`](smallest_rectangle2.md))
  of the found component instances.
- ***`IfRootNotFound`*:** —

  specifies the behavior of the operator when dealing with
  a missing or strongly occluded root component.

  Possible values:

  - *'stop_search'*:
    It is assumed that the root component is always found in the image.
    Consequently, for instances for which the root component could not
    be found the search for the remaining components is not continued.
  - *'select_new_root'*:
    Different components are successively chosen as the root component
    and searched within the full search space.
    The order in which the selection of the root component is performed
    corresponds to the order passed in `RootRanking`.
    The poses of the found instances of all root components are then used
    to start the recursive search for the remaining components.
    Hence, it is possible to find instances even if the original root
    component is not found.
    However, the computation time of the search increases significantly
    in comparison to the search when choosing *'stop_search'*.
    This is especially the case for small values of *`MinScore`*,
    as more root components must be searched.
    If during the search more root components are needed as given in
    *`RootComponent`*, the root components are completed by
    the automatically computed order
    (see [`create_trained_component_model`](create_trained_component_model.md) or
    [`create_component_model`](create_component_model.md)).
- ***`IfComponentNotFound`*:** —

  Specifies how components are searched when the predecessor component
  was not found (e.g., because she is missing or strongly occluded).

  Possible values:

  - *'prune_branch'*:
    Such components are not searched at all and are also treated as
    'not found'.
  - *'search_from_upper'*:
    Such components are searched relative to the pose of the predecessor
    component of the predecessor component.
  - *'search_from_best'*:
    Such components are searched relative to the pose of the already found
    component from which the relative search can be performed with minimum
    computational effort.
- ***`PosePrediction`*:** —

  Determines whether the pose of not found components should be estimated.

  Possible values:

  - *'none'*:
    Only the poses of the found components are returned.
  - *'from_neighbors'*:
    The poses of not found components are estimated and returned with a score
    of *`ScoreComp`* = *0.0*.
    The pose estimation is based on the poses of the found neighboring
    components in the search tree.
  - *'from_all'*:
    The poses of not found components are estimated and returned with a score
    of *`ScoreComp`* = *0.0*.
    The pose estimation is based on the poses of all found components.
- ***`MinScoreComp`*:** —

  Minimal necessary score of the components for the instances to be found.

  This parameter has the same meaning as `MinScore` in
  [`find_shape_model`](find_shape_model.md).

  Settable is either one element or the same number of elements as model
  components in *`ComponentModelID`*.
  In the first case the parameter is used for all components.
  In the second case, each parameter element refers to the corresponding
  component in *`ComponentModelID`*.
- ***`SubPixelComp`*:** —

  Determines whether the extraction shall be done subpixel precise
  and in the given case the maximal allowed object deformation in pixels.

  This parameter has the same meaning as `SubPixel` in
  [`find_shape_model`](find_shape_model.md).
  Therefore the maximal allowed object deformation has to be given as
  integer in the same string.
  Settable is either one element or the same number of elements as model
  components in *`ComponentModelID`*.
  In the first case the parameter is used for all components.
  In the second case, each parameter element refers to the corresponding
  component in *`ComponentModelID`*.

  *Example:* *['least_squares', 'max_deformation 2']*.
- ***`NumLevelsComp`*:** —

  Determine the pyramid levels for the components used in the matching.

  This parameter has the same meaning as `NumLevels` in
  [`find_shape_model`](find_shape_model.md).

  It determines the number of pyramid levels for the components
  to be used in the matching.
  Settable is either one element or the same number of elements as model
  components in *`ComponentModelID`*.
  In the first case the parameter is used for all components.
  In the second case, each parameter element refers to the corresponding
  component in *`ComponentModelID`*.

  Optional, one can set value pairs for this parameter:
  In this case, the first value still determines the number of pyramid levels
  to be used.
  The second value specifies the lowest pyramid level, to which the found
  matches are tracked.
  In doing so, one can set either a single value pair or a value pair for each
  model component in *`ComponentModelID`*.
  If different value pairs should be used for different components, they must
  be specified in the same tuple.
  In case *`ComponentModelID`* contains exactly two components and in
  *`NumLevelsComp`* two values are set, these values are interpreted as
  different number of pyramid levels to be used and not as a value pair.

  *Example:* *`ComponentModelID`* contains two components, for
  which different pyramid levels shall be considered.
  For the first component 5 levels up to the level 2 shall be used.
  For the second component 4 levels up to the level 1 shall be used.
  In this case is *`NumLevelsComp`* = *[5,2,4,1]*.
- ***`GreedinessComp`*:** —

  “Greediness” of the search heuristic for the components: value from 0 to
  1. Thereby 0 means: safe but slow, 1: fast but matches may be missed.

  This parameter has the same meaning as `Greediness` in
  [`find_shape_model`](find_shape_model.md).

  Settable is either one element or the same number of elements as model
  components in *`ComponentModelID`*.
  In the first case the parameter is used for all components.
  In the second case, each parameter element refers to the corresponding
  component in *`ComponentModelID`*.

### Further information about output parameters

- ***`ModelStart`* and *`ModelEnd`*:** —

  Return the first and last index and therewith the index range
  of all component matches associated to the same instance of the
  component model.

  The component matches corresponding to the first found instance of the
  component model are given by the interval of indices
  [*`ModelStart`*[0],*`ModelEnd`*[0]].
  Thereby the indices refer to the values of the parameters *`RowComp`*,
  *`ColumnComp`*, *`AngleComp`*, *`ScoreComp`*, and
  *`ModelComp`*.

  *Example:* The component model consists for three components.
  Two instances have been found on the image, where for one instance only two
  components (component 0 and component 2) could be found.
  Then the returned parameters could look like this:

  |  |  |
  | --- | --- |
  | *`RowComp`* = *[100,200,300,150,250]* | *`ModelStart`* = *[0,3]* |
  | *`ColumnComp`* = *[200,210,220,400,425]* | *`ModelEnd`* = *[2,4]* |
  | *`AngleComp`* = *[0,0.1,-0.2,0.1,0.2]* | *`ModelComp`* = *[0,1,2,0,2]* |
  | *`ScoreComp`* = *[1,1,1,1,1]* | *`Score`* = *[1,1]* |
  |  |

  From the right column it is visible, that in the left column:
  - Values with index 0 to 2 correspond to the components 0 to 2 of
    instance 1.
  - Values with index 3 to 4 correspond to the components 0 and 2 of
    instance 2.
- ***`Score`*:** —

  Score of the found instances of the component model.

  *`Score`* contains the weighted mean of the component scores,
  the values in *`ScoreComp`*.
  The weighting is performed according to the number of model points
  within the respective component.
- ***`RowComp`*, *`ColumnComp`*, and *`AngleComp`*:** —

  The position (*`RowComp`*, *`ColumnComp`*) and rotation
  (*`AngleComp`*) of the model components of all found component
  model instances.

  The coordinates *`RowComp`* and *`ColumnComp`* are the
  coordinates of the component origin (reference point) in
  the search image.
  The component origin depends on the model creation:

  - with [`create_trained_component_model`](create_trained_component_model.md) by training:
    The component origin is the center of gravity of the respective
    returned contour region in `ModelComponents` of the operator
    [`train_model_components`](train_model_components.md).
  - with [`create_component_model`](create_component_model.md) manually:
    The component origin is the center of gravity of the corresponding
    passed component region `ComponentRegions` of the operator
    [`create_component_model`](create_component_model.md).

  Since the relations between the components in *`ComponentModelID`*
  refer to this reference point, the origin of the components must not be
  modified by using [`set_shape_model_origin`](set_shape_model_origin.md).
- ***`ScoreComp`*:** —

  Score of each found component instance.

  The score is a number between 0 and 1, and is an approximate measure of how
  much of the component is visible in the image.
  If, for example, half of the component is occluded, the score cannot exceed
  0.5.
- ***`ModelComp`*:** —

  Index of the found component.

  The tuple contains the indices of the respective model components
  (see [`create_component_model`](create_component_model.md) and [`train_model_components`](train_model_components.md),
  respectively).
  By this the values in *`RowComp`*, *`ColumnComp`*,
  *`AngleComp`*, and *`ScoreComp`* can be associated
  to the different model components.
  See also the example given for *`ModelStart`* and *`ModelEnd`*.

### Information concerning the search

Internally, the shape-based matching is used for the component-based
matching in order to search the individual components
(see [`find_shape_model`](find_shape_model.md)).

The domain of the *`Image`* determines the search space for the
reference point, i.e., the allowed positions, of the root component.

Usually the component model is searched only within those points of the
image domain in which the model fits completely into the image.
This means that the components will not be found if they extend beyond the
borders of the image, even if they would achieve a score greater than
*`MinScoreComp`* (see above).

Note that, if for a certain pyramid level the component model touches the
image border, it might not be found even if it lies completely within the
original image.
As a rule of thumb, the model might not be found if its distance to
an image border falls below $2^{NumLevels-1}$.
This behavior can be changed with
`set_system('border_shape_models','true')`, which will cause
components that extend beyond the image border to be found if they achieve
a score greater than *`MinScoreComp`*.
Here, points lying outside the image are regarded as being occluded, i.e.,
they lower the score.
It should be noted that this mode increases the runtime of the search.

Note further, that in rare cases, which occur typically only for artificial
images, the model might not be found also if for certain pyramid levels the
model touches the border of the reduced domain. Then, it may help to
enlarge the reduced domain by $2^{NumLevels-1}$ using,
e.g., [`dilation_circle`](dilation_circle.md).

When tracking the matches through the image pyramid, on each level,
some less promising matches are rejected based on *`NumMatches`*. Thus,
it is possible that some matches are rejected that would have had a higher
score on the lowest pyramid level. Due to this, for example, the found
match for *`NumMatches`* set to *1* might be
different from the match with the highest score returned when setting
*`NumMatches`* to *0* or > *1*.

### Recommendations

If multiple objects with a similar score are expected, but only the one
with the highest score should be returned, it might be preferable to raise
*`NumMatches`*, and then select the match with the highest score.

To get a meaningful score value and to avoid erroneous matches,
we recommend to always combine the allowance of a deformation with a
subpixel extraction that applies a least-squares adjustment.
If the subpixel extraction and/or the maximum object deformation is
specified separately for each component, for each component in
*`ComponentModelID`* exactly one value for the subpixel extraction
must be passed in *`SubPixelComp`*.
After each value for the subpixel extraction optionally a second value can
be passed, which describes the maximum object deformation of the
corresponding mode. If for a certain component no value for the maximum
object deformation is passed, the component is searched without taking
deformations into account.
Further details can be found in the documentation of
[`find_shape_models`](find_shape_models.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte / uint2)

Input image in which the component model should be
found.

**`ComponentModelID`** (input_control)  component_model `→`  (handle)

Handle of the component model.

**`RootComponent`** (input_control)  integer(-array) `→`  (integer)

Index of the root component.

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8

**`AngleStartRoot`** (input_control)  angle.rad(-array) `→`  (real)

Smallest rotation of the root component

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`AngleExtentRoot`** (input_control)  angle.rad(-array) `→`  (real)

Extent of the rotation of the root component.

Default:
0.79

Suggested values:
6.28, 3.14, 1.57, 0.79, 0.39, 0.0

Restriction:
`AngleExtentRoot >= 0`

**`MinScore`** (input_control)  real `→`  (real)

Minimum score of the instances of the component
model to be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MinScore && MinScore <= 1`

**`NumMatches`** (input_control)  integer `→`  (integer)

Number of instances of the component model to be
found (or 0 for all matches).

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20

**`MaxOverlap`** (input_control)  real `→`  (real)

Maximum overlap of the instances of the
component models to be found.

Default:
0.5

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MaxOverlap && MaxOverlap <= 1`

**`IfRootNotFound`** (input_control)  string `→`  (string)

Behavior if the root component is missing.

Default:
'stop_search'

List of values:
'select_new_root', 'stop_search'

**`IfComponentNotFound`** (input_control)  string `→`  (string)

Behavior if a component is missing.

Default:
'prune_branch'

List of values:
'prune_branch', 'search_from_best', 'search_from_upper'

**`PosePrediction`** (input_control)  string `→`  (string)

Pose prediction of components that are not found.

Default:
'none'

List of values:
'from_all', 'from_neighbors', 'none'

**`MinScoreComp`** (input_control)  real(-array) `→`  (real)

Minimum score of the instances of the components to
be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= MinScoreComp && MinScoreComp <= 1`

**`SubPixelComp`** (input_control)  string(-array) `→`  (string)

Subpixel accuracy of the component poses if not
equal to *'none'*.

Default:
'least_squares'

Suggested values:
'none', 'interpolation', 'least_squares', 'least_squares_high', 'least_squares_very_high', 'max_deformation 1', 'max_deformation 2', 'max_deformation 3', 'max_deformation 4', 'max_deformation 5', 'max_deformation 6'

**`NumLevelsComp`** (input_control)  integer(-array) `→`  (integer)

Number of pyramid levels for the components used in
the matching
(and lowest pyramid level to use if
|*`NumLevelsComp`*| = 2n).

Default:
0

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`GreedinessComp`** (input_control)  real(-array) `→`  (real)

“Greediness” of the search heuristic for the
components (0: safe
but slow; 1: fast but matches may be missed).

Default:
0.9

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.05

Restriction:
`0 <= GreedinessComp && GreedinessComp <= 1`

**`ModelStart`** (output_control)  integer(-array) `→`  (integer)

Start index of each found instance of the component
model in the tuples describing the component matches.

**`ModelEnd`** (output_control)  integer(-array) `→`  (integer)

End index of each found instance of the component
model in the tuples describing the component matches.

**`Score`** (output_control)  real(-array) `→`  (real)

Score of the found instances of the component model.

**`RowComp`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the found component matches.

**`ColumnComp`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of the found component matches.

**`AngleComp`** (output_control)  angle.rad(-array) `→`  (real)

Rotation angle of the found component matches.

**`ScoreComp`** (output_control)  real(-array) `→`  (real)

Score of the found component matches.

**`ModelComp`** (output_control)  integer(-array) `→`  (integer)

Index of the found components.

## Result

If the parameter values are correct, the operator
`find_component_model` returns the value 2 (
H_MSG_TRUE)
. If the input
is empty (no input image available) the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Module

Matching
