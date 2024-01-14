# b4のときのプログラム
----------------------------------------------------------------

学部4年生（B4）のプロジェクトにおけるプログラムの内容をまとめます。このプロジェクトは、粘弾性流体中の気泡の動きを分析するための画像解析とデータ処理に関連しています。以下に、主要な処理と機能を概説します。

### プログラムの主要な機能
動画データの読み込みと基本情報の取得:

指定された動画ファイルを読み込み、動画の基本情報（幅、高さ、総フレーム数、フレームレート）を取得します。
フレームの抽出と保存:

動画から特定のフレームを抽出し、画像ファイルとして保存します。これらの画像は後続の画像処理に使用されます。
画像の回転と輪郭検出:

保存した画像を回転させ、グレースケール変換と2値化処理を施した後、輪郭検出を行います。
膨張・収縮時の気泡の挙動分析:

膨張・収縮時の気泡の画像を抽出し、画像内の気泡の輪郭から面積と位置を計算します。
これらの情報を用いて、気泡の膨張・収縮時の動きを分析します。
自然上昇時の気泡の分析:

特定の動画から自然上昇する気泡の画像を抽出し、同様に輪郭検出と位置の追跡を行います。
上昇速度の計算とグラフ化:

輪郭の中心（図心）の位置変化から気泡の上昇速度を計算し、これらのデータをグラフにして視覚化します。
ピクセルと実際の長さの変換係数計算:

ユーザーが指定した画像上の点間の距離を測定し、ピクセルと実際の長さ（mm）の変換係数を計算します。
総括
このプロジェクトでは、気泡の動きを正確に分析するために、動画データの処理、画像解析、データ計算、および視覚化の各ステップが組み合わされています。これにより、気泡の膨張、収縮、自然上昇の各フェーズにおける動きを詳細に理解し、その特性を数値化することが可能になりました。また、画像処理とデータ解析の技術を駆使して、実験データから有意義な情報を抽出し、科学的な知見を得ることができました。


----------------------------------------------------------------



## 動画データの読み込みと基本情報の取得

関数の概要: 動画ファイルを読み込み、その基本情報（幅、高さ、フレーム数、フレームレート）を取得します。
#### 処理の流れ:
    cv2.VideoCapture を使用して動画ファイルを読み込みます。kMarkdown Preview Enhanced
    cap.get メソッドを使用して、動画の幅、高さ、総フレーム数、フレームレートを取得します。
    フレームの保存と回転処理

関数の概要: 指定されたフレーム数の静止画像を抽出し、それを回転させて保存します。
#### 処理の流れ:
    while ループを使用して動画からフレームを読み込みます。
    cv2.imwrite を使用してフレームを画像として保存します。
    保存した画像を読み込み、cv2.rotate で反時計回りに90度回転させて再保存します。
    静止画像の処理と輪郭の検出

関数の概要: 保存した画像をグレースケールに変換し、2値化して輪郭を検出します。
#### 処理の流れ:
    画像をグレースケールに変換し、cv2.threshold で2値化します。
    cv2.findContours を使用して2値化された画像から輪郭を検出します。
    検出した輪郭を元の画像に描画し、それを保存します。
    気泡の面積計算と最大・最小面積の特定

関数の概要: 各画像の最大輪郭（気泡）の面積を計算し、最大および最小の面積を持つ輪郭を特定します。
#### 処理の流れ:
    気泡の最大膨張時と最小収縮時の特定:
    各フレームで検出された輪郭の中から、面積が最大の輪郭を選択します。これは、cv2.contourArea 関数を用いて行われます。
    選択された輪郭の面積は、気泡のサイズを反映しています。

    面積リストの作成:
    各フレームの最大輪郭面積をリストに保存します。これにより、時間経過に伴う気泡のサイズ変化を追跡できます。

    最大膨張時と最小収縮時の特定:
    保存された面積リストから、面積が最大となるフレーム（最大膨張時）と面積が最小となるフレーム（最小収縮時）を特定します。
    最大面積と最小面積を持つフレームのインデックスを、それぞれidx_max_list と idx_min_list に保存します。
    
    対応する画像の保存:
    最大膨張時と最小収縮時に対応するフレームの画像を別のディレクトリに保存します。これにより、気泡の動態を視覚的に分析することが可能になります。

関数の概要: 気泡の最大膨張時と最小収縮時に対応する画像を特定し、それらを保存します。
#### 処理の流れ:
    最大および最小面積の輪郭に対応する元の画像（回転済み）を特定します。
    これらの画像を別のディレクトリに保存します。

## 膨張時の上昇速度計算
#### 図心の位置の検出:
    連続するフレームの気泡の図心（重心）の位置を計算します。
    cv2.moments 関数を使用して、2値化された画像のモーメントを取得し、これを用いて図心の座標を計算します。
#### 速度の計算:
    連続するフレーム間での図心のY座標の変化量（y_ex）を計算します。
    変化量をフレーム間の時間差（秒単位）で割り、速度（ピクセル/秒）を求めます。
#### 単位の変換: 
    計算された速度をピクセル/秒からmm/秒に変換します。
    収縮時の上昇速度計算
    収縮時の処理も膨張時と同様に行いますが、ここでは収縮時のフレームを使用します。

## プログラムの概要
    1. 動画データの読み込みとフレームの保存
    指定された動画ファイルからフレームを読み込み、各フレームをBMP形式で保存します。
    動画の基本情報（幅、高さ、総フレーム数、フレームレート）を取得します。

    2. 画像の前処理
    保存されたフレームをグレースケールに変換し、明暗の情報のみを抽出します。
    さらに2値化処理を行い、気泡の輪郭と背景のコントラストを強調します。最適な閾値を自動的に決定するために、cv2.THRESH_BINARY_INV と cv2.THRESH_OTSU を使用します。

    3. 輪郭の検出と描画
    2値化された画像から外側の輪郭を検出し、元のフレームに描画して保存します。
    cv2.findContours を使用し、輪郭のすべての点を抽出します。cv2.drawContours を用いて、輪郭を視覚的に強調し、画像に保存します。

    4. 気泡の面積と膨張・収縮の追跡
    気泡の最大膨張時と最小収縮時を特定し、これらの瞬間の画像を保存します。
    輪郭の面積を計算し、面積の変化から気泡の動態を追跡します。
    
    5. 上昇速度の計算
    膨張時と収縮時のそれぞれにおいて、連続するフレームの図心（重心）の位置を計算し、図心の移動から上昇速度を算出します。
    
    6. 自然上昇時の上昇速度計算
    特定の動画から自然上昇時の気泡の動きを含むフレームを抽出し、同様の手順で上昇速度を算出します。
    
    7. グラフ作成と速度の平均値計算
    気泡の膨張時、収縮時、自然上昇時の各フェーズにおける上昇速度をグラフ化します。
    各フェーズの平均上昇速度を計算し、グラフに表示します。
    
    総評
    このプログラムは、真球形状の気泡の膨張時と収縮時、および自然上昇時の上昇速度を自動的に算出することを目的としています。画像処理、輪郭検出、上昇速度の計算などの手法を組み合わせることで、気泡の動態を詳細に分析することが可能です。このプログラムは、気泡の挙動に関する新たな洞察を提供し、さらなる研究の基盤を築くことができます。
