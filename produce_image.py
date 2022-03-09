# %%
from satpy.scene import Scene
import glob

# %%


filenames = glob.glob("./data/**.nat")
scn = Scene(reader="seviri_l1b_native", filenames=filenames)
# %%

# scn.available_composite_names()
c = "natural_enh"

# scn.load([c], upper_right_corner="NE")
scn.load([c])

# %%
new_scn = scn.resample("msg_seviri_fes_3km")
# %%

new_scn.show(c)

# %%
new_scn.save_dataset(c, "my_nice_image.png")
# %%
