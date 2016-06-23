
import tarea

a = """
START
<!--LOOP_START-->
               LEVEL 1:
     <!--DIS_START-->
                   LEVEL 2:[#a]
    <!--DIS_END-->
<!--LOOP_END-->

"""

ds = []
ds.append([{"a": 'UNO'}, {"a": 'DOS'}])
print(tarea.fmt(a, ds, ["LOOP", "DIS"]))
