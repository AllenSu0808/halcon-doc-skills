# ReadAopKnowledge (Operator)

## Name

`ReadAopKnowledge` — Load knowledge about hardware dependent behavior of automatic operator
parallelization.

## Signature

`static void HOperatorSet.ReadAopKnowledge(HTuple fileName, HTuple genParamName, HTuple genParamValue, out HTuple attributes, out HTuple operatorNames)`

`static HTuple HSystem.ReadAopKnowledge(string fileName, HTuple genParamName, HTuple genParamValue, out HTuple operatorNames)`

`static HTuple HSystem.ReadAopKnowledge(string fileName, string genParamName, string genParamValue, out string operatorNames)`

## Description

`ReadAopKnowledge` loads the automatic operator parallelization
(AOP) knowledge of HALCON operators from file. The knowledge is used to
better utilize multiprocessor hardware in order to speed up the processing
of operators. To optimize the automatic operator parallelization,
HALCON needs some knowledge about the speed of operators on the used
hardware. This hardware-specific knowledge
can be obtained and stored by calling the operator [`OptimizeAop`](optimize_aop.md)
and [`WriteAopKnowledge`](write_aop_knowledge.md), respectively.

With `ReadAopKnowledge`, it is possible to load this knowledge
explicitly from a binary file. In doing so, *`fileName`* denotes the
name of this file (incl. path and file extension). If an empty string
*""* is passed to *`fileName`*, HALCON reads the knowledge
from the specific file `.aop_info` in the HALCON installation
directory (Linux) or within the common application data folder
(Windows). This file is read by HALCON automatically during the
initialization phase but can easily be re-read by
`ReadAopKnowledge`. The read knowledge updates the system's
parallelization information and can be controlled by pairs of additional
parameter values passed to *`genParamName`* and *`genParamValue`*.
Every entry in *`genParamName`* must have one corresponding,
specifying entry in *`genParamValue`*, meaning that the tuples
passed to the parameters must have the same length. *`genParamName`*
supports the values in following list, describing the possible applicable
values for *`genParamValue`*:

- ***"ignore_attrib"*** —

  suppresses to check knowledge attributes.
  E.g., while reading the file `ReadAopKnowledge` checks whether
  its content was written for the currently used computer and whether the
  contained parallelization information regards the currently used HALCON
  version, revision, and architecture. The attributes to suppress are
  specified by passing any of the following values to
  *`genParamValue`*:

  - ***"host"*** —

    the host name of the current machine
  - ***"cpu_info"*** —

    the machine topology information
  - ***"variant"*** —

    the HALCON variant
  - ***"version"*** —

    the HALCON version
  - ***"revision"*** —

    the HALCON revision
  - ***"architecture"*** —

    the HALCON architecture

  Multiple suppressions of attribute checks are possible.
- ***"mode"*** —

  sets the way how the system's information gets
  updated.

  - ***"truncate"*** —

    for *`genParamValue`* deletes
    all the existing information before the new knowledge loaded from file
    is added.
  - ***"renew"*** —

    overwrites existing knowledge and adds new one
    (default).
  - ***"append"*** —

    keeps all existing operator information and just
    adds the knowledge not already contained.
  - ***"nil"*** —

    refuses any updates but returns the
    knowledge attributes in *`attributes`* and all the operators
    contained in file in *`operatorNames`*.
- ***"operator"*** —

  denotes that the corresponding index value of
  *`genParamValue`* contains an operator name. Multiple definitions
  of operators are possible. By default, information of any contained
  operator is loaded.
- ***"iconic_type"*** —

  focuses on AOP information for a specific
  iconic type, specified by following values of *`genParamValue`*:
  *"byte"*,*"uint2"*,*"real"*,*"int1"*,
  *"int2"*,*"int4"*,*"int8"*,*"direction"*,
  *"vector_field"*,*"cyclic"*,*"vector_field"*,
  *"complex"*,*"region"*,*"xld"*. Multiple definitions
  of iconic types are possible.

The names of updated operators are returned in *`operatorNames`*,
the attributes of the read knowledge in *`attributes`*. The latter
tuple codes the following meaning by index beginning with index 0 in
corresponding order: host name, HALCON variant, HALCON version,
HALCON revision, HALCON architecture.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of knowledge file

Default:
""

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter name

Default:
"none"

Suggested values:
"none", "ignore_attrib", "operator", "iconic_type", "mode"

**`genParamValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Parameter value

Number of elements:
GenParamName == GenParamValue

Default:
"none"

Suggested values:
"none", "host_name", "variant", "architecture", "version", "revision", "byte", "int1", "int2", "uint2", "int4", "int8", "direction", "cyclic", "vector_field", "complex", "region", "xld", "xld_cont", "xld_poly", "nil", "truncate", "replace", "renew", "append"

**`attributes`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Knowledge attributes

**`operatorNames`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Updated Operators

## Result

`ReadAopKnowledge` returns 2 (
H_MSG_TRUE)
if all parameters are correct and
the file could be read. If necessary, an exception is raised.

## Module

Foundation
