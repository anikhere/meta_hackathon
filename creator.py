import os 
main_folder = 'supply_chain_env'
file_dir = 'agents'
second_dir = 'tasks'
evaulator = 'evaluator'
config = 'config'
scripts = 'scripts'
files = [
    f'{main_folder}/{file_dir}/__init__.py',
    f'{main_folder}/{file_dir}/inventory_agent.py',
    f'{main_folder}/{file_dir}/forecasting_agent.py',
    f'{main_folder}/{file_dir}/management_agent.py',
    f'{main_folder}/{file_dir}/employee_agent.py',

    
]
if __name__ == "__main__":
   for file in files:
      dirname = os.path.dirname(file)
      os.makedirs(dirname,exist_ok=True)
      with open(file,'w') as f:
         f.write(f'just created the {file}')