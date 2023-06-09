from dataclasses import dataclass


# @dataclass
# class Entity:
#     key: object = None
#     value: object = None


@dataclass
class HashMap:
    class Node:
        data: object = None
        next: object = None

    class Entity:
        key: object = None
        value: object = None

    class Bucket:
        head: object = None

        def add(self, key, value):
            new_node = HashMap.Node()
            new_node.data = HashMap.Entity()
            new_node.data.key = key
            new_node.data.value = value
            # entity = HashMap.Entity()
            # entity.key = key
            # entity.value = value
            # new_node.data = entity
            if not self.head:
                self.head = new_node
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        def print_list(self):
            current = self.head
            while current:
                print(current.data.key, current.data.value, end=' ')
                current = current.next


# @dataclass
# class Node:
#     data: HashMap.Entity() = None
#     next: object = None


arr = HashMap.Bucket()
[arr.add(i, i + 10) for i in range(1, 10)]
arr.print_list()

"""
package ru.geekbrains.lesson4;

public class HashMap<K, V> {

    private static final int INIT_BUCKET_COUNT = 16;

    private Bucket[] buckets;

    class Entity{
        K key;
        V value;
    }

    class Bucket<K, V>{

        Node head;
        class Node{
            Node next;
            Entity value;
        }

        /**
         * Добавление нового элемента
         * @param entity Элемент (ключ-значение)
         * @return
         */
        public V add(Entity entity){
            Node node = new Node();
            node.value = entity;

            if (head == null){
                head = node;
                return null;
            }

            Node currentNode = head;
            while (true) {
                if (currentNode.value.key.equals(entity.key)){
                    V buf = (V)currentNode.value.value;
                    currentNode.value.value = entity.value;
                    return buf;
                }
                if (currentNode.next != null){
                    currentNode = currentNode.next;
                }
                else{
                    currentNode.next = node;
                    return null;
                }
            }
        }
        public V remove(K key){
            if (head == null)
                return null;
            if (head.value.key.equals(key)){
                V buf = (V)head.value.value;
                head = head.next;
                return buf;
            }
            else {
                Node node = head;
                while (node.next != null){

                    if (node.next.value.key.equals(key)){
                        V buf = (V)node.next.value.value;
                        node.next = node.next.next;
                        return buf;
                    }
                    node = node.next;
                }
                return null;
            }
        }

        /**
         * Получить значение элемента по ключу
         * @param key Ключ
         * @return Значение
         */
        public V get(K key){
            Node node = head;
            while (node != null){
                if (node.value.key.equals(key))
                    return (V)node.value.value;
                node = node.next;
            }
            return null;
        }

    }

    private int calculateBucketIndex(K key){
        int index = key.hashCode() % buckets.length;
        if (index < 0)
            index = index *-1;
        return index;
    }

    /**
     * Добавление нового элемента
     * @param key Ключ
     * @param value Значение
     * @return Значение предыдущего элемента (после замены, для нового - null)
     */
    public V put(K key, V value){
        int index = calculateBucketIndex(key);
        Bucket bucket = buckets[index];
        if(bucket == null){
            bucket = new Bucket();
            buckets[index] = bucket;
        }

        Entity entity = new Entity();
        entity.key = key;
        entity.value = value;

        return (V)bucket.add(entity);
    }

    /**
     * Удаление элемента по ключу
     * @param key Ключ
     * @return Значение элемента (null - элемент не найден)
     */
    public V remove(K key){
        int index = calculateBucketIndex(key);
        Bucket bucket = buckets[index];
        if (bucket == null)
            return null;
        return (V)bucket.remove(key);
    }

    /**
     * Получить значение элемента по ключу
     * @param key Ключ
     * @return
     */
    public V get(K key){
        int index = calculateBucketIndex(key);
        Bucket bucket = buckets[index];
        if (bucket == null)
            return null;
        return (V)bucket.get(key);
    }

    public HashMap(){
        this(INIT_BUCKET_COUNT);
    }

    public HashMap(int initCount){
        buckets = new Bucket[initCount];
    }

}
"""
