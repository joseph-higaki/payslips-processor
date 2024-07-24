
rem /* conda env
conda env create --prefix .\conda-envs\payslips-processor-env --file environment.yml 
conda activate .\conda-envs\payslips-processor-env
conda env remove -p .\conda-envs\payslips-processor-env

rem /*********** adding code  ******************/


git init
git config --local user.name "Joseph Higaki" | git config --local user.email "josephhigaki@hotmail.com"
git remote add origin git@github.com:joseph-higaki/payslips-processor.git
git add .
git commit -m 'first commit' 
git push origin main 



git checkout add-main-logic

git commit -m 'Add logic and unit tests'

git checkout main
git merge add-main-logic
git push origin main 
