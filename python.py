import pandas as pd

dataset = pd.read_csv('nutrition.csv')


if content == 'Low fat products':
            dataset['fat_100g'].isin(range(10))
            low_fat=dataset.loc[dataset['fat_100g']==True]
            fat=low_fat['product_name']
            print(fat)


            
dataset['fat_100g'].isin(range(10))
low_fat=dataset.loc[dataset['fat_100g']==True]
fat=low_fat['product_name']
print(fat)

dataset['sugars_100g'].isin(range(10))
low_sugar=dataset.loc[dataset['sugars_100g']==True]
sugar=low_sugar['product_name']
print(sugar)

dataset['proteins_100g'].isin(range(20,100))
protein_rich=dataset.loc[dataset['proteins_100g']==True]
protein=protein_rich['product_name']
print(protein)

dataset['salt_100g'].isin(range(1))
low_salt=dataset.loc[dataset['salt_100g']==True]
salt=low_salt['product_name']
print(salt)

dataset['carbohydrates_100g'].isin(range(20))
low_carb=dataset.loc[dataset['carbohydrates_100g']==True]
carb=low_carb['product_name']
print(carb)

dataset['energy_100g'].isin(range(1500,3000))
energy_booster=dataset.loc[dataset['energy_100g']==True]
energy=energy_booster['product_name']
print(energy)

