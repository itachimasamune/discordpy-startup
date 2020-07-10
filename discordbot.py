from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):    # メッセージ送信者がBotだった場合は無視する    
    if message.author.bot:
        if message.content == 'じゃあの':             
            await message.channel.send('ばいびー')
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/test':
        await message.channel.send(random.choice(('てすてす','ああ～、あああ～','チェックワンツー','イッツファイントゥデイ','あー、あー、マイクテスト','あーあー','本日は晴天なり','超テスト','ファイナルテスト','シンプルイズテスト','過剰なテスト','試験','品質テスト','まごころテスト','テスト','えっ？','てきとーなテスト','ハーデスト','てすてすてすてすてすてすてすてす','TEST','伝説のテスト')))
    elif message.content == '/buki':
        await message.channel.send(random.choice(('スプラシューター','スプラシューターコラボ','スプラシューターベッチュー','プライムシューター','プライムシューターコラボ','プライムシューターベッチュー','シャープマーカー','シャープマーカーネオ','わかばシューター','もみじシューター','おちばシューター','プロモデラーMG','プロモデラーRG','プロモデラーPG','N-ZAP85','N-ZAP89','N-ZAP83','.52ガロン','.52ガロンデコ','.52ガロンベッチュー','ジェットスイーパー','ジェットスイーパーカスタム','L3リールガン','L3リールガンD','L3リールガンベッチュー','.96ガロン','.96ガロンデコ','H3リールガン','H3リールガンD','H3リールガンチェリー','ボールドマーカー','ボールドマーカーネオvボールドマーカー7','ボトルガイザー','ボトルガイザーフォイル','ホットブラスター','ホットブラスターカスタム','ラピッドブラスター','ラピッドブラスターデコ','ラピッドブラスターベッチュー','ノヴァブラスター','ノヴァブラスターネオ','ノヴァブラスターベッチュー','クラッシュブラスター','クラッシュブラスターネオ','Rブラスターエリート','Rブラスターエリートデコ','ロングブラスター','ロングブラスターカスタム','ロングブラスターネクロ','スプラローラー','スプラローラーコラボ','スプラローラーベッチュー','ダイナモローラー','ダイナモローラーテスラ','ダイナモローラーベッチュー','カーボンローラー','カーボンローラーデコ','ヴァリアブルローラー','ヴァリアブルローラーフォイル','ホクサイ','ホクサイ・ヒュー','ホクサイベッチュー','パブロ','パブロ・ヒュー','パーマネント・パブロ','スプラチャージャー','スプラスコープ','スプラチャージャーコラボ','スプラスコープコラボ','スプラチャージャーベッチュー','スプラスコープベッチュー','リッター4K','4Kスコープ','リッター4Kカスタム','4Kスコープカスタム','ソイチューバー','ソイチューバーカスタム','スクイックリンα','スクイックリンβ','スクイックリンγ','14式竹筒銃・甲','14式竹筒銃・乙','14式竹筒銃・丙','バケットスロッシャー','バケットスロッシャーデコ','バケットスロッシャーソーダ','ヒッセン','ヒッセン・ヒュー','スクリュースロッシャー','スクリュースロッシャーネオ','スクリュースロッシャーベッチュー','エクスプロッシャー','エクスプロッシャーカスタム','オーバーフロッシャー','オーバーフロッシャーデコ','バレルスピナー','バレルスピナーデコ','バレルスピナーリミックス','スプラスピナー','スプラスピナーコラボ','スプラスピナーベッチュー','ハイドラント','ハイドラントカスタム','クーゲルシュライバー','クーゲルシュライバー・ヒュー','ノーチラス47','ノーチラス79','スプラマニューバー','スプラマニューバーコラボ','スプラマニューバーベッチュー','スパッタリー','スパッタリー・ヒュー','スパッタリークリア','デュアルスイーパー','デュアルスイーパーカスタム','ケルビン525','ケルビン525デコ','ケルビン525ベッチュー','クアッドホッパーブラック','クアッドホッパーホワイト','パラシェルター','パラシェルターソレーラ','キャンピングシェルター','キャンピングシェルターソレーラ','キャンピングシェルターカーモ','スパイガジェット','スパイガジェットソレーラ','スパイガジェットベッチュー')))
    elif message.content == '/regulation':
        await message.channel.send('ルール：')
        await message.channel.send(random.choice(('ガチアサリ','ガチアサリ','ガチホコ','ガチホコ','ガチエリア','ガチエリア','ガチアサリ','ガチアサリ','ガチホコ','ガチホコ','ガチエリア','ガチエリア','ナワバリバトル')))
        await message.channel.send('ステージ：')
        await message.channel.send(random.choice(('バッテラストリート','フジツボスポーツクラブ','ガンガゼ野外音楽堂','コンブトラック','海女美術大学','チョウザメ造船','タチウオパーキング','ホッケふ頭','マンタマリア号','モズク農園','エンガワ河川敷','Bバスパーク','ザトウマーケット','ハコフグ倉庫','デボン海洋博物館','アロワナモール','アジフライスタジアム','ショッツル鉱山','モンガラキャンプ場','スメーシーワールド','ホテルニューオートロ','アンチョビットゲームズ','ムツゴ楼
        await message.channel.send('縛り：')
        await message.channel.send(random.choice(('チームに一人以上','全員','禁止')))
        await message.channel.send(random.choice(('スプラシューター','スプラシューターコラボ','スプラシューターベッチュー','プライムシューター','プライムシューターコラボ','プライムシューターベッチュー','シャープマーカー','シャープマーカーネオ','わかばシューター','もみじシューター','おちばシューター','プロモデラーMG','プロモデラーRG','プロモデラーPG','N-ZAP85','N-ZAP89','N-ZAP83','.52ガロン','.52ガロンデコ','.52ガロンベッチュー','ジェットスイーパー','ジェットスイーパーカスタム','L3リールガン','L3リールガンD','L3リールガンベッチュー','.96ガロン','.96ガロンデコ','H3リールガン','H3リールガンD','H3リールガンチェリー','ボールドマーカー','ボールドマーカーネオvボールドマーカー7','ボトルガイザー','ボトルガイザーフォイル','ホットブラスター','ホットブラスターカスタム','ラピッドブラスター','ラピッドブラスターデコ','ラピッドブラスターベッチュー','ノヴァブラスター','ノヴァブラスターネオ','ノヴァブラスターベッチュー','クラッシュブラスター','クラッシュブラスターネオ','Rブラスターエリート','Rブラスターエリートデコ','ロングブラスター','ロングブラスターカスタム','ロングブラスターネクロ','スプラローラー','スプラローラーコラボ','スプラローラーベッチュー','ダイナモローラー','ダイナモローラーテスラ','ダイナモローラーベッチュー','カーボンローラー','カーボンローラーデコ','ヴァリアブルローラー','ヴァリアブルローラーフォイル','ホクサイ','ホクサイ・ヒュー','ホクサイベッチュー','パブロ','パブロ・ヒュー','パーマネント・パブロ','スプラチャージャー','スプラスコープ','スプラチャージャーコラボ','スプラスコープコラボ','スプラチャージャーベッチュー','スプラスコープベッチュー','リッター4K','4Kスコープ','リッター4Kカスタム','4Kスコープカスタム','ソイチューバー','ソイチューバーカスタム','スクイックリンα','スクイックリンβ','スクイックリンγ','14式竹筒銃・甲','14式竹筒銃・乙','14式竹筒銃・丙','バケットスロッシャー','バケットスロッシャーデコ','バケットスロッシャーソーダ','ヒッセン','ヒッセン・ヒュー','スクリュースロッシャー','スクリュースロッシャーネオ','スクリュースロッシャーベッチュー','エクスプロッシャー','エクスプロッシャーカスタム','オーバーフロッシャー','オーバーフロッシャーデコ','バレルスピナー','バレルスピナーデコ','バレルスピナーリミックス','スプラスピナー','スプラスピナーコラボ','スプラスピナーベッチュー','ハイドラント','ハイドラントカスタム','クーゲルシュライバー','クーゲルシュライバー・ヒュー','ノーチラス47','ノーチラス79','スプラマニューバー','スプラマニューバーコラボ','スプラマニューバーベッチュー','スパッタリー','スパッタリー・ヒュー','スパッタリークリア','デュアルスイーパー','デュアルスイーパーカスタム','ケルビン525','ケルビン525デコ','ケルビン525ベッチュー','クアッドホッパーブラック','クアッドホッパーホワイト','パラシェルター','パラシェルターソレーラ','キャンピングシェルター','キャンピングシェルターソレーラ','キャンピングシェルターカーモ','スパイガジェット','スパイガジェットソレーラ','スパイガジェットベッチュー','ハイパープレッサー','ジェットパック','インクアーマー','スーパーチャクチ','バブルランチャー','スプラッシュボムピッチャー','キューバンボムピッチャー','ロボットボムピッチャー','カーリングボムピッチャー','ナイスダマ','ウルトラハンコ','マルチミサイル','アメフラシ','イカスフィア','クイックボムピッチャー','スプラッシュボム','キューバンボム','クイックボム','カーリングボム','ロボットボム','スプラッシュシールド','トラップ','ポイズンミスト','ポイントセンサー','スプリンクラー','ジャンプビーコン','タンサンボム','トーピード','シューター','チャージャー','ローラー','スピナー','スロッシャー','ブラスター','マニューバー','フデ','シェルター')))

                                                  
        
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
