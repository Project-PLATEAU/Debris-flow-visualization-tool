import os

# フォルダ名
folder_name = "./"

# フォルダ中のすべてのファイルに対して実行
for filename in os.listdir(folder_name):
    if filename.startswith("Result_") and filename.endswith(".csv"): # 修正対象のファイル名を指定
        # ファイル番号を抜き出す
        file_number = int(filename.split("_")[1].split(".")[0])
        # 新しいファイル名を作成する（0詰め3桁）
        new_filename = "Result_{:03d}.csv".format(file_number)
        # ファイル名を変更する
        os.rename(os.path.join(folder_name, filename), os.path.join(folder_name, new_filename))