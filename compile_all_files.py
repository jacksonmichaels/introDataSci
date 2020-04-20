import pandas as pd
import glob

path = "data" # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

print(frame.shape)

frame.to_csv("data/compiled.csv")
print("done saving")