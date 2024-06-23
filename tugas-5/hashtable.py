from typing import Any, Optional


class HashTable:
    def __init__(self, collision_resolution="linear"):
        self.size = 256
        self.slots = [[] for i in range(self.size)]
        self.MAXLOADFACTOR = 0.65
        self.collision_resolution = collision_resolution

    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    def separate_chaining(
        self, slots: list[list[tuple[Any, Any]]], hashedkey: int, key
    ):
        chain = slots[hashedkey]
        for i, (k, v) in enumerate(chain):
            if k == key:
                return hashedkey, i
        return hashedkey, len(chain)

    def linear(
        self, slots: list[Optional[tuple[Any, Any]]], hashedkey: int, key
    ) -> tuple[int, Any]:
        if slots[hashedkey]:
            if slots[hashedkey][0] != key:  # type: ignore
                return self.linear(slots, (hashedkey + 1) % len(slots), key)
        return hashedkey, key

    def quadratic(
        self, slots: list[Optional[tuple[Any, Any]]], hashedkey: int, key, i: int = 1
    ) -> tuple[int, Any]:
        if slots[hashedkey]:
            if slots[hashedkey][0] != key:  # type: ignore
                hashedkey += i ^ 2
                return self.quadratic(slots, hashedkey % len(slots), key, i + 1)
        return hashedkey, key

    def double_hashing(
        self, slots: list[Optional[tuple[Any, Any]]], hashedkey: int, key, i: int = 1
    ) -> tuple[int, Any]:
        if slots[hashedkey]:
            if slots[hashedkey][0] != key:  # type: ignore
                step = 7 - (hash(key) % 7)
                hashedkey += i * step
                hashedkey %= self.size
                return self.double_hashing(slots, hashedkey % len(slots), key, i + 1)
        return hashedkey, key

    collision_resolutions = {
        "separate_chaining": separate_chaining,
        "linear": linear,
        "quadratic": quadratic,
        "double_hashing": double_hashing,
    }

    def put(self, key, val):
        self.check_growth()
        hashedkey = self.collision_resolutions[self.collision_resolution](
            self, self.slots, self._hash(key), key
        )
        if self.collision_resolution == "separate_chaining":
            chain = self.slots[hashedkey[0]]
            if hashedkey[1] == len(chain):
                chain.append((key, val))
            else:
                chain[hashedkey[1]] = (key, val)
        else:
            self.slots[hashedkey[0]] = (key, val)

    def get(self, key):
        hashedkey = self.collision_resolutions[self.collision_resolution](
            self, self.slots, self._hash(key), key
        )
        if self.collision_resolution == "separate_chaining":
            chain = self.slots[hashedkey[0]]
            if hashedkey[1] < len(chain):
                return chain[hashedkey[1]][1]
        else:
            return self.slots[hashedkey[0]][1] if self.slots[hashedkey[0]] else None

    def growth(self):
        New_Hash_Table = HashTable(collision_resolution=self.collision_resolution)
        New_Hash_Table.size = 2 * self.size
        New_Hash_Table.slots = [[] for i in range(New_Hash_Table.size)]
        for i in range(self.size):
            if self.collision_resolution == "separate_chaining":
                for key, value in self.slots[i]:
                    New_Hash_Table.put(key, value)
            elif self.slots[i]:
                New_Hash_Table.put(self.slots[i][0], self.slots[i][1])  # type: ignore
        self.size = New_Hash_Table.size
        self.slots = New_Hash_Table.slots

    def check_growth(self):
        if self.collision_resolution == "separate_chaining":
            total_pairs = sum(len(chain) for chain in self.slots)
            loadfactor = total_pairs / self.size
        else:
            total_pairs = len(list(filter(lambda x: bool(x), self.slots)))  # type: ignore
            loadfactor = total_pairs / self.size

        if loadfactor > self.MAXLOADFACTOR:
            print(
                "Load factor before growing the hash table:",
                loadfactor,
            )
            self.growth()
            if self.collision_resolution == "separate_chaining":
                total_pairs = sum(len(chain) for chain in self.slots)
                loadfactor = total_pairs / self.size
            else:
                total_pairs = len(list(filter(lambda x: bool(x), self.slots)))  # type: ignore
                loadfactor = total_pairs / self.size
            print(
                "Load factor after growing the hash table:",
                loadfactor,
            )

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)
