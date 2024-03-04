# 可視化コンバータ <!-- OSSの対象物の名称を記載ください。分かりやすさを重視し、できるだけ日本語で命名ください。英語名称の場合は日本語説明を（）書きで併記ください。 -->

![概要](.SampleImage.PNG) <!-- OSSの対象物のスクリーンショット（画面表示がない場合にはイメージ画像）を貼り付けください -->

## 1. 概要 <!-- 本リポジトリでOSS化しているソフトウェア・ライブラリについて1文で説明を記載ください -->
本リポジトリでは、Project PLATEAUの令和4年度のユースケース開発業務の一部であるUC23-02「精緻な土砂災害シミュレーション」について、その成果物である「可視化コンバータ」のソースコードを公開しています。

「精緻な土砂災害シミュレーション」は、PLATEAUの3D都市モデルを活用し、家屋の倒壊判定等を加味した精緻な土石流シミュレータを開発。建物損壊リスクを考慮した精緻な避難計画を立案するためのシステムです。

## 2. 「精緻な土砂災害シミュレーション」について <!-- 「」内にユースケース名称を記載ください。本文は以下のサンプルを参考に記載ください。URLはアクセンチュアにて設定しますので、サンプルそのままでOKです。 -->
「精緻な土砂災害シミュレーション」では、カーボンニュートラル施策推進のためのロードマップや計画の策定、太陽光発電を促進する重点エリアや将来の土地利用のあり方の検討などを支援し、地域のカーボンニュートラル施策を推進することを目的として本システムを開発しました。
本システムは、太陽光発電ポテンシャルの推計及び推計結果の建物屋根面への重畳、反射シミュレーション及び光害発生時間の推計といった解析シミュレーション機能に加えて、太陽光発電ポテンシャルの集計機能、建物構造や災害リスク等の条件に応じた太陽光パネル設置の適地判定機能を実装しています。
本システムは、行政職員向けのGUIを備えたオープンソースソフトウェアとしてフルスクラッチで開発されています。
本システムの詳細については[技術検証レポート](https://www.mlit.go.jp/plateau/file/libraries/doc/plateau_tech_doc_0030_ver01.pdf)を参照してください。

## 3. 利用手順 <!-- 下記の通り、GitHub Pagesへリンクを記載ください。URLはアクセンチュアにて設定しますので、サンプルそのままでOKです。 -->
本システムの構築手順及び利用手順については[利用チュートリアル](https://r5-plateau-acn.github.io/SolarPotential/)を参照してください。

## 4. システム概要 <!-- OSS化対象のシステムが有する機能を記載ください。 -->
- 流動深をcsvからczmlに変換します。
- 流体力をcsvからczmlに変換します。
- 建物崩壊情報をcsvからczmlに変換します。
- 建物崩壊フラグをcsvからczmlに変換します。

## 5. 利用技術

| 種別              | 名称   | バージョン | 内容 |
| ----------------- | --------|-------------|-----------------------------|
| ライブラリ      | [pyproj](https://pyproj4.github.io/pyproj/stable/) | 3.6.0 | 地図投影と座標変換ライブラリ |
|       | [czml](https://github.com/cleder/czml) | 0.3.3 | czml読み書きライブラリ |

## 6. 動作環境 <!-- 動作環境についての仕様を記載ください。 -->
| 項目               | 最小動作環境                                                                                                                                                                                                                                                                                                                                    | 推奨動作環境                   | 
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | 
| OS                 | Microsoft Windows 10 または 11                                                                                                                                                                                                                                                                                                                  |  同左 | 
| CPU                | Intel Core i5以上                                                                                                                                                                                                                                                                                                                               | Intel Core i7以上              | 
| メモリ             | 8GB以上                                                                                                                                                                                                                                                                                                                                         | 16GB以上                        | 
| グラフィックカード             | Intel(R) HD Graphics 520以上                                                                                                                                                                                                                                                                                                                                         | NVIDIA GeForce RTX 2080以上                        | 
| ディスプレイ解像度 | 1024×768以上                                                                                                                                                                                                                                                                                                                                    |  1920x1080以上                   | 

## 7. 本リポジトリのフォルダ構成 <!-- 本GitHub上のソースファイルの構成を記載ください。 -->
| フォルダ名 |　詳細 |
|-|-|
| JavaScript code.txt | Cesium実行用のJavaScriptコードです |
| czml_from_bldg_iRIC.py | 建物崩壊フラグをcsvからczmlに変換します |
| czml_from_csv_collapse.py | 建物崩壊情報をcsvからczmlに変換します |
| czml_from_csv_depth.py | 流動深をcsvからczmlに変換します |
| czml_from_csv_fbuilding.py | 流体力をcsvからczmlに変換します |
| log_lonlat_JS生成_テンプレ.xlsx | 緯度経度からJavaScriptコードを生成します |
| lonlat_from_czml.py | czmlから緯度経度を抽出します |
| rename.py | ファイル名を標準化します |

## 8. ライセンス <!-- 変更せず、そのまま使うこと。 -->

- ソースコード及び関連ドキュメントの著作権は国土交通省に帰属します。
- 本ドキュメントは[Project PLATEAUのサイトポリシー](https://www.mlit.go.jp/plateau/site-policy/)（CCBY4.0及び政府標準利用規約2.0）に従い提供されています。

## 9. 注意事項 <!-- 変更せず、そのまま使うこと。 -->

- 本リポジトリは参考資料として提供しているものです。動作保証は行っていません。
- 本リポジトリについては予告なく変更又は削除をする可能性があります。
- 本リポジトリの利用により生じた損失及び損害等について、国土交通省はいかなる責任も負わないものとします。

## 10. 参考資料 <!-- 技術検証レポートのURLはアクセンチュアにて記載します。 -->
- 技術検証レポート: https://www.mlit.go.jp/plateau/file/libraries/doc/plateau_tech_doc_0030_ver01.pdf
- PLATEAU WebサイトのUse caseページ「カーボンニュートラル推進支援システム」: https://www.mlit.go.jp/plateau/use-case/uc22-013/






## 事前準備

rename.pyを実行する。
```
python rename.py
```

標高データ.txtという空のテキストファイルを作成する。  

## 流動深の求め方

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
出力されたdepth.czmlが流動深のczmlとなる。  

## 流体力の求め方

czml_from_csv_fbuilding.pyを実行する
```
python czml_from_csv_fbuilding.py
```

lonlat_from_czml.pyを実行する
```
python lonlat_from_czml.py fbuilding.czml
```

log_lonlat_JS生成_テンプレ.xlsxにlonlat.txtの緯度・経度を貼り付けてJavaScriptソースコードを生成する。  
  
JavaScriptソースコードをJavaScriptcode.txtに貼り付ける。  
  
ローカルでCesium1.8.5を立ち上げsandcastleを開きJavaScript code.txtを貼り付けてRunする。  
  
出力結果を標高データ.txtに張り付ける。  
  
再度czml_from_csv_fbuilding.pyを実行する。  
```
python czml_from_csv_fbuilding.py
```
出力されたfbuilding.czmlが流体力のczmlとなる。    
  
## 建物崩壊情報の求め方

czml_from_csv_collapse.pyを実行する
```
python czml_from_csv_collapse.py
```
出力されたcollapse.czmlが建物崩壊情報のczmlとなる。

## 建物崩壊フラグの求め方  

czml_from_bldg_iRIC.pyを実行する。  
```
python czml_from_bldg_iRIC.py Flag\<csvファイル名>
```

lonlat_from_czml.pyを実行する
```
python lonlat_from_czml.py flag.czml
```

log_lonlat_JS生成_テンプレ.xlsxにlonlat.txtの緯度・経度を貼り付けてJavaScriptソースコードを生成する。  
  
JavaScriptソースコードをJavaScriptcode.txtに貼り付ける。  
  
ローカルでCesium1.8.5を立ち上げsandcastleを開きJavaScript code.txtを貼り付けてRunする。  
  
出力結果を標高データ.txtに張り付ける。  
  
再度czml_from_bldg_iRIC.pyを実行する。  
```
python czml_from_bldg_iRIC.py Flag\merge_timestep_100_Ⅰ-12125.csv
```
出力されたflag.czmlが建物崩壊フラグのczmlとなる。  
