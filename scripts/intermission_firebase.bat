rmdir c:\Github\dp\Internal\firebase\stock_upload /s /q 
call gustil_pull.bat
timeout 3
cd C:\Github\dp\Internal\firebase\stock_upload
ren *.* *.csv 
timeout 3
cd c:\github\dp\internal
python Data_cleaning_firebase.py 
python User_input_firebase.py
timeout 3
call gustil_push.bat
timeout 3  & pause
