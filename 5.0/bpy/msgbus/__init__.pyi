"""
The message bus system can be used to receive notifications when properties of
Blender data-blocks are changed via the data API.


--------------------

The message bus system is triggered by updates via the RNA system. This means
that the following updates will result in a notification on the message bus:

* Changes via the Python API, for example some_object.location.x += 3

.
* Changes via the sliders, fields, and buttons in the user interface.

The following updates do not trigger message bus notifications:

* Moving objects in the 3D Viewport.
* Changes performed by the animation system.

Changes done from msgbus

 callbacks are not included in related undo steps,
so users can easily skip their effects by using Undo followed by Redo.

Unlike properties update

 callbacks, message bus update callbacks are postponed
until all operators have finished executing.
Additionally, for each property the callback is only triggered once per update cycle,
even if the property was changed multiple times during that period.


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
import typing_extensions
import numpy.typing as npt
import bpy.types

def clear_by_owner(owner) -> None:
    """Clear all subscribers using this owner."""

def publish_rna(
    key: bpy.types.Property | bpy.types.Struct | tuple[bpy.types.Struct, str] | None,
) -> None:
    """Notify subscribers of changes to this property
    (this typically doesnt need to be called explicitly since changes will automatically publish updates).
    In some cases it may be useful to publish changes explicitly using more general keys.

        :param key: Represents the type of data being subscribed to

    Arguments include
    - A property instance.
    - A struct type.
    - A tuple representing a (struct, property name) pair.
    """

def subscribe_rna(
    key: bpy.types.Property | bpy.types.Struct | tuple[bpy.types.Struct, str] | None,
    owner: typing.Any | None,
    args,
    notify,
    *,
    options: set[str] | None = set(),
) -> None:
    """Register a message bus subscription. It will be cleared when another blend file is
    loaded, or can be cleared explicitly via `bpy.msgbus.clear_by_owner`.

        :param key: Represents the type of data being subscribed to

    Arguments include
    - A property instance.
    - A struct type.
    - A tuple representing a (struct, property name) pair.
        :param owner: Handle for this subscription (compared by identity).
        :param options: Change the behavior of the subscriber.

    PERSISTENT when set, the subscriber will be kept when remapping ID data.
    """
