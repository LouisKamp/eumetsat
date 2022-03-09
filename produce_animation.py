# %%
from satpy import Scene, MultiScene
import glob

# %%
filenames = glob.glob("./data/**.nat")
mscn = MultiScene.from_files(filenames, "seviri_l1b_native")
mscn.load(['natural_enh'])

new_mscn = mscn.resample("msg_seviri_fes_3km")

new_mscn.save_animation('{name}_{start_time:%Y%m%d_%H%M%S}.mp4', fps=2)

# %%
