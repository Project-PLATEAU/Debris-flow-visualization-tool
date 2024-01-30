-流動深の求め方

rename.pyを実行する。
```
python rename.py
```

標高データ.txtという空のテキストファイルを作成する。  

czml_from_csv_depth.pyを実行する
```
python czml_from_csv_depth.py
```

lonlat_from_czml.pyを実行する
```
python lonlat_from_czml.py depth.czml
```

log_lonlat_JS生成_テンプレ.xlsxにlonlat.txtの緯度・経度を貼り付けてJavaScriptソースコードを生成する。  
  
JavaScriptソースコードをJavaScriptcode.txtに貼り付ける。  
  
ローカルでCesium1.8.5を立ち上げsandcastleを開きJavaScript code.txtを貼り付けてRunする。  
  
出力結果を標高データ.txtに張り付ける。  
  
再度czml_from_csv_depth.pyを実行する。  
```
python czml_from_csv_depth.py
```
出力されたdepth.czmlが流動深のczmlになります。  
  
-流体力の求め方

rename.pyを実行する。
```
python rename.py
```

標高データ.txtという空のテキストファイルを作成する。  

czml_from_csv_fbuilding.pyを実行する
```
python czml_from_csv_fbuilding.py
```

lonlat_from_czml.pyを実行する
```
python lonlat_from_czml.py depth.czml
```

log_lonlat_JS生成_テンプレ.xlsxにlonlat.txtの緯度・経度を貼り付けてJavaScriptソースコードを生成する。  
  
JavaScriptソースコードをJavaScriptcode.txtに貼り付ける。  
  
ローカルでCesium1.8.5を立ち上げsandcastleを開きJavaScript code.txtを貼り付けてRunする。  
  
出力結果を標高データ.txtに張り付ける。  
  
再度czml_from_csv_fbuilding.pyを実行する。  
```
python czml_from_csv_fbuilding.py
```
出力されたfbuilding.czmlが流体力のczmlになります。    
  
-建物崩壊情報の求め方

rename.pyを実行する。
```
python rename.py
```

標高データ.txtという空のテキストファイルを作成する。  

czml_from_csv_collapse.pyを実行する
```
python czml_from_csv_collapse.py
```

lonlat_from_czml.pyを実行する
```
python lonlat_from_czml.py depth.czml
```

log_lonlat_JS生成_テンプレ.xlsxにlonlat.txtの緯度・経度を貼り付けてJavaScriptソースコードを生成する。  
  
JavaScriptソースコードをJavaScriptcode.txtに貼り付ける。  
  
ローカルでCesium1.8.5を立ち上げsandcastleを開きJavaScript code.txtを貼り付けてRunする。  
  
出力結果を標高データ.txtに張り付ける。  
  
再度czml_from_csv_collapse.pyを実行する。  
```
python czml_from_csv_collapse.py
```
出力されたcollapse.czmlが建物崩壊情報のczmlになります。  


-建物崩壊フラグの求め方  

czml_from_bldg_iRIC.pyを実行する。  
```
python czml_from_bldg_iRIC.py Flag\merge_timestep_100_Ⅰ-12125.csv
```
出力されたflag.czmlが建物崩壊フラグのczmlになります。  
