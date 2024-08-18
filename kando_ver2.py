def calculate_values(sensitivity, detailed_scope, self_defeat):
    # 現横感度の計算
    current_sensitivity = sensitivity * detailed_scope
    
    # 目標横感度の計算
    target_sensitivity = current_sensitivity + self_defeat
    
    # N の計算
    if current_sensitivity == 0:
        raise ValueError("現横感度がゼロです。計算できません。")
    
    N = target_sensitivity / current_sensitivity
    
    # 最終的な計算結果
    final_value = N * detailed_scope
    
    return current_sensitivity, target_sensitivity, N, final_value

def main():
    while True:
        try:
            # ユーザーからの入力
            sensitivity = float(input("横感度の値を入力してください: "))
            detailed_scope = float(input("詳細スコープの値を入力してください (0.01 から 5.00 の範囲): "))
            self_defeat = float(input("スティックの傾きの値を入力してください (1 から 50 の範囲): "))
            
            # 詳細スコープの範囲チェック
            if not (0.01 <= detailed_scope <= 5.00):
                raise ValueError("詳細スコープの値は 0.01 から 5.00 の範囲内でなければなりません。")
            
            # 自身の倒し方の範囲チェック
            if not (1 <= self_defeat <= 50):
                raise ValueError("スティックの傾きは 1 から 50 の範囲内でなければなりません。")
            
            # 計算
            current_sensitivity, target_sensitivity, N, final_value = calculate_values(sensitivity, detailed_scope, self_defeat)
            
            # 結果の表示
            print(f"\n計算結果:")
            print(f"横感度: {sensitivity}")
            print(f"詳細スコープ: {detailed_scope}")
            print(f"スティックの傾き: {self_defeat}")
            print(f"現横感度: {current_sensitivity}")
            print(f"目標横感度: {target_sensitivity}")
            print(f"N: {N}")
            print(f"最終値: {final_value}")
        
        except ValueError as e:
            print(f"エラー: {e}")
        
        # 続行するかどうかの確認
        cont = input("もう一度計算しますか？ (y/n): ").strip().lower()
        if cont != 'y':
            break
    
    # コンソールウィンドウがすぐに閉じないようにする
    input("終了するには Enter キーを押してください...")

if __name__ == "__main__":
    main()
