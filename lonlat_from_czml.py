import json
import sys

# 引数のチェックとエラーメッセージの表示
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

# コマンドライン引数からファイル名を取得
filename = sys.argv[1]

# CZMLファイルを開く
with open(filename, 'r') as f:
    data = json.load(f)

# 緯度と経度のリストを作成
longitudes = []
latitudes = []

# setを利用する場合
coord_set = set()

# 全てのデータセットに対して
for dataset in data:
    if 'position' in dataset:
        coordinates = dataset['position']['cartographicDegrees']
        # イテレーションのステップ幅を4にして緯度経度のペアを取得
        for i in range(0, len(coordinates), 4):
            longitude = coordinates[i+1]
            latitude = coordinates[i+2]
            coord_set.add((longitude, latitude))

# 出力ファイル名を変更する（オプション）
output_filename = 'lonlat.txt'

with open(output_filename, 'w') as f:
    for lon, lat in coord_set:
        f.write('{0},{1}\n'.format(lon, lat))