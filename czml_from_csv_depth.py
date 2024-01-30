import os
import pandas as pd
import pyproj
import matplotlib.pyplot as plt
import czml
from datetime import datetime, timedelta
import matplotlib.cm as cm
import time
from multiprocessing import Pool

def getColor(depth, df_all, norm, cmap):
    rgba_color = cmap(norm(depth))
    return [int(x * 255) for x in rgba_color[:3]] + [100]

def process_group(args):
    name, group, df_elevation, df_all, start_time, norm, cmap = args
    positions = []
    colors = {"epoch": start_time.isoformat() + "Z", "rgba":[]}
    for row in group.itertuples():
        if row.Depth != 0:
            positions.extend([row.time, row.lat, row.lon])
            tol = 0.00000001
            elevation_row = df_elevation[(abs(df_elevation['lat'] - row.lon) < tol) & (abs(df_elevation['lon'] - row.lat) < tol)]
            if not elevation_row.empty:
                positions.append(elevation_row.iloc[0]['elevation'])
            else:
                positions.append(0)
            color = getColor(row.Depth, df_all, norm, cmap)
            colors["rgba"].extend([row.time]+color)
    print(f"Processed group {name+1}.")
    if len(positions) > 0:
        packet = czml.CZMLPacket(
            id=f'shape{name+1}',
            name='TOKYO',
            availability="2018-03-13T15:00:00Z/2018-03-13T15:05:00Z",
            position={"epoch": start_time.isoformat() + "Z", "cartographicDegrees": positions},
            point={
                "pixelSize": 8,
                "color": colors},
        )
        return packet
    else:
        return None

def main():
    start = time.time()
    start_time = datetime(2018, 3, 13, 15, 0, 0)
    df_elevation = pd.read_csv('標高データ.txt', header=None, names=['lon', 'lat', 'elevation'])
    doc = czml.CZML()
    doc.packets.append(czml.CZMLPacket(id='document', name='CZML', version='1.0'))
    transformer = pyproj.Transformer.from_crs(6673, 6668)
    folder_name = "./"
    dfs = []
    for i, filename in enumerate(sorted(os.listdir(folder_name))):
        if filename.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder_name, filename), skiprows=2)
            df['lon'], df['lat'] = transformer.transform(df['Y'].values, df['X'].values)
            df['time'] = i - 1
            dfs.append(df)
    df_all = pd.concat(dfs)
 
    norm = plt.Normalize(df_all['Depth'].min(), df_all['Depth'].max())
    cmap = cm.get_cmap('jet')
    
    grouped = [(name, df, df_elevation, df_all, start_time, norm, cmap) for name, df in df_all.groupby(df_all.index)]

    packets = []
    for group in grouped:
        packet = process_group(group)
        if packet is not None:
            packets.append(packet)

    for packet in packets:
        doc.packets.append(packet)

    # CZMLファイルの出力
    with open('depth.czml', 'w') as f:
        f.write(str(doc.dumps()))

    # タイムスタンプ終了、経過時間表示  
    end = time.time()
    print("Execution time: {:.2f} seconds".format(end - start))

if __name__ == '__main__':
    main()