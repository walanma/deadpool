rmdir c:\Github\dp\Internal\firebase\stock_upload /s /q 
call gustil_pull.bat
timeout 3
cd C:\Github\dp\Internal\firebase\stock_upload
ren *.* *.csv 
timeout 3
cd C:\Github\dp\Internal\
python C:\Github\dp\Internal\Data_cleaning_git.py
python C:\Github\dp\Internal\User_input.py
cd C:\Github\dp\Internal\deadpool
git add .
git commit -am "Daily merged update"
git push -u origin gh-pages & pause

