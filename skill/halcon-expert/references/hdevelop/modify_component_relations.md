# modify_component_relations (Operator)

## Name

`modify_component_relations` — Modify the relations within a training result.

## Warning

**`modify_component_relations` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`modify_component_relations( : : ComponentTrainingID, ReferenceComponent, ToleranceComponent, PositionTolerance, AngleTolerance : )`

## Description

`modify_component_relations` modifies the relations between
the model components within the component training result
*`ComponentTrainingID`*. The selection of the relation(s) that
should be changed is performed by setting
*`ReferenceComponent`* and *`ToleranceComponent`*,
respectively. This means that the relative movement of component
*`ToleranceComponent`* with respect to the component
*`ReferenceComponent`* is modified.

The size of the change is specified as follows: By specifying a
position tolerance *`PositionTolerance`*, the semi-axes of the
rectangle that describes the reference point's movement (see
[`train_model_components`](train_model_components.md)) are enlarged by
*`PositionTolerance`* pixels. Accordingly, by specifying an
orientation tolerance *`AngleTolerance`*, the angle range that
describes the variation of the relative orientation (see
[`train_model_components`](train_model_components.md)) is enlarged by
*`AngleTolerance`* to both sides. Consequently, negative
tolerance values lead to a decreased size of the relations. The
operator `modify_component_relations` is particularly useful
when the training images that were used during the training do not
cover the entire spectrum of the relative movements.

In order to select the relations that should be modified, values for
*`ReferenceComponent`* and *`ToleranceComponent`* can be
passed in one of the following ways: For each of both parameters
either one value, several values, or the string *'all'* can
be passed. The following table summarizes the different
possibilities by giving the affected relations for different
combinations of parameter values. Here, four model components are
assumed (0, 1, 2, and 3). If, for example,
*`ReferenceComponent`* is set to *0* and
*`ToleranceComponent`* is set to *1*, then the relation
(0,1), which corresponds to the relative movement of component 1
with respect to component 0, will be modified.

| *`ReferenceComponent`* | *`ToleranceComponent`* | Affected Relation(s) |
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

The number of tolerance values passed in *`PositionTolerance`*
and *`AngleTolerance`* must be either 1 or be equal to the
number of affected relations. In the former case all affected
relations are modified by the same value, whereas in the latter case
each relation can be modified individually by passing different
values within a tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ComponentTrainingID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ComponentTrainingID`** (input_control, state is modified)  component_training `→`  (handle)

Handle of the training result.

**`ReferenceComponent`** (input_control)  string(-array) `→`  (string / integer)

Model component(s) relative to which the movement(s)
should be modified.

Default:
'all'

Suggested values:
'all', 0, 1, 2, 3, 4, 5, 6

**`ToleranceComponent`** (input_control)  string(-array) `→`  (string / integer)

Model component(s) of which the relative movement(s)
should be modified.

Default:
'all'

Suggested values:
'all', 0, 1, 2, 3, 4, 5, 6

**`PositionTolerance`** (input_control)  real(-array) `→`  (real)

Change of the position relation in pixels.

Suggested values:
1.0, 2.0, 3.0, 4.0, 5.0, 10.0, 20.0, 30.0

**`AngleTolerance`** (input_control)  angle.rad(-array) `→`  (real)

Change of the orientation relation in radians.

Suggested values:
0.017, 0.035, 0.052, 0.070, 0.087, 0.175, 0.349

## Result

If the handle of the training result is valid, the operator
`modify_component_relations` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
