// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from lr_interfaces:srv/Height.idl
// generated code does not contain a copyright notice

#ifndef LR_INTERFACES__SRV__DETAIL__HEIGHT__STRUCT_H_
#define LR_INTERFACES__SRV__DETAIL__HEIGHT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Height in the package lr_interfaces.
typedef struct lr_interfaces__srv__Height_Request
{
  int32_t target_height;
} lr_interfaces__srv__Height_Request;

// Struct for a sequence of lr_interfaces__srv__Height_Request.
typedef struct lr_interfaces__srv__Height_Request__Sequence
{
  lr_interfaces__srv__Height_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lr_interfaces__srv__Height_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Height in the package lr_interfaces.
typedef struct lr_interfaces__srv__Height_Response
{
  int32_t current_height;
  int32_t days;
} lr_interfaces__srv__Height_Response;

// Struct for a sequence of lr_interfaces__srv__Height_Response.
typedef struct lr_interfaces__srv__Height_Response__Sequence
{
  lr_interfaces__srv__Height_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lr_interfaces__srv__Height_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LR_INTERFACES__SRV__DETAIL__HEIGHT__STRUCT_H_
