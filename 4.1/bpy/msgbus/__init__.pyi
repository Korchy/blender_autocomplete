"""
The message bus system can be used to receive notifications when properties of
Blender datablocks are changed via the data API.


--------------------

The message bus system is triggered by updates via the RNA system. This means
that the following updates will result in a notification on the message bus:

* Changes via the Python API, for example some_object.location.x += 3

.
* Changes via the sliders, fields, and buttons in the user interface.

The following updates do not trigger message bus notifications:

* Moving objects in the 3D Viewport.
* Changes performed by the animation system.


--------------------

Below is an example of subscription to changes in the active object's location.

```../examples/bpy.msgbus.1.py```

Some properties are converted to Python objects when you retrieve them. This
needs to be avoided in order to create the subscription, by using
datablock.path_resolve("property_name", False)

:

```../examples/bpy.msgbus.2.py```

It is also possible to create subscriptions on a property of all instances of a
certain type:

```../examples/bpy.msgbus.3.py```

[NOTE]
All subscribers will be cleared on file-load. Subscribers can be re-registered on load,
see bpy.app.handlers.load_post.

"""

import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def clear_by_owner(owner):
    """Clear all subscribers using this owner."""

    ...

def publish_rna(key):
    """Notify subscribers of changes to this property
    (this typically doesn't need to be called explicitly since changes will automatically publish updates).
    In some cases it may be useful to publish changes explicitly using more general keys.

        :param key: Represents the type of data being subscribed to

    Arguments include
    - `bpy.types.Property` instance.
    - `bpy.types.Struct` type.
    - (`bpy.types.Struct`, str) type and property name.
    """

    ...

def subscribe_rna(key, owner: typing.Any | None, args, notify, options=None()):
    """Register a message bus subscription. It will be cleared when another blend file is
    loaded, or can be cleared explicitly via `bpy.msgbus.clear_by_owner`.

        :param key: Represents the type of data being subscribed to

    Arguments include
    - `bpy.types.Property` instance.
    - `bpy.types.Struct` type.
    - (`bpy.types.Struct`, str) type and property name.
        :param owner: Handle for this subscription (compared by identity).
        :type owner: typing.Any | None
        :param options: Change the behavior of the subscriber.

    PERSISTENT when set, the subscriber will be kept when remapping ID data.
    """

    ...
