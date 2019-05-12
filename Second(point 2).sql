SELECT a.*
FROM Personal a, Personal b
WHERE b.id=a.id_head
and a.sal> b.sal