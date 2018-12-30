# 10627121 林峻葦
# DS1ex1: Test permuting numbers.
# 此 Python 程式修改自 DS1ex1 C 語言版本.

###############################################################################

### Import
from timeit import default_timer as timer

###############################################################################

### Structure of Perm_struct
class Perm_struct:
  data = 0 # 原始要進行排列之前所設定的資料
  select = 0 # Flag 表示資料已被選中進排列
  perm = 0 # 進入排列的資料

### 跨 function 用的 global variable
global uArray # 三個任務排列用的陣列
global uArrayLen # 陣列已使用長度, task 2 專用.
global uPermCount # 目前排列的 count

###############################################################################

### Function: main
### Main program
def main():

  # Execute command
  while ( True ):
    Menu() # 顯示選單
    cmd = InputStr() # 輸入命令字串
    if ( cmd == "__EOF__" or cmd == "0"): # End-of-file 或命令 0?
      break; # 跳出迴圈
    if ( cmd == "1" ): # 命令 1?
      task_1() # 執行任務1
    elif ( cmd == "2" ): # 命令 2?
      task_2() # 執行任務2
    elif ( cmd == "3" ): # 命令 3?
      task_3() # 執行任務3
    else:
      ErrorMessage( 0, cmd ) # 顯示錯誤訊息

### Function: Menu
### Show menu
def Menu():
  # 印出命令選單
  print( "\nWelcome to use DS1ex1" )
  print( "0: quit" )
  print( "1: task1" )
  print( "2: task2" )
  print( "3: task3" )
  print( "Please type command : ", end="" )

### Function: ErrorMessage
### Print error message
def ErrorMessage( errorNum, string ):
  # 印出錯誤編號所對應的訊息
  if ( errorNum == 0 ): # 錯誤 0?
    print( "<Error> '" + string + "': No such command!" ) # 無此命令
  elif ( errorNum == 1 ): # 錯誤 1?
    print( "<Error> '" + string + "': Value is not a number!" ) # 非整數
  elif ( errorNum == 2 ): # 錯誤 2?
    print( "<Error> '" + string + "': Value isn't in the range between 2 and 9!" ) # 非 2~9
  elif ( errorNum == 3 ): # 錯誤 3?
    print( "<Error> '" + string + "': Value isn't in the range between 1 and 9!" ) # 非 1~9
  elif ( errorNum == 4 ): # 錯誤 4?
    print( "<Error> '" + string + "': Value isn't in the range between 1 and 999999!" ) # 非 1~999999
  else:
    print( "Unknown error!" ) # 未知錯誤

###############################################################################
#                                   Task 1

### Function: task_1
### Do task 1. N 取 N 之排列.
def task_1():
  global uArray # 此變數為 global
  global uPermCount # 此變數為 global

  N = Input_1() # 輸入 N

  # New array
  uArray = [Perm_struct() for i in range(N)] # 配置 Perm_struct 的 array, 長度 N.

  # Fill 1 to N into array
  for i in range(N): # i = 0 到 i < N
    uArray[i].data = i + 1 # i+1 放入陣列的 data
    uArray[i].select = 0 # 初始為 "未選中"

  # Permutation
  print( "Output:" ) # 在多行排列結果之前先顯示訊息
  uPermCount = 0 # 目前排列 count 初始為 0
  perm( N, N, 0 ) # 呼叫遞迴函數進行排列
  print( "L = " + str(N) ) # 印出 level

  del uArray # 釋放陣列

### Function: Input_1
### Input task1 N
def Input_1():
  # Input an integer
  while ( True ):
    print( "Input N: ", end="" ) # 印出提示
    string = InputStr() # 輸入字串
    N = ErrorCheck_1( string ) # 檢查輸入是否合法
    if ( N > 0 ): # 合法?
      return N # 回傳 N 值

### Function: ErrorCheck_1
### Check task1 N error and convert to integer
def ErrorCheck_1( string ):
  # Is integer?
  if ( not IsInt( string ) ): # 不是整數?
    ErrorMessage( 1, string ) # 顯示錯誤訊息
    return 0 # 回傳失敗值

  # Convert string into integer
  num = int( string ) # 字串轉整數
  if ( num < 1 or num > 9 ): # 超出 1~9?
    ErrorMessage(3, string) # 顯示錯誤訊息
    return 0 # 回傳失敗值

  return num # 回傳輸入的整數

###############################################################################
#                                   Task 2

### Function: task_2
### Do task 2. 輸入 M 個自訂 number, M 取 M 之排列.
def task_2():
  global uArray # 此變數為 global
  global uPermCount # 此變數為 global

  M = Input_2() # 輸入 M 以及 M 個 number

  # Permutation
  print( "Output:" ) # 在多行排列結果之前先顯示訊息
  uPermCount = 0 # 目前排列 count 初始為 0
  startTime = timer() # 儲存起始時間
  perm( M, M, 0 ) # 呼叫遞迴函數進行排列
  endTime = timer() # 儲存結束時間
  print( "T = " + str(endTime - startTime) + " seconds" ) # 印出經過時間

  del uArray # 釋放陣列

### Function: Input_2
### Input task2 M
def Input_2():
  global uArray # 此變數為 global
  global uArrayLen # 此變數為 global

  # Input an integer
  while ( True ):
    print( "Input M: ", end="" ) # 印出提示
    string = InputStr() # 輸入字串
    M = ErrorCheck_2_M( string ) # 檢查輸入是否合法
    if ( M > 0 ): # 合法?
      break # 跳出迴圈

  uArray = [Perm_struct() for i in range(M)] # 配置 Perm_struct 的 array, 長度 M.

  # Input M records of data
  uArrayLen = 0 # 初始 array 已用長度為 0
  while ( uArrayLen < M ): # 當還沒輸入滿 M 個 number
    print( "Input " + str(M - uArrayLen) + " number : ", end="" ) # 印出提示
    string = InputStr() # 輸入字串

    # Check every token in the input string
    list = string.split() # 以 white space 把字串拆開
    for i in range(len(list)): # i = 0 到 i < list 的長度
      num = ErrorCheck_2_num( list[i] ) # 檢查輸入是否合法
      if ( num > 0 ): # 合法?
        # Put into array
        uArray[uArrayLen].data = num # 儲存所輸入的 number
        uArray[uArrayLen].select = 0 # 初始為 "未選中"
        uArrayLen = uArrayLen + 1 # 陣列已用長度加 1
      if ( uArrayLen == M ): # 已經滿 M 個 number?
        break # 跳出迴圈

  return M; # 回傳 M 值

### Function: IsDuplicated
### Check whether data is duplicated in array
def IsDuplicated( data ):
  global uArray # 此變數為 global
  global uArrayLen # 此變數為 global

  # Is data duplicated in the array?
  for i in range(uArrayLen): # i = 0 到 i < uArrayLen
    if ( data == uArray[i].data ): # 資料有重複?
      return True # 回傳是

  return False # 回傳否

### Function: ErrorCheck_2_M
### Check task2 M error and convert to integer
def ErrorCheck_2_M( string ):
  # Is integer?
  if ( not IsInt( string ) ): # 輸入字串不是整數?
    ErrorMessage(1, string) # 顯示錯誤訊息
    return 0 # 回傳失敗值

  # Convert string into integer
  num = int( string ) # 字串轉整數
  if ( num < 2 or num > 9 ): # 超出 2~9?
    ErrorMessage(2, string) # 顯示錯誤訊息
    return 0 # 回傳失敗值

  return num # 回傳輸入的整數

### Function: ErrorCheck_2_num
### Check task2 number error and convert to integer
def ErrorCheck_2_num( string ):
  # Is integer?
  if ( not IsInt( string ) ): # 不是整數?
    ErrorMessage( 1, string ) # 顯示錯誤訊息
    return 0 # 回傳失敗值

  # Check error
  num = int( string ) # 字串轉整數
  if ( num < 1 or num > 999999 ): # 超出 1~999999?
    ErrorMessage(4, string) # 顯示錯誤訊息
    return 0 # 回傳失敗值
  if ( IsDuplicated( num ) ): # 資料有重複?
    print( string + " is duplicated!" ) # 顯示錯誤訊息
    return 0 # 回傳失敗值

  return num # 回傳輸入的整數

###############################################################################
#                                   Task 3

### Function: task_3
### Do task 3. 9 取 M 之排列.
def task_3():
  global uArray # 此變數為 global
  global uPermCount # 此變數為 global

  N = 9 # 本任務為 9 取 M 之排列
  M = Input_3() # 輸入 M

  # New array
  uArray = [Perm_struct() for i in range(N)] # 配置 Perm_struct 的 array, 長度 N.

  # Fill 1 to N into array
  for i in range(N): # i = 0 到 i < N
    uArray[i].data = i + 1 # i+1 放入陣列的 data
    uArray[i].select = 0 # 初始為 "未選中"

  # Permutation
  print( "Output:" ) # 在多行排列結果之前先顯示訊息
  uPermCount = 0 # 目前排列 count 初始為 0
  startTime = timer() # 儲存起始時間
  perm( N, M, 0 ) # 呼叫遞迴函數進行排列
  endTime = timer() # 儲存結束時間
  print( "T = " + str(endTime - startTime) + " seconds" ) # 印出經過時間

  del uArray # 釋放陣列

### Function: Input_3
### Input task3 M
def Input_3():
  # Input an integer
  while ( True ):
    print( "Input M: ", end="" ) # 印出提示
    string = InputStr() # 輸入字串
    M = ErrorCheck_3( string ) # 檢查輸入是否合法
    if ( M > 0 ): # 合法
      return M # 回傳 M 值

### Function: ErrorCheck_3
### Check task3 M error and convert to integer
def ErrorCheck_3( string ):
  # Is integer?
  if ( not IsInt( string ) ): # 不是整數?
    ErrorMessage(1, string) # 顯示錯誤訊息
    return 0 # 回傳失敗值

  # Convert string into integer
  num = int( string ) # 字串轉整數
  if ( num < 1 or num > 9 ): # 超出 1~9?
    ErrorMessage(3, string) # 顯示錯誤訊息
    return 0 # 回傳失敗值

  return num # 回傳輸入的整數

###############################################################################

### Function: InputStr
### Input a string
def InputStr():
  # 重複輸入直到取得非空字串
  while (True):
    try:
      string = input() # 輸入字串
    except EOFError: # End-of-file 錯誤?
      return "__EOF__" # 回傳特殊字串

    if ( len( string ) > 0 ): # 非空字串?
      return string # 回傳輸入的字串

### Function: IsInt
### Check whether strin is integer
def IsInt( string ):
  try:
    num = int( string ) # 字串轉整數
  except ValueError: # 不是正確的整數?
    return False # 回傳失敗

  return True # 回傳成功

### Function: perm
### Do permutation. N 取 M 之排列.
def perm( N, M, level ):
  global uArray # 此變數為 global

  if ( level == M ): # 已取 M 個?
    Print( M ) # 印出目前的排列
    return # 離開函數

  for i in range(N): # i = 0 到 i < N
    if ( not uArray[i].select ): # 第 i 個還沒被選?
      uArray[i].select = 1 # 設定為 "已選中"
      uArray[level].perm = uArray[i].data # 把第 i 個資料放入 level 裡
      perm( N, M, level+1 ) # 遞迴呼叫, level 加 1.
      uArray[i].select = 0 # 回復為 "未選中"

### Function: Print
### Print current permutation
def Print( M ):
  global uArray # 此變數為 global
  global uPermCount # 此變數為 global

  # Print current permutation
  uPermCount = uPermCount + 1 # 目前排列的 count 加 1
  print( "[" + str(uPermCount) + "] ", end="" ) # 印出目前排列的 count
  for i in range(M): # i = 0 到 i < M
    print( uArray[i].perm, end="" ) # 印出目前排列的第 i 個資料
    if ( i != M - 1 ): # 還沒印滿 M 個資料?
      print( ", ", end="" ) # 印出逗號

  print("") # 印換行

###############################################################################

if __name__ == '__main__':
  main() # 呼叫主程式
