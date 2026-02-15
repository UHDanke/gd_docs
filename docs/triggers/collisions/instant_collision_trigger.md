# Instant Collision Trigger

Checks the current collision state of the given Block IDs and spawns True ID and False ID accordingly.

Can be remapped and groups spawned by it inherit remaps, but resets remaps on versions before 2.208.

The collision state is only updated once per tick, Instant Collision does not check collisions, it checks what the last recorded collision state was.

Using Toggle or Silent Move with Instant Collision to do multiple checks per tick is not possible.
