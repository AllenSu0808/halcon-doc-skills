## Deep Counting

List of Operators ↓

This chapter explains how to use Deep Counting.

Deep Counting is used to find objects in images and returns
the number of objects.

![figure](../assets/1621db827d9908c1.svg)

A possible example for a Deep Counting application:
Objects in an image are counted and the object quantity is returned.

Deep Counting uses user-defined templates to prepare a Deep Counting model.
This model can be used to count objects that resemble the templates.

The general workflow is described in the following section.

### General Workflow

This paragraph describes how to obtain the number from objects of a kind
in images using a Deep Counting model.
An application scenario can be seen in the HDevelop example
`deep_counting_workflow.hdev`

1. Create a Deep Counting model by using

   - [`CreateDeepCountingModel`](create_deep_counting_model.md).
2. Query the available DL devices for inference by using

   - [`QueryAvailableDlDevices`](query_available_dl_devices.md).
3. Set the model parameters, the used devices
   or augmentation parameters for the templates using

   - [`SetDeepCountingModelParam`](set_deep_counting_model_param.md).
4. Draw templates for the preparation of the model.
   This can be done using the procedure

   - `draw_deep_counting_templates`.

   The drawn templates are needed for the operator
   [`PrepareDeepCountingModel`](prepare_deep_counting_model.md).
5. Prepare the model for the inference using

   - [`PrepareDeepCountingModel`](prepare_deep_counting_model.md).

   Note that when changing parameters that influence the template creation,
   or when other templates should be used, [`PrepareDeepCountingModel`](prepare_deep_counting_model.md)
   must be called again, before the model can be applied
   with [`ApplyDeepCountingModel`](apply_deep_counting_model.md).
6. Apply the model using the operator

   - [`ApplyDeepCountingModel`](apply_deep_counting_model.md).

   The result will be saved in *`deepCountingResult`*.
7. Visualize the Deep Counting results from *`deepCountingResult`*
   using the procedure

   - `dev_display_deep_counting_results`.

---

#### List of Operators

- [`ApplyDeepCountingModel`](apply_deep_counting_model.md) — Apply a Deep Counting model on a set of images for inference.

- [`CreateDeepCountingModel`](create_deep_counting_model.md) — Create a Deep Counting model for counting objects.

- [`GetDeepCountingModelParam`](get_deep_counting_model_param.md) — Return the parameters of a Deep Counting model.

- [`PrepareDeepCountingModel`](prepare_deep_counting_model.md) — Set templates of a Deep Counting model.

- [`ReadDeepCountingModel`](read_deep_counting_model.md) — Read a Deep Counting model from a file.

- [`SetDeepCountingModelParam`](set_deep_counting_model_param.md) — Set selected parameters of the Deep Counting model.

- [`WriteDeepCountingModel`](write_deep_counting_model.md) — Write a Deep Counting model in a file.
