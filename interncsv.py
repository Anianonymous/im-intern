import pandas as pd
details={'Device Name':['Pulse Oximeter','Blood Warmer','C-Pap Machine','ECG Machine',
         'HFNC Machine','Infusion Pump','NIBP Monitor'],
         'REF':['NML903055','NML903090','NML903105','NML903060','NML903095','NML903065','NML903050'],
         'LOT':['34683','34641','34662','34690','34648','34697','34676'],
         'Qty':['4','1','1','9','5','10','5'],
        }
df=pd.DataFrame(details)
df.to_csv('details.csv',index=False)
         