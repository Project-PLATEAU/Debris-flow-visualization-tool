import os
import pandas as pd
import pyproj
import matplotlib.pyplot as plt
import czml
from datetime import datetime, timedelta
import matplotlib.cm as cm
import time
from multiprocessing import Pool
import numpy as np
import dateutil.parser

id = 0

def get_shifted_position1(lat, lon, alt):
    lat_shift = -1.0 / 111000  # 1m shift in latitude (degrees)
    lon_shift =  1.0 / (111000 * np.cos(np.deg2rad(lat)))  # 1m shift in longitude (degrees)
  
    new_lat = lat - lat_shift  # subtract for South shift
    new_lon = lon + lon_shift  # add for East shift
    new_alt = alt  # altitude remains the same
  
    return [new_lat, new_lon, new_alt]

def get_shifted_position2(lat, lon, alt):
    lat_shift = 1.0 / 111000  # 1m shift in latitude (degrees)
    lon_shift = 1.0 / (111000 * np.cos(np.deg2rad(lat)))  # 1m shift in longitude (degrees)
  
    new_lat = lat - lat_shift  # subtract for South shift
    new_lon = lon + lon_shift  # add for East shift
    new_alt = alt  # altitude remains the same
  
    return [new_lat, new_lon, new_alt]

def get_shifted_position3(lat, lon, alt):
    lat_shift =  1.0 / 111000  # 1m shift in latitude (degrees)
    lon_shift = -1.0 / (111000 * np.cos(np.deg2rad(lat)))  # 1m shift in longitude (degrees)
  
    new_lat = lat - lat_shift  # subtract for South shift
    new_lon = lon + lon_shift  # add for East shift
    new_alt = alt  # altitude remains the same
  
    return [new_lat, new_lon, new_alt]

def get_shifted_position4(lat, lon, alt):
    lat_shift = -1.0 / 111000  # 1m shift in latitude (degrees)
    lon_shift = -1.0 / (111000 * np.cos(np.deg2rad(lat)))  # 1m shift in longitude (degrees)
  
    new_lat = lat - lat_shift  # subtract for South shift
    new_lon = lon + lon_shift  # add for East shift
    new_alt = alt  # altitude remains the same
  
    return [new_lat, new_lon, new_alt]

def create_show_intervals(times):
    intervals = []
    for i, t in enumerate(times):
        if i == 0:
            # 初めのポイントから次のポイントまでを表示
            start_time = dateutil.parser.parse("2018-03-13T15:00:00Z")
            start_time += timedelta(seconds=times[i])
            end_time = dateutil.parser.parse("2018-03-13T15:00:00Z")
            end_time += timedelta(seconds=times[i + 1])
            interval = {"interval": f"{start_time.replace(tzinfo=None).isoformat()}Z/{end_time.replace(tzinfo=None).isoformat()}Z", "boolean": True}
        elif i == len(times) - 1:
            # 最後のポイントは表示しない
            start_time = dateutil.parser.parse("2018-03-13T15:00:00Z")
            start_time += timedelta(seconds=times[i])
            interval = {"interval": f"{start_time.replace(tzinfo=None).isoformat()}Z/9999-12-31T23:59:59Z", "boolean": False}
        else:
            # 現在のポイントから次のポイントまでを表示
            start_time = dateutil.parser.parse("2018-03-13T15:00:00Z")
            start_time += timedelta(seconds=times[i])
            end_time = dateutil.parser.parse("2018-03-13T15:00:00Z")
            end_time += timedelta(seconds=times[i + 1])
            interval = {"interval": f"{start_time.replace(tzinfo=None).isoformat()}Z/{end_time.replace(tzinfo=None).isoformat()}Z", "boolean": True}
        intervals.append(interval)
    return intervals

def process_group(args):
    name, group, df_elevation, df_all, start_time, norm, cmap = args
    positions = []
    colors = []
    times = []
    count = 0
    for row in group.itertuples():
        if row.Building != 0:
            if count % 5 == 0:
                positions.extend([row.lat, row.lon])
                tol = 0.00000001
                elevation_row = df_elevation[(abs(df_elevation['lat'] - row.lon) < tol) & (abs(df_elevation['lon'] - row.lat) < tol)]
                if not elevation_row.empty:
                    positions.append(elevation_row.iloc[0]['elevation'])
                else:
                    positions.append(0)
                colors.append([255, 0, 0, 255] if row.Building != 1 else [0, 0, 255, 0])
                times.append(row.time)
            count = count + 1
    lines = []
    print(f"Processed group {name+1}.")
    if len(positions) > 3:
        show_intervals = create_show_intervals(times)
        for i in range(0, len(positions)-3, 3):  # except last 4 elements
            global id
            id = id + 1
            position = positions[i+0:i+3]
            position1 = get_shifted_position1(*position)  # get position shifted by 1m South and 1m East
            position2 = get_shifted_position2(*position)  # get position shifted by 1m South and 1m East
            position3 = get_shifted_position3(*position)  # get position shifted by 1m South and 1m East
            position4 = get_shifted_position4(*position)  # get position shifted by 1m South and 1m East
            packet = czml.CZMLPacket(
                id=f'line{id}',
                name='TOKYO',
                availability="2018-03-13T15:00:00Z/2018-03-13T15:05:00Z",
                polygon={
                    "positions": {"epoch": start_time.isoformat() + "Z", "cartographicDegrees": position1 + position2 + position3 + position4},
                    "material": {
                        "solidColor": {
                            "color": {
                                "rgba" : colors[int(i/3)] 
                            }
                        }
                    },
                    "show": show_intervals[int(i/3)]
                }
            )
            lines.append(packet)

        return lines
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

    all_lines = []
    for group in grouped:
        lines = process_group(group)
        if lines is not None:
            all_lines.append(lines)

    for lines in all_lines:
        for packet in lines:
            doc.packets.append(packet)

    # CZMLファイルの出力
    with open('collapse.czml', 'w') as f:
        f.write(str(doc.dumps()))

    # タイムスタンプ終了、経過時間表示  
    end = time.time()
    print("Execution time: {:.2f} seconds".format(end - start))

if __name__ == '__main__':
    main()