# ModifyComponentRelations (Operator)

## Name

`ModifyComponentRelations` — Modify the relations within a training result.

## Warning

**`ModifyComponentRelations` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.ModifyComponentRelations(HTuple componentTrainingID, HTuple referenceComponent, HTuple toleranceComponent, HTuple positionTolerance, HTuple angleTolerance)`

`void HComponentTraining.ModifyComponentRelations(HTuple referenceComponent, HTuple toleranceComponent, HTuple positionTolerance, HTuple angleTolerance)`

`void HComponentTraining.ModifyComponentRelations(string referenceComponent, string toleranceComponent, double positionTolerance, double angleTolerance)`

## Description

`ModifyComponentRelations` modifies the relations between
the model components within the component training result
*`componentTrainingID`*. The selection of the relation(s) that
should be changed is performed by setting
*`referenceComponent`* and *`toleranceComponent`*,
respectively. This means that the relative movement of component
*`toleranceComponent`* with respect to the component
*`referenceComponent`* is modified.

The size of the change is specified as follows: By specifying a
position tolerance *`positionTolerance`*, the semi-axes of the
rectangle that describes the reference point's movement (see
[`TrainModelComponents`](train_model_components.md)) are enlarged by
*`positionTolerance`* pixels. Accordingly, by specifying an
orientation tolerance *`angleTolerance`*, the angle range that
describes the variation of the relative orientation (see
[`TrainModelComponents`](train_model_components.md)) is enlarged by
*`angleTolerance`* to both sides. Consequently, negative
tolerance values lead to a decreased size of the relations. The
operator `ModifyComponentRelations` is particularly useful
when the training images that were used during the training do not
cover the entire spectrum of the relative movements.

In order to select the relations that should be modified, values for
*`referenceComponent`* and *`toleranceComponent`* can be
passed in one of the following ways: For each of both parameters
either one value, several values, or the string *"all"* can
be passed. The following table summarizes the different
possibilities by giving the affected relations for different
combinations of parameter values. Here, four model components are
assumed (0, 1, 2, and 3). If, for example,
*`referenceComponent`* is set to *0* and
*`toleranceComponent`* is set to *1*, then the relation
(0,1), which corresponds to the relative movement of component 1
with respect to component 0, will be modified.

| *`referenceComponent`* | *`toleranceComponent`* | Affected Relation(s) |
| --- | --- | --- |
|  |  |  |
| 'all' | 'all' | (0,1) (0,2) (0,3) |
|  |  | (1,0) (1,2) (1,3) |
|  |  | (2,0) (2,1) (2,3) |
|  |  | (3,0) (3,1) (3,2) |
|  |  |  |
| 'all' | [1,2] | (0,1) (0,2) |
|  |  | (1,2) |
|  |  | (2,1) |
|  |  | (3,1) (3,2) |
|  |  |  |
| [0,1] | 'all' | (0,1) (0,2) (0,3) |
|  |  | (1,0) (1,2) (1,3) |
|  |  |  |
| 0 | 1 | (0,1) |
|  |  |  |
| 0 | [1,2] | (0,1) (0,2) |
|  |  |  |
| [0,1] | 2 | (0,2) (1,2) |
|  |  |  |
| [0,1,2] | [1,2,3] | (0,1) (1,2) (2,3) |

The number of tolerance values passed in *`positionTolerance`*
and *`angleTolerance`* must be either 1 or be equal to the
number of affected relations. In the former case all affected
relations are modified by the same value, whereas in the latter case
each relation can be modified individually by passing different
values within a tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- componentTrainingID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`componentTrainingID`** (input_control, state is modified)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

**`referenceComponent`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Model component(s) relative to which the movement(s)
should be modified.

Default:
"all"

Suggested values:
"all", 0, 1, 2, 3, 4, 5, 6

**`toleranceComponent`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Model component(s) of which the relative movement(s)
should be modified.

Default:
"all"

Suggested values:
"all", 0, 1, 2, 3, 4, 5, 6

**`positionTolerance`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Change of the position relation in pixels.

Suggested values:
1.0, 2.0, 3.0, 4.0, 5.0, 10.0, 20.0, 30.0

**`angleTolerance`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Change of the orientation relation in radians.

Suggested values:
0.017, 0.035, 0.052, 0.070, 0.087, 0.175, 0.349

## Result

If the handle of the training result is valid, the operator
`ModifyComponentRelations` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
