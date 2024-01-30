import pandas as pd
import pyproj
from czml import czml
from datetime import datetime, timedelta
import sys

# 引数のチェックとエラーメッセージの表示
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

# コマンドライン引数からファイル名を取得
filename = sys.argv[1]

# CSVファイルの読み込み
df = pd.read_csv(filename)

# 座標変換用のTransformerを作成(適切なCRSに変更してください)
transformer = pyproj.Transformer.from_crs(6673, 6668)

# 緯度経度へ変換
df['lon'], df['lat'] = transformer.transform(df['ycoord'].values, df['xcoord'].values)

# 基準となる開始時刻
start_time = datetime(2018, 3, 13, 15, 0, 0)

df_elevation = pd.read_csv('標高データ.txt', header=None, names=['lon', 'lat', 'elevation'])

# CZMLドキュメントの作成
czml_doc = czml.CZML()
czml_doc.packets.append(czml.CZMLPacket(id='document', name='CZML', version='1.0'))

# 各行をCZMLパケットに変換
for index, row in df.iterrows():
    positions = []
    for i in range(1, 73):
        if row[str(i)] == 0.5:
            positions.extend([i, row['lat'], row['lon']])
            tol = 0.00000001
            elevation_row = df_elevation[(abs(df_elevation['lat'] - row.lon) < tol) & (abs(df_elevation['lon'] - row.lat) < tol)]
            if not elevation_row.empty:
                positions.append(elevation_row.iloc[0]['elevation'] + row['measuredHe'])
            else:
                positions.append(0)
    if len(positions) > 0:
        # CZMLパケット
        packet = czml.CZMLPacket(
            id=f"{index}_{i}",
            availability="2018-03-13T15:00:00Z/2018-03-13T15:05:00Z",
            position={
                "epoch" : start_time.isoformat() + "Z",
                "cartographicDegrees": positions
            },
            point={
                "pixelSize": 10,
                "color" : {
                    "rgba" : [255, 0, 0, 255]
                },
                "outlineColor" :  {
                    "rgba" : [0, 0, 0, 255]
                },
                "outlineWidth" :2.5 
            },
            description=row["buildingID"]
        )
        czml_doc.packets.append(packet)

# CZMLファイルの出力
with open('flag.czml', 'w') as f:
    f.write(czml_doc.dumps())